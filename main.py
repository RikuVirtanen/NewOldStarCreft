import pygame
import sys
from player import Player
from entity import BGEntity
from enemy import Enemy

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
'''
CONSTANTS
'''
WIDTH, HEIGHT = ((960, 720))
ADDENEMY = pygame.USEREVENT + 1
ADDENTITY = pygame.USEREVENT + 2

def draw_text(surface, text, size, pos, color):
    font = pygame.font.Font(pygame.font.match_font('Comic Sans MS'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = pos
    surface.blit(text_surface, text_rect)
    
def handle_events(all_sprites, enemies, entities):
    for event in pygame.event.get():
            
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        
        elif event.type == QUIT:
            sys.exit()
        
        elif event.type == ADDENEMY:
            new_enemy = Enemy(WIDTH, HEIGHT)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)  
            
        elif event.type == ADDENTITY:
            new_entity = BGEntity(WIDTH, HEIGHT)
            entities.add(new_entity)
            all_sprites.add(new_entity)
    
def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    
    pygame.time.set_timer(ADDENEMY, 250)
    
    pygame.time.set_timer(ADDENTITY, 500)
    
    pygame.font.init()
    
    player = Player(WIDTH, HEIGHT)
    
    enemies = pygame.sprite.Group()
    entities = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    clock = pygame.time.Clock()
    
    while True:
        
        handle_events(all_sprites, enemies, entities)
                
        pressed_keys = pygame.key.get_pressed()
        
        
        player.update(pressed_keys)
        enemies.update()
        entities.update()
        
        screen.fill((0, 0, 0))
        
        draw_text(screen, "LIVES: ", 12, (0, 0), (255, 0, 0))
        draw_text(screen, str(player.lives), 12, (50, 0), (255, 0, 0))
        draw_text(screen, "POINTS: ", 12, (100, 0), (255, 0, 0))
        draw_text(screen, str(player.points), 12, (160, 0), (255, 0, 0))
        
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
            
            if pygame.sprite.collide_rect(player, entity):
                if entity in enemies:
                    if player.lives == 1:
                        player.kill()
                        sys.exit()
                    player.lives -= 1
                    entity.kill()
                elif entity in entities:
                    if entity.image == "meteor":
                        player.points += 1
                    elif entity.image == "asteroid":
                        player.points += 2
                    elif entity.image == "planet":
                        player.points += 5
                    elif entity.image == "saturn":
                        player.points += 10
                    elif entity.image == "uranus":
                        player.points += 15
                    entity.kill()
                    

        pygame.display.flip()
        
        clock.tick(30)
        
if __name__ == "__main__":
    main()