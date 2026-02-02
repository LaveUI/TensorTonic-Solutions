import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.

    """

    # Write code here
    z = np.asarray(x, dtype=float)
    return (1 / (1 + np.exp(-z)))
    pass

    #np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))