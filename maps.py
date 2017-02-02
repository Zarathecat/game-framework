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

class Map():
    def __init__(self):
        self.walls = [(0, 0, 0,0), (0,0,0,0) ] #rects for drawing
        self.rects = [(0, 0, 0, 0), (0,0,0,0)] #rects for collision detection
        self.colour = ''
        self.right_door = {'rect': (0,0,0,0), 'drawn': (0,0,0,0),
                           'dest_map' : ''}
        self.left_door = {'rect': (0,0,0,0), 'drawn': (0,0,0,0),
                           'dest_map' : ''}
        self.characters = []
