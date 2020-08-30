import cv2
import numpy as np
from os.path import splitext, isfile


def connect_dots(in_path, out_path=None, color=(255, 255, 255), thickness=1, return_array=False):
    """
    Function to detect blue, green and red dots in the provided image, and connects
    with a simple line. This implementation assumes square or spherical shapes of
    the colored dots, a black background, and a single dot per color.

    :param in_path: path to the input image
    :param out_path: path to the output image. If None,
    :param color: color of the line in BGR
    :param thickness: line thickness
    :param return_array: Boolean to specify if the output needs to be returned as an
    array. For testing purposes.

    :return Returns None or an (_ ,_ , 3) numpy array of the output if return_array=True
    """

    assert (isfile(in_path)), "Input file does not exist"

    # Load image as BGR image array
    im = cv2.imread(in_path, 1)

    # Extract the dot coordinates
    dot_cords = []
    for i in range(3):
        # Extract image channel
        color_channel = im[:, :, i].copy()
        pixels = np.argwhere(color_channel > 0)

        assert (len(pixels) > 0), "Input image contains an empty image channel"

        # Find the center of the region
        color_xy = np.mean(np.argwhere(color_channel > 0), axis=0).astype('int')
        # Store in coordinate array
        dot_cords.append(color_xy)

    # Draw the lines connecting the dots
    cv2.line(im, tuple(np.flip(dot_cords[0])), tuple(np.flip(dot_cords[1])), color, thickness)
    cv2.line(im, tuple(np.flip(dot_cords[1])), tuple(np.flip(dot_cords[2])), color, thickness)
    cv2.line(im, tuple(np.flip(dot_cords[2])), tuple(np.flip(dot_cords[0])), color, thickness)

    if return_array:
        return im

    # Construct out_path is none is provided
    if out_path is None:
        (root, ext) = splitext(in_path)
        out_path = "".join([root + "_connected", ext])

    # Write the output image to file
    cv2.imwrite(out_path, im)

    return None
