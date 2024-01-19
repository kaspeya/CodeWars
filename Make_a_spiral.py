""" Your task, is to create a NxN spiral with a given size."""

import numpy as np


def spiralize(n):
    moving_mode = 0  # 0 - слева направо, 1 - сверху вниз, 2 - справа налево, 3 - снизу вверх
    moving_patterns = np.array([(1, 0), (0, 1), (-1, 0), (0, -1)])
    corner_point = np.array([0, 0])
    old_corner_point = np.array([0, 0])
    
    arr = np.insert(np.array([np.arange(n, 2, -2)] * 2).flatten('F'), 0, n)
    
    if n % 2 == 0:
        arr = np.append(arr, 2)
    
    image = np.zeros([n, n], dtype=int)
    
    for side in arr:
        old_corner_point = corner_point
        corner_point = corner_point + moving_patterns[moving_mode] * (side - 1)
        moving_mode = (moving_mode + 1) % len(moving_patterns)
        
        if old_corner_point[0] == corner_point[0]:
            max_v = max(old_corner_point[1], corner_point[1]) + 1
            min_v = min(old_corner_point[1], corner_point[1])
            image[min_v:max_v, corner_point[0]] = 1
        else:
            max_v = max(old_corner_point[0], corner_point[0]) + 1
            min_v = min(old_corner_point[0], corner_point[0])
            image[corner_point[1], min_v:max_v] = 1
    
    return image.tolist()
