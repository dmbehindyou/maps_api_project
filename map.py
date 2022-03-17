import os
import sys
import pygame
import requests


class MapParams(object):
    def __init__(self):
        self.lon = 52.422864
        self.lat = 55.767974
        self.z = 18
        self.type = "map"


def create_map(mp):
    params = {
        "ll": ",".join([str(mp.lon), str(mp.lat)]),
        "z": mp.z,
        "l": mp.type
    }
    api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(api_server, params=params)
    if not response:
        print("Ошибка выполнения запроса:")
        sys.exit(0)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    mp = MapParams()
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_PAGEUP and mp.z <= 20:
                mp.z += 1
            elif event.key == pygame.K_PAGEDOWN and mp.z > 1:
                mp.z -= 1
        map_file = create_map(mp)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove(map_file)


if __name__ == "__main__":
    main()
