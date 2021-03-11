import pygame
import sys
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

font = pygame.font.SysFont(None, 30)

black = (0, 0, 0)
white = (255, 255, 255)

width, height = 700, 500

window = pygame.display.set_mode((width, height))

pygame.display.set_caption('Dream Space')

game_icon = pygame.image.load('icon.png')

pygame.display.set_icon(game_icon)

fps = 60

clock = pygame.time.Clock()

player_width = 60
player_height = 60

player_img = pygame.image.load('sprites/player.png')
player_img = pygame.transform.scale(player_img, (player_width, player_height))
player_img = pygame.transform.rotate(player_img, 180)

space_img = pygame.image.load('sprites/space.png')
space_img = pygame.transform.scale(space_img, (width, height))

enemy_width = 60
enemy_height = 60

enemy_x = 0
enemy_y = -100

enemy_img = pygame.image.load('sprites/enemy.png')
enemy_img = pygame.transform.scale(enemy_img, (enemy_width, enemy_height))

space_speed = 10



def main():
	enemy_speed = 5
	player_speed = 5

	max_enemies = 5

	space_x = 0
	space_y = 0

	player_x = (width // 2) - player_width // 2
	player_y = (height - player_height) - 50

	enemies = []

	score = 0

	while True:
		clock.tick(fps)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()
		window.fill(black)

		window.blit(space_img, (space_x, space_y))
		window.blit(space_img, (space_x, space_y - height))

		window.blit(player_img, (player_x, player_y))

		space_y += space_speed

		if space_y >= height:
			space_y = 0


		if keys[pygame.K_a] and player_x - player_speed > 0: # LEFT
			player_x -= player_speed

		if keys[pygame.K_d] and player_x + player_speed < width - player_width: # RIGHT
			player_x += player_speed


		score_text = font.render(f'SCORE: {score}', True, white)
		window.blit(score_text, (0, 0))

		if random.random() < 0.01:
			if len(enemies) < max_enemies:
				enemy_x = random.randint(0, width - enemy_width)
				enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
				enemies.append(enemy_rect)


		player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
		for rect in enemies:
			window.blit(enemy_img, (rect.x, rect.y))

			if rect.y > height:
				if rect in enemies:
					enemies.remove(rect)
					score += 1
					if score % 10 == 0 and score != 0:
						enemy_speed += 1
						player_speed += 0.1
						max_enemies += 1

					

			rect.y += enemy_speed


			if player_rect.colliderect(rect):
				pygame.display.update()
				pygame.time.delay(2000)
				main()

		pygame.display.update()


main()