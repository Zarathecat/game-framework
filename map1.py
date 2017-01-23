#!/usr/bin/env python

# Copyright 2017 Zara Zaimeche

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from maps import *
from sampleconf import *
from colours import *

map1 = Map()

# for own reference, there are currently 50 columns,
# 50 rows
# and a cell is 10 px in size.
# so the screen is 500 by 500.

# walls are areas which the player cannot cross. They are
# rects.

# When divided by CELLSIZE, all points must be ints, or graphics
# will not correspond to underlying map, and collisions will look
# weird.

leftmost = COLUMNS/ (CELLSIZE/2)
uppermost = ROWS/ (CELLSIZE/2)
wall_width = CELLSIZE
wall_vertical_length = (ROWS-CELLSIZE/2) * CELLSIZE
wall_horizontal_length = (COLUMNS-CELLSIZE/2) * CELLSIZE
rightmost = wall_horizontal_length
lowest = wall_vertical_length
gap_size = 4 * CELLSIZE

map1.walls = [(leftmost, uppermost, wall_width, wall_vertical_length),
          (leftmost, uppermost, wall_horizontal_length, wall_width),
          (rightmost, uppermost, wall_width, wall_vertical_length - gap_size),
          (leftmost, lowest, wall_horizontal_length- gap_size, wall_width)
         ]
""" The above is: [(5, 5, 10, 450), 
                   (5, 5, 450, 10),
                   (450, 5, 10, 410),
                   (5, 450, 410, 10)]
    To give the screen a nice border wall. """

def walls_to_rects((a, b, c, d)):
    a = a/10
    b = b/10
    c = c/10
    d = d/10
    return (a, b, c, d)

map1_rects = []

for wall in map1.walls:
    map1_rect = walls_to_rects(wall)
    map1_rects.append(map1_rect)

map1.rects = map1_rects

map1.colour = YELLOW
