import unittest
import cv2
import numpy as np
from connectdots import connect_dots
from os import remove


class TestDots(unittest.TestCase):

    def test_simple_triangle(self):
        # Set up Canvas
        input_image = np.zeros((100, 100, 3))
        # Color pixels at the corners
        input_image[0, 0, 0] = 255
        input_image[input_image.shape[0] - 1, 0, 1] = 255
        input_image[0, input_image.shape[0] - 1, 2] = 255
        input_image.astype('uint8')

        color = (255, 255, 255)
        thickness = 1

        # Construct expected output
        output_expected = cv2.line(input_image.copy(), (0, 0), (0, input_image.shape[0]),
                                   color, thickness)
        output_expected = cv2.line(output_expected, (0, 0), (input_image.shape[0], 0),
                                   color, thickness)
        output_expected = cv2.line(output_expected, (input_image.shape[0] - 1, 0), (0, input_image.shape[0] - 1),
                                   color, thickness)

        # Save test input image and generate output
        cv2.imwrite('test_img.png', input_image)
        output = connect_dots('test_img.png', return_array=True)

        # Remove test image
        remove('test_img.png')

        self.assertTrue((output == output_expected).all())


if __name__ == '__main__':
    unittest.main()
