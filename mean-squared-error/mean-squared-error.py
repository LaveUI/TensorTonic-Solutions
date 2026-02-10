import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    x = np.array(y_pred, dtype=float)
    y = np.array(y_true, dtype=float)
    mse = np.mean(np.square(x-y))
    return mse
    pass
