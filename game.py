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
from map1 import *
from map2 import *  # test
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

def check_walls_collision(x, y, chosen_map):
    for rect in chosen_map.rects:
        rect = pygame.Rect(rect)
        if rect.collidepoint(x, y):
            return True
    return False


def check_for_collision(chara, direction, chosen_map):
    """ check for a collision between a character and any screen edges
       or walls. If chara hits screen edge, it sets chara's position
       to the screen edge."""

    chara_x = chara.location[0]
    chara_y = chara.location[1]

    collide = True
    up_check = chara_y - chara.movespeed
    down_check = chara_y + chara.movespeed
    left_check = chara_x - chara.movespeed
    right_check = chara_x + chara.movespeed

    if direction == UP:
        # if y coord doesn't collide with screen upper edge...
        if up_check > 0:
            # check for wall collision with x coord and new y coord
            collide = check_walls_collision(chara_x, up_check, chosen_map)
        # if y coord collides with screen upper edge...
        else:
            # set character's y coordinate to equal the screen upper edge.
            # it's a bit weird putting this in the same function, but
            # not sure how to split it out neatly yet
            chara.location[1] = 0

    elif direction == DOWN:
        if down_check < ROWS:
            collide = check_walls_collision(chara_x, down_check, chosen_map)
        else:
            chara.location[1] = ROWS -1

    elif direction == LEFT:
        if left_check > 0:
            collide = check_walls_collision(left_check, chara_y, chosen_map)
        else:
            chara.location[0] = 0

    elif direction == RIGHT:
        if right_check < COLUMNS:
            collide = check_walls_collision(right_check, chara_y, chosen_map)
        else:
            chara.location[0] = COLUMNS - 1

    return collide


def move_character(chara, direction):
    chara_x = chara.location[0]
    chara_y = chara.location[1]

    if direction == UP:
        chara.location[1] = chara_y - chara.movespeed

    elif direction == DOWN:
        chara.location[1] = chara_y + chara.movespeed

    elif direction == LEFT:
        chara.location[0] = chara_x - chara.movespeed

    elif direction == RIGHT:
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

map_list = {'map1': map1, 'map2': map2}
    
def change_map(new_map):
    for key, value in map_list.iteritems():
        if new_map == key:
            chosen_map =value
    return chosen_map

def main():
    player.location = [COLUMNS/2, ROWS-1]  # player starts at bottom

    direction = ''

    # placement of walls. start with map1
    chosen_map = map1 #test

    while True:
        window_surface.fill(BLACK)
        for wall in chosen_map.walls:
            pygame.draw.rect(window_surface, chosen_map.colour, (wall))


        player_x = player.location[0]
        player_y = player.location[1]
        player_rect = pygame.Rect(player_x, player_y, player.size, player.size)
        player_dimensions = get_dimensions(player_x, player_y, player.size)
        pygame.draw.rect(window_surface, player.colour, (player_dimensions))


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

        if check_for_collision(player, direction, chosen_map) == False:
            move_character(player, direction)

        for chara in chosen_map.characters:

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

            # doors on right and left of screen. This should be tidied...
            # The door rect is the drawn rect /10 .
            # This code is longwinded. Where the player goes depends
            # on the 'direction' of the door, and we don't expect more doors
            # than 'right left up down' for now. The data structure for doors
            # should change when we do.
            right_door_rect = chosen_map.right_door['rect']
            draw_right_door = chosen_map.right_door['drawn']
            pygame.draw.rect(window_surface, GREEN, (draw_right_door))
            left_door_rect = chosen_map.left_door['rect']
            draw_left_door = chosen_map.left_door['drawn']
            pygame.draw.rect(window_surface, GREEN, (draw_left_door))

            # if player hits a door, go to different specified map, and move
            # player to opposite side of screen (to give illusion of travel).
            if player_rect.colliderect(right_door_rect):
                old_map = chosen_map
                chosen_map = change_map(old_map.right_door['dest_map'])
                # we send player to left of screen, though not all the way
                # to the left, as otherwise they'll end up trapped flipping
                # between the two doors. So the player rect starts where the
                # door rect ends.
                player.location[0] = COLUMNS - right_door_rect[0]
            if player_rect.colliderect(left_door_rect):
                old_map = chosen_map
                chosen_map = change_map(old_map.left_door['dest_map'])
                left_door_width = left_door_rect[3]
                right_of_map = left_door_rect[0] + left_door_width
                player.location[0] = COLUMNS - right_of_map

        pygame.display.update()
        main_clock.tick(FPS)


main()
