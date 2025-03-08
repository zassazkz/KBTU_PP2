import pygame 

pygame.mixer.init()
pygame.init()
sc = pygame.display.set_mode((400,300), pygame.RESIZABLE)

pygame.display.set_caption("Music Player")


image = pygame.image.load('mus.jpeg')
image = pygame.transform.scale(image, (400, 300))

music = ["Miley Cyrus - Jolene.mp3","Soap&Skin - Me and the Devil.mp3","The Willow Maid - Erutan.mp3"]

current_music = 0
pygame.mixer.music.load(music[current_music])

pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                current_music = (current_music + 1) % len(music)
                pygame.mixer.music.load(music[current_music])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_music = (current_music - 1) % len(music)
                pygame.mixer.music.load(music[current_music])
                pygame.mixer.music.play()


    sc.blit(image, (0, 0))
    pygame.display.flip()


pygame.quit()