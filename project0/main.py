import numpy as np

def randomization(n):
    """
    Arg:
      n (int): an integer
    Returns:
      A (np.ndarray): a randomly-generated nx1 Numpy array.
    """
    #Your code here
    A = np.random.rand(n, 1)
    return A

def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    
    Arg:
      h (int) : an integer describing the height of A and B
      w (int) : an integer describing the width of A and B
    Returns (in this order):
      A (np.ndarray) : a randomly-generated h x w Numpy array.
      B (np.ndarray) : a randomly-generated h x w Numpy array.
      s (np.ndarray) : the sum of A and B.
    """
    #Your code here
    A = np.random.rand(h, w)
    B = np.random.rand(h, w)
    s = A + B
    return A, B, s


def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A (np.ndarray) : a Numpy column array of shape (n, 1)
      B (np.ndarray) : a Numpy column array of shape (n, 1)
    Returns:
      s (float) : the L2 norm of A+B.
    """
    #Your code here
    s = np.linalg.norm(A + B)
    return s


def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    #Your code here
    out = np.tanh(np.dot(weights.T, inputs))
    return out

def scalar_function(x, y):
    """
    Returns the f(x,y) defined in the problem statement.
    """
    #Your code here
    if x <= y:
        return x*y
    else:
        return x/y

def vector_function(x, y):
    """
    Make sure vector_function can deal with vector input x,y 
    """
    #Your code here
    raise NotImplementedError


if __name__ == "__main__":
    print(randomization(5))
