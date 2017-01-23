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
from charas import *
from map1 import *
from map2 import *  # test
import os
from player import player
import pygame
from pygame.locals import *
import random
import sys 

main_clock = pygame.time.Clock()

pygame.init()

window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
window_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

pygame.mouse.set_visible(False)

basic_font = pygame.font.SysFont(None, 20)

# placement of walls
chosen_map = map1

# moves character as long as they will not end up offscreen
def move_character(chara, direction):
    chara_x = chara.location[0]
    chara_y = chara.location[1]
    if direction == UP:
        # check character won't go off top of screen
        if chara_y - chara.movespeed > -chara.movespeed:
            # check for wall collision. only move chara if not
            for rect in chosen_map.rects:
                rect = pygame.Rect(rect)
                if rect.collidepoint(chara_x, chara_y - chara.movespeed):
                    break
            else:
                chara.location[1] = chara_y - chara.movespeed

    elif direction == DOWN:
        # check chara won't go off bottom of screen
        if chara_y + chara.movespeed < ROWS:
            for rect in chosen_map.rects:
                rect = pygame.Rect(rect)
                if rect.collidepoint(chara_x, chara_y + chara.movespeed):
                    break
            else:
                chara.location[1] = chara_y + chara.movespeed

    elif direction == LEFT:
        # check won't go off left
        if chara_x - chara.movespeed > -chara.movespeed:
            for rect in chosen_map.rects:
                rect = pygame.Rect(rect)
                if rect.collidepoint(chara_x - chara.movespeed, chara_y):
                    break
            else:
                chara.location[0] = chara_x - chara.movespeed

    elif direction == RIGHT:
        #check won't go off right
        if chara_x + chara.movespeed < ROWS:
            for rect in chosen_map.rects:
                rect = pygame.Rect(rect)
                if rect.collidepoint(chara_x + chara.movespeed, chara_y):
                    break
            else:
                chara.location[0] = chara_x + chara.movespeed

    return chara.location


def end_game():

    pygame.quit()
    sys.exit()

def get_dimensions(x, y, size):
    chara_x_pos = x * CELLSIZE
    chara_y_pos = y * CELLSIZE
    chara_scaled = size * CELLSIZE
    chara_dimensions = chara_x_pos, chara_y_pos, chara_scaled, chara_scaled
    return chara_dimensions
    

def main():
    player.location = [COLUMNS/2, ROWS-1]  # player starts at bottom

    direction = ''

    while True:

        window_surface.fill(BLACK)
        for wall in chosen_map.walls:
            pygame.draw.rect(window_surface, chosen_map.colour, (wall)) #test


        player_x = player.location[0]
        player_y = player.location[1]
        player_rect = pygame.Rect(player_x, player_y, player.size, player.size)
        player_dimensions = get_dimensions(player_x, player_y, player.size)
        pygame.draw.rect(window_surface, BRIGHTGREEN, (player_dimensions))


        for event in pygame.event.get():
	    if event.type == QUIT:
	        end_game()
      	    if event.type == KEYDOWN:
	        if event.key == K_ESCAPE:
		    end_game()
	        elif event.key == K_LEFT:
		    direction = LEFT
                elif event.key == K_RIGHT:
		    direction = RIGHT
                elif event.key == K_UP:
		    direction = UP
                elif event.key == K_DOWN:
                    direction = DOWN
	# stop if user releases key. we don't use keyup as they might
	# release a key while holding another down.
        # There is probably a neater way of doing this.
            elif 1 not in pygame.key.get_pressed():
                direction = ""

        move_character(player, direction)

        for chara in charas:

            # this currently won't handle long lines very well. or at all.
            chara_text = chara.catchphrase
            text_surf = basic_font.render(chara_text, 1, WHITE)
            text_rect = text_surf.get_rect()
            text_rect.top = ROWS / 9 * CELLSIZE

            chara_x = chara.location[0]
            chara_y = chara.location[1]
            chara_rect = pygame.Rect(chara_x, chara_y, chara.size, chara.size)

            chara_dimensions= get_dimensions(chara_x, chara_y, chara.size)
            pygame.draw.rect(window_surface, chara.colour, (chara_dimensions))


            if chara_rect.colliderect(player_rect):
                window_surface.blit(text_surf, text_rect)

        pygame.display.update()
        main_clock.tick(FPS)


main()
