#!/usr/bin/env python3
import os
import json
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    """Compute 1 / (1 + e^(-x)).
    
    Arguments:
      x (numpy.ndarray): A matrix of real numbers.

    Returns:
      numpy.ndarray: A matrix of real numbers such that for every
      element x_i in x, every corresponding element y_i in the returned
      matrix is y_i = 1 / (1 + e^(-x_i)).
    """
    return 1 / (1 + np.exp(-x))


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


def train(x, y):
    """Train a model on the specified training samples and labels.

    Arguments:
      x (numpy.ndarray): Training input samples, an n * m matrix where n
        is the number of inputs in each training sample and m is the
        number of training samples.
      y (numpy.ndarray): Training input labels, a vector with m labels.

    Returns:
      tuple: (numpy.ndarray, numpy.float64): A tuple of trained model
        weights and model bias. The weights array is an n * 1 matrix.
        The bias is a real number.
    """
    # Training iterations.
    count = 250

    # Learning rate.
    alpha = 0.0056

    # Initialize weights and bias.
    w = np.zeros((x.shape[0], 1))
    b = 0

    # Determine number of training samples.
    m = x.shape[1]

    for i in range(count):
        # Compute activation of the neuron for each training sample.
        # The result is a (1 * n) matrix where n is the number of inputs
        # in each training sample.
        a = sigmoid(np.dot(w.T, x) + b)

        # Compute cost.
        c = np.sum(-(y * np.log(a) + (1 - y) * np.log(1 - a))) / m
        if (i % 10 == 0):
            print('iteration: {} of {}; cost: {:.4f}'.format(i, count - 1, c))

        # Reduce cost by descending the gradient of cost function.
        dw = np.dot(x, (a - y).T) / m
        db = np.sum((a - y)) / m

        # Descend the gradient to approach optimal w and b.
        w = w - alpha * dw
        b = b - alpha * db

    # Return the model.
    return w, b


def classify(w, b, x):
    """Classify input samples in x with the model (w, b).
    
    Arguments:
      w (numpy.ndarray): Training weights, an n * 1 matrix.
      b (numpy.float64): Training bias, a real number.

    Returns:
      numpy.ndarray: A 1 * m matrix where m is the number of input
        samples. The returned array contains output labels for each
        input sample as predicted by the model.
    """
    m = x.shape[1]
    y = np.zeros((1, m))
    a = sigmoid(np.dot(w.T, x) + b)
    for i in range(a.shape[1]):
        y[0, i] = 0 if a[0, i] <= 0.5 else 1
    return y


def test():
    """Train a model on training set and test it with test set.
    
    After the training and testing is done, the learned model is written
    to a file named model.json.
    """
    # Read training data into matrices x and y where x contains the
    # training input samples and y contains the training labels.
    train_x, train_y = read_set('train-set')
    test_x, test_y = read_set('test-set')

    w, b = train(train_x, train_y)

    train_y_result = classify(w, b, train_x)
    test_y_result = classify(w, b, test_x)

    train_accuracy = 1 - np.mean(np.abs(train_y_result - train_y))
    test_accuracy = 1 - np.mean(np.abs(test_y_result - test_y))

    print('train accuracy: {:.2f}%'.format(100 * train_accuracy))
    print('test accuracy:  {:.2f}%'.format(100 * test_accuracy))
    if train_accuracy - test_accuracy > 0.02:
        print('warning: model is overfitting training set')

    model = {
        'w': w.tolist(),
        'b': b.tolist()
    }

    with open('model.json', 'w') as f:
        json.dump(model, f, indent=2)
    print('written model to model.json')


if __name__ == '__main__':
    test()
