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

from colours import *
try:
    from conf import *
except:
    from sampleconf import *
import pygame
from pygame.locals import *
import sys 

""" small utility for finding out desired rect coordinates while
 developing. In the future it'd be nice to display this on a
 static grid, but I found blitting the data to the screen more
 trouble than it was worth, so I'll come back to it. """

main_clock = pygame.time.Clock()

pygame.init()

window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
window_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)

def end_game():

    pygame.quit()
    sys.exit()


def main():
    while True:

        window_surface.fill(BLACK)

        for event in pygame.event.get():
	    if event.type == QUIT:
	        end_game()
      	    if event.type == KEYDOWN:
	        if event.key == K_ESCAPE:
		    end_game()

        x, y = pygame.mouse.get_pos()
        print "screen coordinates = ", (x, y)
        x = x/CELLSIZE
        y = y/CELLSIZE
        print "grid coordinates = ", (x, y)

        pygame.display.update()
        main_clock.tick(40)


main()
