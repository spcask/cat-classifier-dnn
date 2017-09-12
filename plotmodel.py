#!/usr/bin/env python

import json
import numpy as np
import matplotlib.pyplot as plt
import model


def plot(l, i, a):
    """Show the activations as a 64x64 plot.
   
    The activations in the i-th node of the l-th layer are plotted as an
    image.
    """
    # Arrange the activations into a 64x64 RGB matrix such that the
    # activation in a[i, j] represent the activations of R, G and B
    # components of the corresponding pixel (i, j) in the input image.
    a = np.array(a).reshape(64, 64, 3)

    # Normalize the activations.
    a_norm = (a - np.min(a)) / (np.max(a) - np.min(a))

    # Plot the activations.
    plt.imsave('plots/l{:d}a{:02d}.png'.format(l, i), a_norm)


if __name__ == '__main__':
    # Load the model parameters from JSON.
    with open('model.json') as f:
        j = json.load(f)

    # Convert the parameters to numpy arrays.
    params = [[np.array(w), np.array(b), g] for w, b, g in j]

    # params[0] = parameters of the first hidden layer.
    # params[0][0] = weights of the first hidden layer.
    # It's shape is (number of layer 1 units) x (number of input units).
    # Therefore x is an n x n identity matrix where n is the number of
    # input units.
    x = np.identity(params[0][0].shape[1])

    # For each input in x, compute activations of all units in the
    # neural network. Each input in x has exactly one input turned and
    # no two inputs are same by virtue of x being an identity matrix.
    # Therefore, cache contains the activations for each possible input
    # unit being turned on.
    a, cache = model.forward(params, x)

    # Extract all activations from the cache. The output 'a' from
    # forward propagation is the activation from the output layer.
    activations = [x for x, _ in cache[1:]] + [a]

    # For each layer in network ...
    for l, a in enumerate(activations, 1):
        # For each unit in layer ...
        for i, a_i in enumerate(a, 1):
            # Plot the activations of the unit.
            plot(l, i, a_i)
