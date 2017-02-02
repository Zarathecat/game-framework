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

# walls are areas which the player cannot cross. They are
# rects.

map2.rects = [(3, 3, 1, (ROWS-CELLSIZE/2)),
          (5, 3, (COLUMNS-CELLSIZE/2), 1),
          (COLUMNS, 5, 1, (ROWS-CELLSIZE)),
          (1, 5, 4, 1)
         ]

left_door_rect = (0, (ROWS/2), 1, 3)

map2_walls = []

for rect in map2.rects:
    map2_wall = map2.rects_to_walls(rect, CELLSIZE)
    map2_walls.append(map2_wall)

map2.walls = map2_walls

map2.colour = DARKGREY

left_door_drawn = map2.rects_to_walls(left_door_rect, CELLSIZE)
map2.left_door = {'rect': left_door_rect, 'drawn': left_door_drawn,
                  'dest_map': 'map1'}

map2.characters = [dude]
