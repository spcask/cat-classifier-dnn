#!/usr/bin/env python3
import os
import json
import numpy as np
import matplotlib.pyplot as plt


def relu(z):
    """Compute max(0, z).
    
    Arguments:
      z (numpy.ndarray): A matrix of real numbers.

    Returns:
      numpy.ndarray: A matrix of real numbers such that for every
      element z_i in z, every corresponding element y_i in the returned
      matrix is y_i = max(0, z_i).
    """
    return np.maximum(0, z)


def sigmoid(z):
    """Compute 1 / (1 + e^(-z)).
    
    Arguments:
      z (numpy.ndarray): A matrix of real numbers.

    Returns:
      numpy.ndarray: A matrix of real numbers such that for every
      element z_i in z, every corresponding element y_i in the returned
      matrix is y_i = 1 / (1 + e^(-z_i)).
    """
    return 1 / (1 + np.exp(-z))


def relu_derivative(z):
    """Compute the derivative of relu(z).
    
    Arguments:
      z (numpy.ndarray): A matrix of real numbers.

    Returns:
      numpy.ndarray: A matrix of real numbers such that for every
      element z_i in z, every corresponding element y_i in the returned
      matrix is y_i = d(relu(z_i))/dz_i.
    """
    dz = np.zeros(z.shape)
    dz[z > 0] = 1
    return dz


def sigmoid_derivative(z):
    """Compute the derivative of relu(z).
    
    Arguments:
      z (numpy.ndarray): A matrix of real numbers.

    Returns:
      numpy.ndarray: A matrix of real numbers such that for every
      element z_i in z, every corresponding element y_i in the returned
      matrix is y_i = d(sigmoid(z_i))/dz_i.
    """
    s = sigmoid(z)
    return s * (1 - s)


def g(activation):
    """Return the specified activation function.

    Arguments:
      activation (str): Name of the activation function, e.g. "relu".

    Returns:
      function: Activation function.
    """
    return {
        'relu': relu,
        'sigmoid': sigmoid,
    }[activation]


def g_derivative(activation):
    """Return the derivative function of the specified activation.

    Arguments:
      activation (str): Name of the activation function, e.g. "relu".

    Returns:
      function: Derivative of activation function.
    """
    return {
        'relu': relu_derivative,
        'sigmoid': sigmoid_derivative,
    }[activation]


def read_set(dirname):
    """Read image data in specified directory into matrices.

    This function returns a tuple of two numpy arrays.
    
    The first array is a n * m, where n = w * h * 3 and m is the number
    of image samples, where w and h are the width and height,
    respectively, of each image. The factor 3 is due to R, G and B
    values of each pixel kept separately in the matrix. Each column in
    the first numpy array is a column vector containing w * h * 3
    inputs. Each R, G and B values is a real number between 0 and 1.
    
    The second array is a 1 * m matrix of labels. Each value in this
    matrix is either 1 or 0. The value 1 represents that the
    corresponding input sample is a cat and the value 0 represents that
    the input is not a cat.

    Arguments:
      dirname (str): Directory from which image files are to be read.

    Returns:
      tuple: (numpy.ndarray, numpy.ndarray): A tuple of image samples
        and image labels.
    """
    images = []
    labels = []

    # Iterate over each image in the specified directory.
    for filename in os.listdir(dirname):

        # Read RGBA channels from image file.
        img = plt.imread(os.path.join(dirname, filename))

        # Ignore the alpha channel.
        img = img[:,:,:3]

        # Add the image and label to our data set.
        images.append(img)
        labels.append(1 if 'cat' in filename else 0)

    # Convert the image samples to a 4D matrix.
    images = np.array(images)

    # Convert the 4D matrix to a 2D matrix where each column is a vector
    # containing all the RGB values in the image flattened out into a
    # column vector.
    x = images.reshape(images.shape[0], -1).T

    # Convert the labels into a 1 x m matrix.
    y = np.array(labels)

    return x, y


def init_params(units, activations):
    """Initialize parameters of the model.
    
    Arguments:
      units (list): Each item in the list is the number of units
        in the layer. units[0] is the number of input units and
        units[len(units) - 1] is the number of output units.
      activations (list): Each item in the list is a string that denotes
        the activation function name used in the units in each layer.
        activations[0] is the activation function name for the 1st
        hidden layer.

    Returns:
      list: List of parameters of the model. Each item in the list is a
        tuple of the form (w, b, activation) where w is the
        weight-matrix of a layer, b is the bias-matrix of a layer and
        activation is the activation function name of a layer.
    """
    params = []

    for l in range(1, len(units)):
        w = np.random.randn(units[l], units[l - 1]) / np.sqrt(units[l-1])
        b = np.zeros((units[l], 1))
        activation = activations[l - 1]
        params.append([w, b, activation])

    return params


def forward(params, x):
    """Perform forward propagation in the neural-network.
    
    Arguments:
      params (list): Parameter list of the model.
      x (numpy.ndarray): Input matrix.

    Returns:
      cache (list): Each item in the cache is a tuple of the form (z, a)
        where z is the weighted sum of inputs arriving in a layer and a
        is the activation value of the layer. This cache is used by
        backward() function to compute its derivatives.
    """
    cache = []

    a = x
    cache.append((None, x))

    for (w, b, activation) in params:
        z = np.dot(w, a) + b
        a = g(activation)(z)
        cache.append((z, a))

    return a, cache


def backward(params, y, cache):
    """Perform backward propagation in the neural-network.

    Arguments:
      params (list): Parameter list of the model.
      cache (list): Cache returned by forward() function.
      x (numpy.ndarray): Labelled output matrix.
    """
    # Learning rate.
    alpha = 0.005

    # Number of training samples.
    m = y.shape[1]

    # Activation output from the last layer.
    _, a = cache[-1]

    # dL/da of the last year, where L is the loss function.
    da = (- y / a + (1 - y) / (1 - a))

    # For every layer starting with the output layer and going upto the
    # first hidden layer, update the weights and biases according to the
    # backpropagation algorithm.
    #
    # In each iteration, params, z and a are the parameters, weighted
    # sum of inputs and activataion of the current layer. z_ and a_ are
    # the weighted sum of inputs and activation of the previous layer.
    for params, (z, a), (z_, a_) in zip(reversed(params),
                                        reversed(cache[1:]),
                                        reversed(cache[:-1])):
        w, b, activation = params

        dz = da * g_derivative(activation)(z)
        dw = np.dot(dz, a_.T) / m
        db = np.sum(dz, axis=1, keepdims=True) / m

        params[0] = w - alpha * dw
        params[1] = b - alpha * db

        da = np.dot(w.T, dz)


def train(x, y):
    """Train a model on the specified training samples and labels.

    Arguments:
      x (numpy.ndarray): Training input samples, an n * m matrix where n
        is the number of inputs in each training sample and m is the
        number of training samples.
      y (numpy.ndarray): Training input labels, a vector with m labels.

    Returns:
      list: Model parameters. 
    """
    # Training iterations.
    iterations = 1700

    units = [x.shape[0], 10, 10, 10, 1]
    activations = ['relu'] * (len(units) - 2) + ['sigmoid']

    # Get a new randomly initialized params.
    np.random.seed(1)
    params = init_params(units, activations)

    # Determine number of training samples.
    m = x.shape[1]

    for i in range(iterations):
        # Forward propagation.
        a, cache = forward(params, x)

        # Compute cost.
        c = np.sum(- y * np.log(a) - (1 - y) * np.log(1 - a)) / m

        y = y.reshape(a.shape)
        backward(params, y, cache)

        if ((i + 1) % 100 == 0):
            print('iteration: {} of {}; cost: {:.6f}'.format(i + 1, iterations, c))

    return params


def classify(params, x):
    """Classify input samples in x with the specified model parameters.

    Arguments:
      params (list): Model parameters.
      x (numpy.ndarray): Inputs, an n * m matrix where n is the number
        of input units in each input sample and m is the number of
        input samples.

    Returns:
      numpy.ndarray: A 1 * m matrix where m is the number of input
        samples. The returned array contains output labels for each
        input sample as predicted by the params.
    """
    m = x.shape[1]
    y = np.zeros((1, m))
    a, _ = forward(params, x)
    for i in range(m):
        y[0, i] = 0 if a[0, i] <= 0.5 else 1
    return y


def test(params, train_x, train_y, test_x, test_y):
    """Test the trained parameters with training set and test set."""
    train_y_result = classify(params, train_x)
    test_y_result = classify(params, test_x)
    train_accuracy = 1 - np.mean(np.abs(train_y_result - train_y))
    test_accuracy = 1 - np.mean(np.abs(test_y_result - test_y))

    print('train accuracy: {:.2f}%'.format(100 * train_accuracy))
    print('test accuracy:  {:.2f}%'.format(100 * test_accuracy))

    if train_accuracy - test_accuracy > 0.02:
        print('warning: params is overfitting training set')


if __name__ == '__main__':
    # Read training data into matrices x and y where x contains the
    # training input samples and y contains the training labels.
    train_x, train_y = read_set('train-set')
    test_x, test_y = read_set('test-set')

    # Train the params.
    params = train(train_x, train_y)

    # Test the params.
    test(params, train_x, train_y, test_x, test_y)

    # Write params to a file.
    params = [[w.tolist(), b.tolist(), g] for w, b, g in params]
    with open('model.json', 'w') as f:
        json.dump(params, f, indent=2)

    print('written model to model.json')
