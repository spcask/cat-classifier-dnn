#!/usr/bin/env python3

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import model


def classify_images(dirname, verbose=False):
    """Classify all images in a given directory.

    The directory must contain 64x64 PNG images only.

    Arguments:
      dirname (str): Directory containing images to be classified.
    """
    images = []
    filenames = []
    for filename in os.listdir(dirname):
        # Add the file path to the list of filenames.
        filename = os.path.join(dirname, filename)
        filenames.append(filename)

        # Read RGBA channels from image file.
        img = plt.imread(filename)

        # Ignore the alpha channel (the A channel).
        img = img[:,:,:3]

        # Add the image to our data set.
        images.append(img)

    # Convert the image samples to a 4D matrix.
    images = np.array(images)

    # Convert the 4D matrix to a 2D matrix where each column is a vector
    # containing all the RGB values in the image flattened out into a
    # column vector.
    x = images.reshape(images.shape[0], -1).T

    # Load the model parameters from JSON.
    with open('model.json') as f:
        j = json.load(f)

    # Convert the parameters to numpy arrays.
    params = [[np.array(w), np.array(b), g] for w, b, g in j]

    # Classify the given set of inputs.
    y = model.classify(params, x)

    # Print the classification results.
    results = []
    for filename, output in zip(filenames, y[0]):
        result = 'cat' if output == 1 else 'not'
        results.append((filename, result))
        if verbose:
            print(filename + ':', result)

    return results


if __name__ == '__main__':
    if len(sys.argv) == 1:
        dirname = 'extra-set'
    elif len(sys.argv) == 2:
        dirname = sys.argv[1]
    else:
        print('Usage: {} [DIR]'.format(sys.argv[0]))
        sys.exit(1)

    classify_images(dirname, verbose=True)
