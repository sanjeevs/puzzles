import pygame


def main():
    pygame.init()
    surface_width = 480
    surface_height = 480

    main_surface = pygame.display.set_mode((surface_width, surface_height))
    some_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        main_surface.fill((0, 255, 0))
        main_surface.fill(some_color, some_rect)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
