# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:55:01 2023

@author: chucker1
"""

import unittest
from src.patch_indices.patch_indices import PatchGenerator

class PatchGeneratorTestCase(unittest.TestCase):
    def test_block_generation(self):
        patch_generator = PatchGenerator(100, 80, 10, 20, y_overlap=2, x_overlap=3)

        expected_patches = [
            (0, 0, 10, 20),   # First block
            (0, 17, 10, 20),  # Second block with overlap
            (0, 34, 10, 20),  # Third block with overlap
            (0, 51, 10, 20)  # Fourth block with overlap and adjusted size
        ]

        generated_patches = list(patch_generator)[:4]

        self.assertEqual(len(generated_patches), len(expected_patches))

        for expected, generated in zip(expected_patches, generated_patches):
            self.assertEqual(expected, generated)

if __name__ == '__main__':
    unittest.main()
    
