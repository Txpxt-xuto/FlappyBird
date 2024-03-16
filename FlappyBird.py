import sys
import time
import random
import pygame

ptgame.init()
clock = pygame.time.Clock()

def draw_floor():
    screen.blit(floor_img, (floor_x, 520))
    screen.blit(floor_img, (floor_x + 480, 520))
def create_pipes():
    pipe_y = random.choice(pipe_height)
    top_pipe = pipe_img.get_rect(midbottom=(467, pipe_y - 300))
    bottom_pipe = pipe_img.get_rect(midbottom=(467, pipe_y))
    return top_pipe, bottom_pipe
def pipe_animation():
    global game_over, score_time
    for pipe in pipes:
        if pipe.top < 0:
            flipped_pipe = pygame.transform.flip(pipe_img,False,True)
            screen.blit(flipped_pipe, pipe)
        else:
            screen.blit(pipe_img, pipe)
        pipe.centerx -=3
        if pip.right < 0:
            pipes.remove(pipe)
        if bird_rect.colliderect(pipe):
            game_over = True
