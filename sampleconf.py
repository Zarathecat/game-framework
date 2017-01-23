#!/usr/bin/env

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

# If you would like to save your own config, make a copy of this file
# called 'conf.py', and change that.

# Window width in pixels
WIDTH = 500

# Window height in pixels
HEIGHT = 500

# size in pixels of one cell of grid
CELLSIZE = 10

COLUMNS = WIDTH / CELLSIZE
ROWS = HEIGHT / CELLSIZE

grid = []

for row in range(1, ROWS):
    for column in range(1, COLUMNS):
        coordinate = (column, row)
        grid.append(coordinate)

# each coordinate will correspond to one cell in the grid; we will multiply by
# 10

# Framerate; a higher value will result in a faster game
FPS = 40

# Background music, put music in game's music directory and change
# the empty string to something like 'music/example.mp3'

MUSIC = ''

# Save file. Game will read high score from here.

SAVEFILE = 'save.txt'
