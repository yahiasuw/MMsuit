# Component Specifications

## 1 **System Requirements**
- Python 3.8+
- Required Libraries:
  - **Dash**: For building the web application interface.
  - **Plotly**: For interactive visualizations and plotting.
  - **Pandas**: For handling data manipulation and analysis.
  - **NumPy**: For numerical operations and calculations.
  - **SciPy**: For optimization routines, particularly to fit data to the Michaelis-Menten equation.
  
## 2 **Architecture**
- **Frontend (Dash)**: The frontend will be a Dash app, providing a responsive, interactive web interface.
  *Experiment Excuter*
  - *Inputs*:Upload button: Allows the user to upload a CSV file
  - *Outputs*: Display Km, Display Vmax, plot Michaelis Menten plot, plot Lineweaver-Burk Plot
  *MM executer*
  - Km and Vmax input boxes: allows the user to input
  - 
- **Backend**: The backend will be responsible for processing the uploaded data, performing kinetic calculations, and simulating enzyme kinetics. This will be implemented using Python.
  - MMvelocity: calculates velocity via Michaelis-Menten equation *see below*
  - LBfitter: *given substrate concentrations and velocities* fits and minimizes Lineweaver-Burk equation
  - MMfitter: *given substrate concentrations and velocities*, fits and minimizes Michaelis-Menten curve and computes Km and Vmax
  - MMplot:  *given substrate concentrations and velocities* plots Michaelis menten plot using Plotly and MMfitter
  - LBplot:  *given substrate concentrations and velocities* plots Lineweaver-Burk plot using Plotly and LBfitter
  - MMsimulator: *given Vmax and Km* simulates a Michaelis Menten plot using given parameters

## 3 **Kinetic Calculation Details**
- **Michaelis-Menten Equation**: The basic form of the equation is:

  $V = \frac{V_{max} [S]}{K_m + [S]}$
  Where:
  - $V$ = reaction velocity
  - $[S]$ = substrate concentration
  - $K_m$ = Michaelis constant
  - $V_{max}$ = maximum reaction velocity
  
- **Lineweaver-Burk Plot**: A linearized form of the Michaelis-Menten equation, given by:
  
  $\frac{1}{V} = \frac{K_m}{V_{max}} \cdot \frac{1}{[S]} + \frac{1}{V_{max}}$

- **Additional Calculations**:
  - $k_{cat} = \frac{V_{max}}{[E]_{\text{total}}}$
  - $t_{1/2} = \frac{\ln 2}{k}$, where $k$ is the rate constant.

## 6. Timeline *{5 days each}*
- **Backend development**: Successfully computing different constants and plotting graphs (achieved)
- **Frontend development**: Transfering functions to dash framework (achieved)
- **Testing**: building tests for the application
