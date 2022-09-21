# CS231A Homework 0, Problem 4
import numpy as np
import matplotlib.pyplot as plt
from skimage import io


def part_a():
    # ===== Problem 4a =====
    # Read in image1 as a grayscale image. Take the singular value
    # decomposition of the image.
    # Hint: use io.imread to read in the image file

    img1 = None

    # BEGIN YOUR CODE HERE

    # END YOUR CODE HERE
    return u, s, v

def part_b(u, s, v):
    # ===== Problem 4b =====
    # Save and display the best rank 1 approximation 
    # of the (grayscale) image1.

    rank1approx = None

    # BEGIN YOUR CODE HERE

    # END YOUR CODE HERE
    return rank1approx

def part_c(u, s, v):
    # ===== Problem 4c =====
    # Save and display the best rank 20 approximation
    # of the (grayscale) image1.

    rank20approx = None

    # BEGIN YOUR CODE HERE

    # END YOUR CODE HERE
    return rank20approx


if __name__ == '__main__':
    u, s, v = part_a()
    rank1approx = part_b(u, s, v)
    rank20approx = part_c(u, s, v)
