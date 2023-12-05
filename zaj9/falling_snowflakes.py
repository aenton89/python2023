import pygame
import sys
import random


# makra
BACKGROUND = (153, 217, 234)
COUNTER_COLOR = (0, 183, 239)
FPS = 60
SNOWFLAKE_SPEED = 1.5
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SNOWFLAKE_SCALE = 2
MAX_FALLEN_SNOWFLAKES = 3

# klasa platka sniegu
class Snowflake(pygame.sprite.Sprite):

    def __init__(self, image, speed = SNOWFLAKE_SPEED):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 0
        self.speed = speed
    
    def update(self):
        self.rect.y += self.speed

# inicjalizacja biblioteki pygame
pygame.init()

# ekran startowy
start_screen_font = pygame.font.Font(None, 36)
start_screen_text_line1 = "Press Enter to start the game"
start_screen_text_line2 = "Game's over when 3 snowflakes fall down"
start_screen_text1 = start_screen_font.render(start_screen_text_line1, True, (255, 255, 255))
start_screen_text2_font = pygame.font.Font(None, 24)
start_screen_text2 = start_screen_text2_font.render(start_screen_text_line2, True, (255, 255, 255))
start_screen_rect1 = start_screen_text1.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
start_screen_rect2 = start_screen_text2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 10))

# ekran koncowy
end_screen_font = pygame.font.Font(None, 56)
end_screen_text = end_screen_font.render("Game Over", True, (255, 255, 255))
end_screen_rect = end_screen_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))

# licznik platkow sniegu
snowflake_counter_font = pygame.font.Font(None, 24)
snowflake_counter = 0

# flagi ekranow
start_screen = True
game_screen = False
end_screen = False

# ekran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snowflake Melting Game")

# platki sniegu
try:
    original_snowflake_image = pygame.image.load("snowflake.png")
except pygame.error:
    print("Nie można wczytać obrazka 'snowflake.png'")
    pygame.quit()
    sys.exit()

# skalowanie obrazka
original_width, original_height = original_snowflake_image.get_size()
scaled_width = int(original_width * SNOWFLAKE_SCALE)
scaled_height = int(original_height * SNOWFLAKE_SCALE)
snowflake_image = pygame.transform.scale(original_snowflake_image, (scaled_width, scaled_height))

sg_snowflakes = pygame.sprite.Group()

# zegar
clock = pygame.time.Clock()

# MAIN LOOP
while True:
    # obsluga zdarzen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_screen:
            mouse_pos = pygame.mouse.get_pos()
            clicked_snowflakes = [snowflake for snowflake in sg_snowflakes if snowflake.rect.collidepoint(mouse_pos)]
            for c_snowflake in clicked_snowflakes:
                c_snowflake.kill()
        elif event.type == pygame.KEYDOWN and start_screen:
            if event.key == pygame.K_RETURN:
                start_screen = False
                game_screen = True
        
    #wyswietlenie ekranu startowego
    if start_screen:
        screen.fill(BACKGROUND)
        screen.blit(start_screen_text1, start_screen_rect1)
        screen.blit(start_screen_text2, start_screen_rect2)
        pygame.display.flip()
        continue

    elif game_screen:
        # nowe platki sniegu
        if (random.random()) < 0.03:
            snowflake = Snowflake(snowflake_image)
            sg_snowflakes.add(snowflake)

    elif end_screen:
        screen.fill(BACKGROUND)
        screen.blit(end_screen_text, end_screen_rect)
        pygame.display.flip()
        continue

    # sprawdzenie czy platki spadly
    for snowflake in sg_snowflakes:
            if snowflake.rect.bottom >= SCREEN_HEIGHT:
                snowflake_counter += 1

    if snowflake_counter >= MAX_FALLEN_SNOWFLAKES:
        game_screen = False
        end_screen = True

    # usuniecie platkow, ktore spadly
    sg_snowflakes = pygame.sprite.Group([snowflake for snowflake in sg_snowflakes if snowflake.rect.bottom < SCREEN_HEIGHT])

    # rysowanie i update
    sg_snowflakes.update()
    screen.fill(BACKGROUND)
    sg_snowflakes.draw(screen)

    snowflake_counter_text = snowflake_counter_font.render(f"Snowflakes fallen: {snowflake_counter}", True, COUNTER_COLOR)
    screen.blit(snowflake_counter_text, (10, SCREEN_HEIGHT - 30))
 
    pygame.display.flip()
    clock.tick(FPS)