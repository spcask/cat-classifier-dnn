#!/usr/bin/env python3
import os
import h5py
import numpy as np
import matplotlib.pyplot as plt


def write_imgs(data_type):
    """Convert data in HDF5 file to image files.

    data_type (str): Either "train" or "test".
    """
    dirname = '{}-set'.format(data_type)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    data = h5py.File('h5data/{}_catvnoncat.h5'.format(data_type))
    x = np.array(data['{}_set_x'.format(data_type)][:])
    y = np.array(data['{}_set_y'.format(data_type)][:])
    for i, (x_i, y_i) in enumerate(zip(x, y)):
        label = 'cat' if y_i == 1 else 'not'
        filename = '{}/{:03d}-{}.png'.format(dirname, i, label)
        print('Writing {} image {} to {} ...'
              .format(data_type, i, filename))
        plt.imsave(filename, x_i)


def verify_imgs(data_type):
    """Read the data in image files and compare with data in HDF5 file.

    data_type (str): Either "train" or "test".
    """
    dirname = '{}-set'.format(data_type)

    data = h5py.File('h5data/{}_catvnoncat.h5'.format(data_type))
    x = np.array(data['{}_set_x'.format(data_type)][:])

    for i, filename in enumerate(sorted(os.listdir(dirname))):
        img = plt.imread(dirname + '/' + filename)
        img = img[:,:,:3]
        rgb = (255 * img).astype(np.uint8)
        if not np.array_equal(x[i], rgb):
            print('{}/{} does not match image in HDF5 file'.format(
                  dirname, filename))
    print('Verified {} files.'.format(data_type))


if __name__ == '__main__':
    write_imgs('train')
    write_imgs('test')
    verify_imgs('train')
    verify_imgs('test')
