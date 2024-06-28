import pygame
import sys
import time

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre du jeu
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong - Jeu de Tennis de table")

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Vitesse de rafraîchissement de l'écran
fps = 60
clock = pygame.time.Clock()

# Dimensions des raquettes et de la balle
paddle_width = 10
paddle_height = 80
ball_size = 10

# Positions initiales des raquettes et de la balle
paddle1_pos = [110, (screen_height - paddle_height) // 2]  # Raquette gauche dans le cadre de jeu
paddle2_pos = [screen_width - 120, (screen_height - paddle_height) // 2]  # Raquette droite dans le cadre de jeu
ball_pos = [screen_width // 2, screen_height // 2]
ball_vel = [4, 4]

# Vitesse des raquettes
paddle1_vel = 0
paddle2_vel = 0
paddle_speed = 6

# Scores et statistiques
paddle1_misses = 0
paddle2_misses = 0
start_time = time.time()
total_guesses = 0

# Fonction pour dessiner les éléments du jeu
def draw():
    screen.fill(black)
    
    # Dessiner le cadre de jeu réduit pour la balle
    pygame.draw.rect(screen, gray, (100, 60, screen_width - 200, screen_height - 120))
    
    # Dessiner les raquettes
    pygame.draw.rect(screen, white, (*paddle1_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (*paddle2_pos, paddle_width, paddle_height))
    
    # Dessiner la balle
    pygame.draw.ellipse(screen, white, (*ball_pos, ball_size, ball_size))
    
    # Dessiner les informations autour du cadre de jeu
    font = pygame.font.SysFont(None, 20)
    
    # Afficher le temps de jeu
    elapsed_time = int(time.time() - start_time)
    text_time = font.render(f"Temps de jeu: {elapsed_time} sec", True, white)
    screen.blit(text_time, (10, 10))
    
    # Afficher le nombre de coups joués
    text_guesses = font.render(f"Nombre de coups joués: {total_guesses}", True, white)
    screen.blit(text_guesses, (10, 30))
    
    # Afficher le nombre de coups ratés
    text_misses = font.render(f"Nombre de coups ratés: Gauche {paddle1_misses} - Droite {paddle2_misses}", True, white)
    screen.blit(text_misses, (10, 50))
    
    # Afficher les contrôles
    text_controls = "Contrôles: S pour monter, W pour descendre la raquette gauche; " \
                    "Flèches Haut/Bas pour la raquette droite"
    text_controls_surface = font.render(text_controls, True, white)
    screen.blit(text_controls_surface, (screen_width // 2 - text_controls_surface.get_width() // 2, screen_height - 60))
    
    # Dessiner le bouton fermer
    pygame.draw.rect(screen, gray, (screen_width - 120, 10, 100, 30))
    text_close = font.render("Fermer", True, black)
    screen.blit(text_close, (screen_width - 110, 15))
    
    pygame.display.flip()

# Fonction pour gérer les collisions de la balle
def ball_collision():
    global ball_vel, paddle1_misses, paddle2_misses
    # Collision avec les parois supérieure et inférieure du cadre de jeu de la balle
    if ball_pos[1] <= 70 or ball_pos[1] >= screen_height - ball_size - 50:
        ball_vel[1] = -ball_vel[1]
    
    # Collision avec les raquettes
    if (ball_pos[0] <= paddle1_pos[0] + paddle_width and 
        paddle1_pos[1] < ball_pos[1] < paddle1_pos[1] + paddle_height):
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] <= 110:
        paddle2_misses += 1
        reset_ball()
    elif (ball_pos[0] >= paddle2_pos[0] - ball_size and 
          paddle2_pos[1] < ball_pos[1] < paddle2_pos[1] + paddle_height):
        ball_vel[0] = -ball_vel[0]
    elif ball_pos[0] >= screen_width - ball_size - 110:
        paddle1_misses += 1
        reset_ball()

# Fonction pour remettre la balle au centre après un point marqué
def reset_ball():
    global ball_pos, ball_vel
    ball_pos = [screen_width // 2, screen_height // 2]
    ball_vel = [4, 4]

# Fonction pour mettre à jour la position des éléments du jeu
def update():
    global ball_pos, paddle1_pos, paddle2_pos, total_guesses
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    
    # Empêcher les raquettes de sortir du cadre de jeu
    paddle1_pos[1] = max(min(paddle1_pos[1], screen_height - paddle_height - 50), 70)
    paddle2_pos[1] = max(min(paddle2_pos[1], screen_height - paddle_height - 50), 70)
    
    # Compter le nombre de coups joués
    total_guesses += 1

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_vel = -paddle_speed   # Descendre la raquette gauche
            elif event.key == pygame.K_s:
                paddle1_vel = paddle_speed    # Monter la raquette gauche
            elif event.key == pygame.K_UP:
                paddle2_vel = -paddle_speed   # Monter la raquette droite
            elif event.key == pygame.K_DOWN:
                paddle2_vel = paddle_speed    # Descendre la raquette droite
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle1_vel = 0   # Arrêter la raquette gauche
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle2_vel = 0   # Arrêter la raquette droite
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if screen_width - 120 <= event.pos[0] <= screen_width - 20 and 10 <= event.pos[1] <= 40:
                running = False  # Clique sur le bouton fermer

    update()
    ball_collision()
    draw()
    
    clock.tick(fps)

pygame.quit()
sys.exit()
