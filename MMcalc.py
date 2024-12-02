#Dependencies

#Load Packages
from scipy import stats
from scipy import optimize as op
import numpy as np
import plotly.graph_objects as go


#Define equations
def MMvelocity(S:float, Km:float, Vmax:float)-> float:
    '''
    Inputs: Michaelis-Menten equation parameters (S, Km, Vmax).
    Output: Velocity for given S
    '''
    return Vmax*S/(Km + S)

def kcat(Vmax: float,Et: float) -> float:
    '''
    Inputs: Vmax and Et {Enzyme active site concentration}.
    Output: Kcat
    '''
    return Vmax/Et

def LBfitter(eSV: tuple):
    '''
    Inputs: eSV:(Experimental data) tuple with two arrays (substrate array, velocities array)
    :return: tuple with two arrays of fitted data (substrate array, velocities array), Km, Vmax,Pearson correlation coefficient(r), p-value(p), standard error(std_err)
    '''
    srecep = 1/(eSV[0])
    vrecep = 1/(eSV[1])
    #Calculate zscore to remove outliers (> 2 SD)
    z_scores = stats.zscore(vrecep)
    filtered_vrecep = vrecep[np.abs(z_scores) < 2]
    filtered_srecep = np.delete(srecep, np.where(np.abs(z_scores) > 2)) #Remove corresponding indices from substrate concentrations
    def objective(params):
        slope, intercept = params
        y_pred = slope * filtered_srecep + intercept
        return np.sum((filtered_vrecep - y_pred) ** 2)  # Minimize the residual sum of squares
    # Initial guess by linear regression of LB equation
    initial_slope, initial_intercept, *_ = stats.linregress(filtered_srecep, filtered_vrecep)
    bounds = [(-np.inf, np.inf), (0, np.inf)]      # Reject negative values for y-intercept
    # Optimization
    optimized = op.minimize(
        objective,
        x0=[initial_slope, max(0, initial_intercept)],
        bounds=bounds
    )

    # Extract optimized parameters
    slope, intercept= optimized.x

    ###
    Vmax = 1 / intercept
    Km = Vmax * slope
    fittedx = filtered_srecep
    fittedx = np.insert(fittedx, [0,0], [-1/Km,0])
    fittedy = (slope*fittedx)+intercept
    fittedLB = (fittedx, fittedy)
    return fittedLB, Km, Vmax
def MMfitter(eSV: tuple):
    '''
    Inputs:
    eSV: (Experimental data) tuple with two arrays (substrate array, velocities array)
    :return: tuple with two arrays of fitted data (substrate array, velocities array), optimized parameters, covariance of optimized parameters
    '''
    def residual_sum_of_squares(params):
        Vmax, Km = params
        predicted = MMvelocity(eSV[0], Vmax, Km)
        residuals = eSV[1] - predicted
        return np.sum(residuals ** 2)  # Sum of squared residuals

    # Initial guess for Vmax and Km using LBfitter
    LBfunc = LBfitter(eSV)
    initial_guess = [LBfunc[2], LBfunc[1]]

    # Minimize the RSS
    result = op.minimize(residual_sum_of_squares, initial_guess, bounds=[(0, None), (0, None)])
    popt = result.x  # Optimized parameters

    # Covariance estimation from curve_fit for comparison
    popt_curvefit, pcov_curvefit = op.curve_fit(MMvelocity, eSV[0], eSV[1])

    # Fitted substrate and velocities using minimized parameters
    fittedSV = (eSV[0], MMvelocity(eSV[0], *popt))

    return fittedSV, popt, result.fun, pcov_curvefit

#Plotting functions
def MMplot(expSV):
    '''
    Inputs: expSV: (Experimental data) tuple with two arrays (substrate array, velocities array)
    returns: Michaelis-Menten plot with experimental and fitted data.
    '''
    figMM = go.Figure()
    figMM.add_trace(go.Scatter(x=expSV[0], y=expSV[1], mode='markers', name='Experimental'))  # Experimental as scatter
    fitted = MMfitter(expSV)
    figMM.add_trace(go.Line(x=fitted[0][0], y=fitted[0][1], mode='lines', name='Fitted'))  # Fitted as line
    figMM.update_layout(title='Michaelis-Menten Plot', xaxis_title='Substrate concentration', yaxis_title='Velocity')
    #figMM.show()
    return figMM

def MMsimulator(Km:float,Vmax:float):
    '''
    Inputs: Km, Vmax
    :param Km:
    :param Vmax:
    :return: simulated Michaelis-Menten plot
    '''
    xsimulate = np.linspace(Km*(0.1),Km*10,100)
    ysimulate = MMvelocity(xsimulate,Km,Vmax)
    figsimulate = go.Figure()
    figsimulate.add_trace(go.Scatter(x=xsimulate, y=ysimulate, mode='lines', name='Simulated'))
    figsimulate.update_layout(title='Michaelis-Menten Plot', xaxis_title='Substrate concentration', yaxis_title='Velocity')
    #figsimulate.show()
    return figsimulate

def LBplot(expSV:tuple):
    '''
    Inputs: expSV: (Experimental data) tuple with two arrays (substrate array, velocities array)
    returns: Lineweaver-Burk plot with experimental and fitted data.
    '''
    srecep = 1 / (expSV[0])
    vrecep = 1 / (expSV[1])
    figLB = go.Figure()
    figLB.add_trace(go.Scatter(x=srecep, y=vrecep, mode='markers', name='Experimental'))  # Experimental as scatter
    LBfitted = LBfitter(expSV)
    figLB.add_trace(go.Line(x= LBfitted[0][0], y=LBfitted[0][1], mode='lines', name='Fitted'))  # Fitted as line
    figLB.update_layout(title='Lineweaver-Burk Plot', xaxis_title='1/Substrate', yaxis_title='1/Velocity')
    #figLB.show()
    return figLB

