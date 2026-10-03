import pygame

pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
#não sei se vai funcionar com todo mundo, quando eu fiz o curso funcionou, mas no momento atual to udando o python 3.14 e aparentemente nao tem versão do pygame pra essa versão