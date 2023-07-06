import pygame
import os
import random
tela_largura = 500
tela_altura = 800

imagem_cano = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
imagem_chao = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
imagem_background = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
imagens_passaro = [
pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))
]
pygame.font.init()
fontes_pontos = pygame.SysFont("arial", 50)

class passaro:
    imgs = imagens_passaro
    rotação_maxima = 25
    velocidade_rotação = 20
    tempo_animacao = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0

