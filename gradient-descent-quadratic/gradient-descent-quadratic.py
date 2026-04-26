def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    vot = [a, b, c, x0, lr, steps]
    x = float(x0)
    # Write 
    for _ in range(steps):
        fx = 2 * a * x + b

        x = x - lr*fx

    return float(x)
    pass