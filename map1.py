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
from charas import *  # should be restructured so these aren't imported.

map1 = Map()

# for own reference, there are currently 50 columns,
# 50 rows
# and a cell is 10 px in size.
# so the screen is 500 by 500.

# walls are areas which the player cannot cross. They are
# rects.

leftmost = 2 # '2' so that player doesn't walk through door straight onto wall
uppermost = 1
wall_width = 1
wall_vertical_length = (ROWS-CELLSIZE/2)
wall_horizontal_length = (COLUMNS-CELLSIZE/2) - 1
rightmost = wall_horizontal_length +1
lowest = wall_vertical_length
gap_size = 4

right_door_x = COLUMNS - 1
right_door_y = ROWS/2
door_width = 1
door_height = 3

# map rects are later multipled by 10 to get drawn coordinates
map1.rects = [(leftmost, uppermost, wall_width, wall_vertical_length),
          (leftmost, uppermost, wall_horizontal_length, wall_width),
          (rightmost, uppermost, wall_width, wall_vertical_length - gap_size),
          (leftmost, lowest, wall_horizontal_length- gap_size, wall_width)
         ]
""" The above is: [(2, 1, 1, 45),
                   (2, 1, 44, 1),
                   (45, 1, 1, 41),
                   (2, 45, 40, 1)]
    To give the screen a nice border wall. """

right_door_rect = (right_door_x, right_door_y, door_width, door_height)
left_door_rect = (0, (ROWS/2), 1, 3)

map1_walls = []

for rect in map1.rects:
    map1_wall = map1.rects_to_walls(rect, CELLSIZE)
    map1_walls.append(map1_wall)

map1.walls = map1_walls
right_door_drawn = map1.rects_to_walls(right_door_rect, CELLSIZE)
left_door_drawn = map1.rects_to_walls(left_door_rect, CELLSIZE)
map1.right_door = {'rect': right_door_rect, 'drawn': right_door_drawn,
                   'dest_map': 'map2'}
map1.left_door = {'rect': left_door_rect, 'drawn': left_door_drawn,
                  'dest_map': 'map3'}
map1.colour = YELLOW

map1.characters = [heroine, tiger]
