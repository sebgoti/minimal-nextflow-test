#!/usr/bin/env python3

from skimage.filters import gaussian, median
from skimage.io import imread, imsave
import numpy as np
import os
import argparse

def main(args):
    # Read image:
    img = imread(args.input)
    # Parse gaussian kernel values:
    sigmas = [float(s) for s in args.sigma.split(",")]
    
    if args.filter == 'gaussian':
        blurred_img = gaussian(img, sigma=sigmas)
    else:
        blurred_img = median(img)
        
    imsave(args.output + '.tiff', blurred_img)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blur a tiff image')
    
    parser.add_argument('-i', '--input', type=str, required=True, \
                        help='Path to TIFF image')
    parser.add_argument('-o', '--output', type=str, required=True, \
                        help='Path to write image')
    parser.add_argument('-s', '--sigma', type=str, required=True, \
                        help='Sigmae for blurring in Gaussian filter')
    parser.add_argument('-f', '--filter', type=str, default='gaussian')
    
    args = parser.parse_args()
    main(args)