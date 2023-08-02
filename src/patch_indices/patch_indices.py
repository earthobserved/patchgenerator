# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:26:03 2023

@author: chucker1
"""

class PatchGenerator:
    """
    PatchGenerator class generates patches of specified size within given dimensions with optional overlap.

    Args:
        
        ysize (int): Total size along the y-axis (rows).
        xsize (int): Total size along the x-axis (columns).
        y_patch_size (int): Patch size along the y-axis (rows).
        x_patch_size (int): Patch size along the x-axis (columns).
        y_overlap (int, optional): Overlap size in the y-axis (rows). Defaults to 0.
        x_overlap (int, optional): Overlap size in the x-axis (columns). Defaults to 0.
        
    
    Raises:
        ValueError: If x_patch_size is larger than xsize or y_patch_size is larger than ysize.
    """
    def __init__(self, ysize, xsize, y_patch_size, x_patch_size, y_overlap=0, x_overlap=0):
        # assert ysize > 0 and xsize > 0, "Array size must be positive."
        # assert y_patch_size > 0 and x_patch_size > 0, "Patch size must be positive."
        # assert y_overlap >= 0 and x_overlap >= 0, "Overlap must be non-negative."

        # assert y_patch_size <= ysize, "Patch size along y-axis cannot exceed array size."
        # assert x_patch_size <= xsize, "Patch size along x-axis cannot exceed array size."
        # assert y_overlap <= y_patch_size, "Overlap along y-axis cannot exceed Patch size."
        # assert x_overlap <= x_patch_size, "Overlap along x-axis cannot exceed Patch size."
        
        if ysize <= 0 or xsize <= 0:
            raise ValueError("Array size must be positive.")
        if y_patch_size <= 0 or x_patch_size <= 0:
            raise ValueError("Patch size must be positive.")
        if y_overlap < 0 or x_overlap < 0:
            raise ValueError("Overlap must be non-negative.")
        if y_patch_size > ysize:
            raise ValueError("Patch size along y-axis cannot exceed array size.")
        if x_patch_size > xsize:
            raise ValueError("Patch size along x-axis cannot exceed array size.")
        if y_overlap > y_patch_size:
            raise ValueError("Overlap along y-axis cannot exceed Patch size.")
        if x_overlap > x_patch_size:
            raise ValueError("Overlap along x-axis cannot exceed Patch size.")

            
        self.ysize = ysize
        self.xsize = xsize
        self.y_patch_size = y_patch_size
        self.x_patch_size = x_patch_size
        self.y_overlap = y_overlap
        self.x_overlap = x_overlap
        self.i = 0
        self.j = 0


    def __iter__(self):
        """
        Returns the iterator object.

        Returns:
            PatchGenerator: Iterator object.
        """
        return self


    def __next__(self):
        """
        Generates the next patch.

        Returns:
            tuple: A tuple containing the starting row index (i), starting column index (j),
            number of rows (rows), and number of columns (cols) for the next patch.

        Raises:
            StopIteration: When all patches have been generated.
        """
        if self.i >= self.ysize:
            # print("self.i >= self.ysize", self.i, self.ysize)
            raise StopIteration
        if self.j >= self.xsize:
            # print("self.j >= self.xsize", self.j, self.xsize)
            raise StopIteration

        i = self.i
        j = self.j

        if self.i + self.y_patch_size - self.y_overlap < self.ysize:
            rows = self.y_patch_size
        else:
            rows = self.ysize - self.i

        if self.j + self.x_patch_size - self.x_overlap < self.xsize:
            cols = self.x_patch_size
        else:
            cols = self.xsize - self.j

        self.i += self.y_patch_size - self.y_overlap
        if self.i >= self.ysize:
            self.i = 0
            self.j += self.x_patch_size - self.x_overlap

        return i, j, rows, cols


if __name__ == "__main__":
    import numpy as np
    ysize = 1024
    xsize = 1024
    y_block_size = 512
    x_block_size = 512
    y_overlap = 100
    x_overlap = 100
        
    arr = np.ones((ysize, xsize), dtype=np.uint8)
    print(np.unique(arr, return_counts=True))
    
    patch_generator = PatchGenerator(ysize, xsize, y_block_size, x_block_size, y_overlap=y_overlap, x_overlap=x_overlap)
    for i, j, rows, cols in patch_generator:
        print(f"Clip array patch: i={i}, j={j}, rows={rows}, cols={cols}")
        # print(f"{i}, {j}, {rows}, {cols}")
        print(arr[i:i+rows, j:j+cols].shape)
        arr[i:i+rows, j:j+cols] = 255
        
    print(np.unique(arr, return_counts=True))
        