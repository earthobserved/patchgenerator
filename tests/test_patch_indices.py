# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:55:01 2023

@author: chucker1
"""

import unittest
import sys # added!
sys.path.append("..") # added!
from src.patch_indices.patch_indices import PatchGenerator

    
class TestArrayPatchGenerator(unittest.TestCase):
    def test_patch_generation(self):
        ysize = 1024
        xsize = 1024
        y_block_size = 512
        x_block_size = 512
        y_overlap = 100
        x_overlap = 100

        generator = PatchGenerator(ysize, xsize, y_block_size, x_block_size, y_overlap, x_overlap)
        
        expected_patches = [
            (0, 0, 512, 512), # First block
            (412, 0, 512, 512), # Second block with overlap
            (824, 0, 200, 512), # Third block with overlap
            (0, 412, 512, 512) # Fourth block with overlap
        ]

        patches = list(generator)[:4]

        self.assertEqual(patches, expected_patches)

    def test_invalid_arguments(self):
        # Test invalid block size and overlap
        with self.assertRaises(ValueError):
            PatchGenerator(10, 10, 0, 4)

        with self.assertRaises(ValueError):
            PatchGenerator(10, 10, 4, 0)

        with self.assertRaises(ValueError):
            PatchGenerator(10, 10, 4, 5, y_overlap=5)

        with self.assertRaises(ValueError):
            PatchGenerator(10, 10, 4, 5, x_overlap=6)

        # Test block size larger than array size
        with self.assertRaises(ValueError):
            PatchGenerator(10, 10, 12, 5)

        with self.assertRaises(ValueError):
            PatchGenerator(10, 10, 5, 12)

    def test_empty_array(self):
        # Test empty array case
        with self.assertRaises(ValueError):
            PatchGenerator(0, 0, 3, 3)

    def test_single_patch(self):
        # Test case where the array size is equal to the block size
        ysize = 4
        xsize = 4
        y_block_size = 4
        x_block_size = 4

        generator = PatchGenerator(ysize, xsize, y_block_size, x_block_size)
        patches = list(generator)
        expected_patches = [(0, 0, 4, 4)]
        self.assertEqual(patches, expected_patches)

        
        
if __name__ == '__main__':
    unittest.main()
