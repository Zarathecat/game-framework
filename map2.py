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
from charas import *

map2 = Map()

# This is a test alternate map, to show how the
# map generator interacts with the main event loop.
# for own reference, there are currently 50 columns,
# 50 rows
# and a cell is 10 px in size.
# so the screen is 500 by 500.
# map.wall coordinate/cellsize needs to be an int.

# walls are areas which the player cannot cross. They are
# rects.

map2.walls = [(30, 30, CELLSIZE, (ROWS-CELLSIZE/2) * CELLSIZE),
          (COLUMNS, 30, (COLUMNS-CELLSIZE/2) * CELLSIZE, CELLSIZE),
          (COLUMNS * CELLSIZE, ROWS, CELLSIZE, (ROWS-CELLSIZE) * CELLSIZE),
          (COLUMNS/5, ROWS, (COLUMNS-CELLSIZE), CELLSIZE)
         ]

left_drawn_door = (0, (ROWS/2) * CELLSIZE, 10, 30)

def walls_to_rects((a, b, c, d)):
    a = a/10
    b = b/10
    c = c/10
    d = d/10
    return (a, b, c, d)

map2_rects = []

for wall in map2.walls:
    map2_rect = walls_to_rects(wall)
    map2_rects.append(map2_rect)

map2.rects = map2_rects

map2.colour = DARKGREY

door_rect = walls_to_rects(left_drawn_door)
map2.left_door = {'rect': door_rect, 'drawn': left_drawn_door,
                  'dest_map': 'map1'}

map2.characters = [dude]
