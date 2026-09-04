from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_RADIUS
import pygame

class Player(CircleShape):

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.radius = PLAYER_RADIUS
        super().__init__(self.x, self.y, self.radius)
        self.rotation = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        self.screen = screen
        pygame.draw.polygon(self.screen, "white", self.triangle(), LINE_WIDTH)
