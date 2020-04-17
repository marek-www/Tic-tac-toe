# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:16:47 2020

author: Marek
"""

import pygame
import sys

pygame.init()

game = True

while game:
    
    WIDTH = 600
    HEIGHT = 600
    
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    
    matrix = [[None for i in range(3)] for j in range(3)]
    counter = 0
    win = None
    winner = None
    win_line = None
    
    x_png = pygame.image.load('x.png')
    o_png = pygame.image.load('o.png')
    X_pic = pygame.transform.scale(x_png, (WIDTH//3, HEIGHT//3))
    O_pic = pygame.transform.scale(o_png, (WIDTH//3, HEIGHT//3))
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
    
    def display():
    
        screen.fill(white)
        pygame.display.set_caption('Tic Tac Toe')
        pygame.draw.line(screen, black, (WIDTH/3, 0), (WIDTH/3, HEIGHT), 5)
        pygame.draw.line(screen, black, (WIDTH * 2 / 3, 0), (WIDTH * 2 / 3, HEIGHT), 5)
        pygame.draw.line(screen, black, (0, HEIGHT/3), (WIDTH, HEIGHT/3), 5)
        pygame.draw.line(screen, black, (0, HEIGHT * 2 / 3), (WIDTH, HEIGHT * 2 / 3), 5)
        pygame.draw.rect(screen, black, (0, HEIGHT, WIDTH, 100))
    
    def update_prompt():
        
        font = pygame.font.SysFont('comicsansms', 50)
        text = None
    
        if winner == 'X':
            text = 'X won!'
        elif winner == 'O':
            text = 'O won!'    
        elif counter == 9:
            text = ' Draw! '
        elif counter % 2 == 0:
            text = 'O turn'
        elif counter % 2 == 1:
            text = 'X turn'
            
        text_disp = font.render(text, True, red, black)
        text_rect = text_disp.get_rect(center = (WIDTH/2, HEIGHT + 50))
        screen.blit(text_disp, text_rect)
        
    def click(pos):
        
        x, y = pos
        
        if x < WIDTH / 3:
            column = 0
        elif x >= WIDTH / 3 and x < WIDTH * 2 / 3:
            column = 1
        elif x >= WIDTH * 2 / 3:
            column = 2
    
        if y < HEIGHT / 3:
            row = 0
        elif y >= HEIGHT / 3 and y < HEIGHT * 2 / 3:
            row = 1
        elif y >= HEIGHT *2 / 3 and y < HEIGHT:
            row = 2        
        return row, column
    
    def update_matrix(mat):
        
        global counter
        
        XO = None
        row, col = click(event.pos)
        if mat[row][col] == None:
            counter += 1
            if counter % 2 == 0:
                XO = 'X'
                screen.blit(X_pic, (col*(HEIGHT/3), row*(WIDTH/3)))
            else:
                XO = 'O'
                screen.blit(O_pic, (col*(HEIGHT/3), row*(WIDTH/3)))
            mat[row][col] = XO
    
    def winner(mat):
        
        global win, winner, win_line
        
        for idx, row in enumerate(mat):
            if row[0] == row[1] == row[2] != None:
                if row[0] == 'X':
                    winner = 'X'
                else:
                    winner = 'O'
                win_line = ('row', idx)
                win = True  
                draw_line(win_line)
        
        for col in range(3):
            if mat[0][col] == mat[1][col] == mat[2][col] != None:
                if mat[0][col] == 'X':
                    winner = 'X'
                else:
                    winner = 'O'
                win_line = ('col', col)
                win = True
                draw_line(win_line)
                
        if mat[0][0] == mat[1][1] == mat[2][2] != None:
            if mat[1][1] == 'X':
                winner = 'X'
            else:
                winner = 'O'
            win_line = ('down', -1)
            win = True
            draw_line(win_line)
    
        if mat[0][2] == mat[1][1] == mat[2][0] != None:
            if mat[1][1] == 'X':
                winner = 'X'
            else:
                winner = 'O'
            win_line = ('up', 1)
            win = True
            draw_line(win_line)
        
        if counter == 9:
            win = True
    
    
    def draw_line(end):
        
        line, num = end

        if win:
            if line == 'row':
                pygame.draw.line(screen, red, (10, (num*HEIGHT/3 + HEIGHT/6)), (WIDTH-10, (num*HEIGHT/3 + HEIGHT/6)), 10)
            elif line == 'col':
                pygame.draw.line(screen, red, ((num*WIDTH/3 + WIDTH/6), 10), ((num*WIDTH/3 + WIDTH/6), HEIGHT-10), 10)
            elif line == 'down':
                pygame.draw.line(screen, red, (10, 10), (WIDTH - 10, HEIGHT - 10), 10)
            elif line == 'up':
                pygame.draw.line(screen, red, (10, HEIGHT - 10), (WIDTH - 10, 10), 10)
                
    def restart_game():
        
        global game
        pygame.draw.rect(screen, black, (0, HEIGHT, WIDTH/2, 100))
        pygame.draw.rect(screen, black, (WIDTH/2, HEIGHT, WIDTH/2, 100))
        pygame.draw.rect(screen, red, (0, HEIGHT, WIDTH/2, 100), 5)
        pygame.draw.rect(screen, red, (WIDTH/2, HEIGHT, WIDTH/2, 100), 5)
        
        font = pygame.font.SysFont('comicsansms', 50)
        text1 = 'Play again'
        text2 = 'Quit'
        button_1_text = font.render(text1, True, red, black)
        button_1_rect = button_1_text.get_rect(center = (WIDTH/4, HEIGHT + 50))
        button_2_text = font.render(text2, True, red, black)
        button_2_rect = button_2_text.get_rect(center = (WIDTH*3/4, HEIGHT + 50))
        screen.blit(button_1_text, button_1_rect)
        screen.blit(button_2_text, button_2_rect)
        pygame.display.flip() 

        while True:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    
                    x, y = event.pos
                    
                    if y > HEIGHT:
                        
                        if x < WIDTH/2:
                            print('lewy')
                        elif x > WIDTH/2:
                            print('prawy')
                            game = False
                        return None
               
    display()
    pygame.display.flip()
       
    while not win:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    update_matrix(matrix)
                except:
                    continue
                winner(matrix)
                update_prompt()
                pygame.display.flip()
                if win:
                    restart_game()
                    

pygame.quit()
sys.exit()        
            
