import pytest
from MMsuit.MMcalc import *

# Synthetic good data
@pytest.fixture
def syndata():
    # S = np.array(np.linspace(1, 80, 50))
    # V = MMvelocity(xSubstrate, 40, 10)
    S = np.round(np.array([1.0, 2.612244897959184, 4.224489795918368, 5.836734693877551, 7.448979591836735, 9.061224489795919, 10.673469387755102, 12.285714285714286, 13.89795918367347, 15.510204081632653, 17.122448979591837, 18.73469387755102, 20.346938775510203, 21.959183673469386, 23.571428571428573, 25.183673469387756, 26.79591836734694, 28.408163265306122, 30.020408163265305, 31.63265306122449, 33.244897959183675, 34.857142857142854, 36.46938775510204, 38.08163265306123, 39.69387755102041, 41.30612244897959, 42.91836734693877, 44.53061224489796, 46.142857142857146, 47.755102040816325, 49.36734693877551, 50.97959183673469, 52.59183673469388, 54.204081632653065, 55.816326530612244, 57.42857142857143, 59.04081632653061, 60.6530612244898, 62.26530612244898, 63.87755102040816, 65.48979591836735, 67.10204081632654, 68.71428571428571, 70.3265306122449, 71.93877551020408, 73.55102040816327, 75.16326530612245, 76.77551020408163, 78.38775510204081, 80.0]),3)
    V = np.round(np.array([0.24390243902439024, 0.6130268199233716, 0.95523765574527, 1.2733748886910061, 1.5698924731182797, 1.8469217970049918, 2.1063229963753525, 2.349726775956284, 2.578568723968194, 2.794117647058824, 2.9974991068238657, 3.1897150799166085, 3.371660466689212, 3.544137022397892, 3.707865168539326, 3.8634940513462745, 4.011610143599144, 4.1527446300715996, 4.2873797726610325, 4.415954415954417, 4.538868765672889, 4.65648854961832, 4.769148652255137, 4.877156299006796, 4.980793854033291, 5.080321285140562, 5.175978341127246, 5.267986479961372, 5.356550580431178, 5.441860465116279, 5.524092258506508, 5.603409600717811, 5.679964734405995, 5.7538994800693235, 5.825346112886049, 5.894428152492669, 5.961261075623327, 6.02595296025953, 6.088605068848534, 6.149312377210217, 6.208164054942929, 6.265243902439024, 6.320630749014454, 6.374398816130225, 6.4266180492251594, 6.477354421279655, 6.526670210880738, 6.574624257252709, 6.621272194449233, 6.666666666666667]),3)
    return (S,V)

@pytest.fixture
def bad_data():
    S = np.array([0.24390243902439024, 'bad', 'bad', 'bad', 'bad'])
    V = np.array([3,2,2,3,5])
    return (S,V)
@pytest.fixture
def nan_data():
    S = np.array([np.nan , 2.612244897959184, 4.224489795918368, 5.836734693877551, 7.448979591836735, 9.061224489795919, 10.673469387755102, 12.285714285714286, 13.89795918367347, 15.510204081632653, 17.122448979591837, 18.73469387755102, 20.346938775510203, 21.959183673469386, 23.571428571428573, 25.183673469387756, 26.79591836734694, 28.408163265306122, 30.020408163265305, 31.63265306122449, 33.244897959183675, 34.857142857142854, 36.46938775510204, 38.08163265306123, 39.69387755102041, 41.30612244897959, 42.91836734693877, 44.53061224489796, 46.142857142857146, 47.755102040816325, 49.36734693877551, 50.97959183673469, 52.59183673469388, 54.204081632653065, 55.816326530612244, 57.42857142857143, 59.04081632653061, 60.6530612244898, 62.26530612244898, 63.87755102040816, 65.48979591836735, 67.10204081632654, 68.71428571428571, 70.3265306122449, 71.93877551020408, 73.55102040816327, 75.16326530612245, 76.77551020408163, 78.38775510204081, 80.0])
    V = np.array([0.24390243902439024, np.nan, 0.95523765574527, 1.2733748886910061, 1.5698924731182797, 1.8469217970049918, 2.1063229963753525, 2.349726775956284, 2.578568723968194, 2.794117647058824, 2.9974991068238657, 3.1897150799166085, 3.371660466689212, 3.544137022397892, 3.707865168539326, 3.8634940513462745, 4.011610143599144, 4.1527446300715996, 4.2873797726610325, 4.415954415954417, 4.538868765672889, 4.65648854961832, 4.769148652255137, 4.877156299006796, 4.980793854033291, 5.080321285140562, 5.175978341127246, 5.267986479961372, 5.356550580431178, 5.441860465116279, 5.524092258506508, 5.603409600717811, 5.679964734405995, 5.7538994800693235, 5.825346112886049, 5.894428152492669, 5.961261075623327, 6.02595296025953, 6.088605068848534, 6.149312377210217, 6.208164054942929, 6.265243902439024, 6.320630749014454, 6.374398816130225, 6.4266180492251594, 6.477354421279655, 6.526670210880738, 6.574624257252709, 6.621272194449233, 6.666666666666667])
    return (S,V)
@pytest.fixture
def invalid_data():
    array1 = np.array(['apple', 'banana', 'cherry', None])
    array2 = np.array([None, 'dog', 'elephant', 'fish'])
    return (array1, array2)

def test_MMhandler():
    with pytest.raises(ValueError):
        MMhandler(invalid_data)
    with pytest.raises(ValueError, match="Input must be a tuple with two numpy arrays."):
        MMhandler(bad_data)
    with pytest.raises(ValueError, match="Input must be a tuple with two numpy arrays."):
        MMhandler((3,2,2,3,5))
def test_MMvelocity():
    with pytest.raises(ZeroDivisionError):
        MMvelocity(0,0,10)

def test_kcat():
    with pytest.raises(ZeroDivisionError):
        kcat(100,0)

def test_MMfitter(syndata):
    assert 39.9 <= MMfitter(syndata)[1][0] <= 40.1  # Vmax
    assert 9.9 <= MMfitter(syndata)[1][1] <= 10.1 # Km
    assert round(MMfitter(syndata)[4], 2)  == 0 # Should be approximated to zero
    assert MMfitter(syndata)[3] == True

def test_MMfitter(nan_data):
    assert 39.9 <= MMfitter(nan_data)[1][0] <= 40.1
    assert 9.9 <= MMfitter(nan_data)[1][1] <= 10.1
    assert round(MMfitter(nan_data)[4], 2) == 0
    assert MMfitter(nan_data)[3] == True

def test_LBfitter(syndata):
    assert 39.9 <= LBfitter(syndata)[1] <= 40.1
    assert 9.9 <= LBfitter(syndata)[2] <= 10.1
    assert round(LBfitter(syndata)[3], 2) == 0
    assert 9.9 <= LBfitter(syndata)[4][0] <= 10.1

def test_MMplot(syndata):
    fig = MMplot(syndata)
    assert len(fig.data) == 2
    trace = fig.data[0]
    assert trace['mode'] == 'markers'
    assert trace['name'] == 'Experimental'
    trace = fig.data[1]
    assert trace['mode'] == 'lines'
    assert trace['name'] == 'Fitted'

def test_LBplot(syndata):
    fig = LBplot(syndata)
    assert len(fig.data) == 2
    trace = fig.data[0]
    assert trace['mode'] == 'markers'
    assert trace['name'] == 'Experimental'
    trace = fig.data[1]
    assert trace['mode'] == 'lines'
    assert trace['name'] == 'Fitted'

def test_MMsimulator():
    simulated = MMsimulator(40,10)
    assert len(simulated) == 2
    trace = simulated[0].data[0]
    assert trace['mode'] == 'lines'
    trace = simulated[1].data[0]
    assert trace['mode'] == 'lines'
