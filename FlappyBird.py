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
def score_update():
    global score,score_time,high_score_time
    if pipes:
        for pipe in pipes:
            if 65 < pipe.centerx < 69 and score_time:
                score += 1 
                score_time = False
            if pipe.left <= 0:
                score_time = True
    if score > high_score:
        high_score = score
def draw_score(game_state):
    if game_state == "game_on":
        score_text = score_font.render(str(score),True,(255,255,255))
        score_rect = score_text.get_rect(center=(width // 2,66))
        screen.blit(score_text,score_rect)
    elif game_state == "game_over":
        score_text = score_font.render(f"Score:{score}",True,(255,255,255))
        score_rect = score_text.get_rect(center=(width // 2,66))
        screen.blit(score_text,score_rect)

        high_sacore_text = score_font.render(f"Score:{high_score}",True,(255,255,255))
        high_score_rect = high_score_text.get_rect(center=(width // 2,506))
        screen.blit(high_sacore_text,high_score_rect)