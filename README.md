# `patchgenerator`

The `patchgenerator` is a simple tool to generate array indices, with or without overlap, to create numpy array patches. Only requires python.

# Example usage:

```
from patch_indices.patch_indices import PatchGenerator

patch_generator = PatchGenerator(100, 80, 10, 20, y_overlap=2, x_overlap=3)
for patch in patch_generator:
    row_start, cols_start, row_end, cols_end = patch
    print("row_start, cols_start, row_end, cols_end", row_start, cols_start, row_end, cols_end)
```
```
import numpy as np
from patch_indices.patch_indices import PatchGenerator

np_array = np.ones((100, 80, 3), dtype=np.uint8)
y_size, x_size, z_size = np_array.shape
patch_size_y = 10
patch_size_x = 20

patch_generator = PatchGenerator(y_size, x_size, patch_size_y, patch_size_x, y_overlap=2, x_overlap=3)
for patch in patch_generator:
    row_start, cols_start, row_end, cols_end = patch
    print("row_start, cols_start, row_end, cols_end", row_start, cols_start, row_end, cols_end)
    print(np_array[row_start:row_start + row_end, cols_start:cols_start + cols_end, :].shape)
```