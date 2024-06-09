import pygame, numpy
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np

def test():
    noise = PerlinNoise(octaves=2, seed=1)
    xpix, ypix = 20, 20
    pic = [[noise([i / xpix, j / ypix]) for j in range(xpix)] for i in range(ypix)]
    plt.imshow(pic, cmap='gray')
    plt.colorbar
    plt.show()

def test2():
    xpix = 100  # example value
    ypix = 100  # example value

    # Initialize an empty list to hold the picture data
    pic = []

    # Iterate over each row
    noise = PerlinNoise(octaves=3, seed=2)
    for i in range(ypix):
        row = []
        # Iterate over each column within the current row
        for j in range(xpix):
            # Calculate the noise value for the current pixel
            noise_value = noise([i / xpix, j / ypix])
            # Append the noise value to the current row
            row.append(noise_value)
        # Append the completed row to the picture
        pic.append(row)
    plt.imshow(pic, cmap='gray')
    plt.show()

def test3():
    xpix = 100  # example value
    ypix = 100  # example value

    # Initialize an empty list to hold the picture data
    pic = np.zeros((xpix, ypix))

    # Iterate over each row
    noise = PerlinNoise(octaves=3, seed=2)
    for i in range(ypix):
        for j in range(xpix):
            pic[i][j] = noise([i / xpix, j / ypix])
    plt.imshow(pic, cmap='gray')
    plt.show()

def test5():
    array1 = np.array([1, 2])
    array2 = np.array([2, 3])

def main():
    test3()
    pass


if __name__ == "__main__":
    main()