import pygame

class KeyboardControll:
    def __init__(self):
        pygame.init()
        win = pygame.display.set_mode((400, 400))

    def get_key(self, key_name: str) -> bool:
        ans: bool = False
        for e in pygame.event.get(): pass
        key_input = pygame.key.get_pressed()
        key = getattr(pygame, 'K_{}'.format(key_name))
        if key_input[key]:
            ans = True
        pygame.display.update()
        return ans
