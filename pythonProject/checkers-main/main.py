import pygame as pg
from game import *

width = 700
height = 700
rows = 8
cols = 8
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (120, 42, 42)
squareSize = width // rows

image1 = pg.transform.scale(pg.image.load('images/checkers.png'), (60, 60))
image2 = pg.transform.scale(pg.image.load('images/image2.jpg'), (60, 60))


def drawAll(screen, board):
    drawBoard(screen)
    drawPiece(screen, board)


def drawBoard(window):
    window.fill(brown)
    board = Game().board
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "w":
                pg.draw.rect(window, white, (col * squareSize, row * squareSize, squareSize, squareSize))


def drawPiece(screen, board):
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == "w":
                if row < 3:
                    screen.blit(image1, (col * squareSize, row * squareSize, squareSize // 2, squareSize // 2))
                if row > 4:
                    screen.blit(image2, (col * squareSize, row * squareSize, squareSize, squareSize))


def main():
    pg.init()
    window = pg.display.set_mode((width, height))
    clock = pg.time.Clock()
    window.fill(blue)
    running = True
    board = Game().board

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        clock.tick(60)
        drawAll(window, board)
        pg.display.update()

    pg.quit()


main()
