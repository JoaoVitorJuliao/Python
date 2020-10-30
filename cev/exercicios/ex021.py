# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

"""
import pygame

pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

O PROBLEMA DESSE CÓDIGO É QUE AO MOVIMENTAR O MOUSE, O PROGRAMA É ENCERRADO INSTANTANEAMENTE.

OU

from pygame import mixer

mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()

input('Está escutando? ')

O PROBLEMA DESSE CÓDIGO É QUE O PROGRAMA É ENCERRADO INSTANTANEAMENTE, A NÃO SER QUE O MANTENHA RODANDO, PODENDO SER ATRAVÉS DE UMA INPUT NÃO RESPONDIDA.
"""

from playsound import playsound

playsound('ex021.mp3')
