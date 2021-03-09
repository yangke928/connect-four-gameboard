'''Ke Yang
   cs5001
   Project
   April 1st
'''
from turtle import *

SIZE_PIECES = 20
SIZE_BOARD_UNIT = 50
SIZE_TRIANGLE = 15

class Chessboard:
    '''Class Chessboard
       Attributes: window, num_column, num_row, pieces,
                   pieces.hideturtle(), triangle, triangle.hideturtle()
                   big_board, big_board.hideturtle(), turn, turn.hideturtle()
                   button_loc_x, button_loc_y, board_loc_x, board_loc_y
       Methods: draw_score, draw_turn, draw_turn_mvc, draw_circle
                draw_triangle, draw_board, draw_all_board, is_press_valid,
                find_column_of_button, draw_new_piece
    '''
    def __init__(self, num_column, num_row):
        '''
        Constructor -- creates new instances of chessboard
        Parameters:
            self -- the current object
            num_column -- the number of columns that player input
            num_row -- the number of rows that player input
        '''
        self.window = Screen()
        self.num_column = num_column
        self.num_row = num_row
        self.pieces = Turtle()
        self.pieces.hideturtle()
        self.triangle = Turtle()
        self.triangle.hideturtle()
        self.big_board = Turtle()
        self.big_board.hideturtle()
        self.turn = Turtle()
        self.turn.hideturtle()
        self.button_loc_x = 0
        self.button_loc_y = 0
        self.board_loc_x = -(num_column / 2 -0.5) * SIZE_BOARD_UNIT
        self.board_loc_y = -(num_row / 2 * SIZE_BOARD_UNIT - \
                             (SIZE_BOARD_UNIT / 2 - SIZE_PIECES))

    def draw_score(self, red_score, yellow_score):
        '''
        Method -- show the current score of red and yellow player
        Parameters:
            self -- the current object
            red_score -- the current score of red player
            yellow_socre -- the current score of yellow player
        '''
        
        self.big_board.penup()
        self.big_board.goto(0, (self.num_row /2 + 1) * SIZE_BOARD_UNIT)
        self.big_board.color("black")
        self.big_board.write("Red:"+str(red_score)+" Yellow:"+str(yellow_score), \
                             align = "center", font = ("Time", 20, "normal"))

    def draw_turn(self, num):
        '''
        Method -- show the current player is red or yellow in man vs man game
        Parameter :
            self -- the current boject
            num -- 0 for red player and 1 for yellow player
        '''
        if num == 0:
            player = "red"
        else:
            player = "yellow"
        self.turn.penup()
        self.turn.goto(int((-self.num_column/2 - 1) * SIZE_BOARD_UNIT),0)
        self.turn.clear()
        self.turn.color(player)
        self.turn.write(player + " 's\nturn ", align = "center", \
                        font = ("Time", 15, "normal"))

    def draw_turn_mvc(self, num):
        '''
        Method -- show the current paly is player or computer
                  in man vs computer game
        Parameter:
            self -- the current object
            num -- 0 for the player and 1 for the computer
        '''
        if num == 0:
            player = "you"
        else:
            player = "computer"
        self.turn.penup()
        self.turn.goto(int((-self.num_column/2 - 1) * SIZE_BOARD_UNIT),0)
        self.turn.clear()
        self.turn.color("red" if player == "you" else "yellow")
        self.turn.write(player+"\n"+"turn", align = "center", \
                        font = ("Time", 15, "normal"))
        
    def draw_circle(self, x, y, color):
        '''
        Method -- draw the circle in the chessboard
        Parameters:
            self -- the current object
            x, y -- the x coordinate and y coordinate of the
                    positon of the circle to draw
            color -- the color of the circle in the chess board in
                     different situations
        '''
        self.pieces.penup()
        self.pieces.speed(0)
        self.pieces.goto(x, y)
        self.pieces.color(color)
        self.pieces.begin_fill()
        self.pieces.circle(SIZE_PIECES)
        self.pieces.end_fill()

    def draw_triangle(self, x,y):
        '''
        Method -- draw the triangle as the user button in the chessboard
        Parameters:
            self -- the current object
            x, y -- the x coordinate and y coordinate of the
                    position of the triangle to draw
        '''
        self.triangle.penup()
        self.triangle.goto(x, y)
        self.triangle.color("black")
        self.triangle.begin_fill()
        self.triangle.speed(0)
        for i in range (3):
            self.triangle.fd(SIZE_TRIANGLE)
            self.triangle.right(120)
        self.triangle.end_fill()
    
    
    def draw_board(self):
        '''
        Method -- draw the whole borad
        Parameters:
            self -- the current object
        '''
        self.big_board.penup()
        self.big_board.speed(0)
        self.big_board.goto(-self.num_column / 2 * SIZE_BOARD_UNIT, \
                            self.num_row /2 * SIZE_BOARD_UNIT)
        self.big_board.color("blue")
        self.big_board.begin_fill()
        for n in range (2):
            self.big_board.fd(self.num_column * SIZE_BOARD_UNIT)
            self.big_board.right(90)
            self.big_board.fd(self.num_row * SIZE_BOARD_UNIT)
            self.big_board.right(90)
        self.big_board.end_fill()
        x = self.board_loc_x 
        y = self.board_loc_y 
        for i in range(self.num_row):
            for j in range(self.num_column):
                self.draw_circle(x, y, "white")
                x += SIZE_BOARD_UNIT
            x = -(self.num_column / 2 -0.5) * SIZE_BOARD_UNIT
            y += SIZE_BOARD_UNIT
        
    def draw_all_board(self):
        '''
        Method -- draw all the board and the triangle as the player button
        Parameters:
            self -- the current object
        '''
        self.draw_board()
        x = -(self.num_column / 2 * SIZE_BOARD_UNIT - SIZE_BOARD_UNIT / 2 \
              + SIZE_TRIANGLE / 2)
        y = self.num_row / 2 * SIZE_BOARD_UNIT + SIZE_BOARD_UNIT / 2
        self.button_loc_x = x
        self.button_loc_y = y
        for i in range(self.num_column):
            self.draw_triangle(x,y)
            x += SIZE_BOARD_UNIT


    def is_press_valid(self, x, y):
        '''
        Method -- check if the player click on the button (the triangle)
        Parameters:
            self -- the current object
            x, y -- the x coordinate and y coordinate of the position
                    where the player click
        '''
        if self.button_loc_x <= x <= - self.button_loc_x and \
        (self.button_loc_y - SIZE_TRIANGLE) <= y<= self.button_loc_y:
            if (x - self.button_loc_x) % SIZE_BOARD_UNIT <= SIZE_TRIANGLE:
                return True
        else:
            return False

    def find_column_of_button(self, x):
        '''
        Method -- check which column the player click
        Parameters:
            self -- the current object
            x - the potision of player click, the x coordinate
        '''
        return int((x - self.button_loc_x)//SIZE_BOARD_UNIT)

    def draw_new_piece(self, ro, co, color):
        '''
        Method -- draw a new circle where the player put their
                  pieces on in the player's color
        Parameters:
            self -- the current object
            ro -- which row the current piece in
            co -- which colunm the current piece in
            color -- which color the current player is, red or yellow
        '''
        self.draw_circle(self.board_loc_x + co * SIZE_BOARD_UNIT, \
                         self.board_loc_y + ro * SIZE_BOARD_UNIT, color)        
    
        

        
 
            
        
       
        
    
