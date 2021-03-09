'''Ke Yang
   cs5001
   Project
   April 1st
'''
from chessboard import *
from point import *
import random

COLOR = ["red", "yellow"]

class Game:
    '''Class Game
       Attributes: point, co, ro, currentplayer, curr_ro, curr_co
                   red_scorefile, yellow_scorefile, column_play_pick
                   lst
       Methods: init_chessboard, initialize_lst, save_red_score,
                save_yellow_score, change_lst, horizontal, vertical,
                diagonal, is_full, check_click, launcher_phase1.
                launcher_manvsman, launcher_manvscomputer
    '''
    def __init__(self, red_scorefile, yellow_scorefile,num_column, num_row):
        '''
        Constructor -- create new instances of game
        Parameters:
            self -- the current object
            red_socrefile -- the file that has the red play's score
            yellow_socrefile -- the file that has the yellow play's score
            num_column -- the number of columns the player wants to have
                          in the chessboard
            num_row -- the number of rows the player wants to have
                          in the chessboard
        '''
        self.point = Point()
        self.co = num_column
        self.ro = num_row
        # 0 for red, 1 for yellow and -1 for empty
        self.currentplayer = 0 
        self.curr_ro = 0
        self.curr_co = 0
        self.red_scorefile = red_scorefile
        self.yellow_scorefile = yellow_scorefile
        self.column_play_pick = int(0)
        self.lst = []

    def init_chessboard(self):
        '''
        Method -- initialize Chessboard
        Parameters --
            self -- the current object
        '''
        self.chessboard = Chessboard(self.co, self.ro)

    def initialize_lst(self):
        '''
        Method -- get the origianl list to present the pieces in chessboard,
                  0 for red, 1 for yellow, -1 for empty
        Parameters --
            self -- the current object
        '''
        temp_lst = []
        for i in range(self.co):
            temp_lst.append(-1)
        for j in range(self.ro):
            self.lst.append(temp_lst.copy())

    def save_red_score(self):
        '''
        Method -- save the red player's score in the red scorefile
        Parameters:
            self -- the current object
        '''
       
        try:
            with open (self.red_scorefile, "w") as outfile:
                outfile.write(str(self.point.point_red))
        except OSError:
            print("Sorry, you can't save your score")

    def save_yellow_score(self):
        '''
        Method -- save the yellow player's score in the red scorefile
        Parameters:
            self -- the current object
        '''
       
        try:
            with open (self.yellow_scorefile, "w") as outfile:
                outfile.write(str(self.point.point_yellow))
        except OSError:
            print("Sorry, you can't save your score")

    def change_lst(self):
        '''
        Method -- change the list to the current situation list after
                  the player put their pieces in the chessboard
        Parameters:
            self -- the current object
        '''
        for i in range(self.ro):
            if self.lst[i][self.column_play_pick] == -1:
                self.lst[i][self.column_play_pick] = int(self.currentplayer)
                self.curr_ro = i
                self.curr_co = self.column_play_pick
                return True
        return False

    def horizontal(self):
        '''
        Method -- check if there is a 4-piece streak in a row
        Parameters:
            self -- the current object        
        '''
        count = 0
        for j in range(self.co):
            if self.lst[self.curr_ro][j] == self.currentplayer:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False

    def vertical(self):
        '''
        Method -- check if there is a 4-piece streak in a colunm
        Parameters:
            self -- the current object        
        '''
        count = 0
        for j in range(self.ro):
            if self.lst[j][self.curr_co] == self.currentplayer:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
        return False

    def diagonal(self):
        '''
        Method -- check if there is a 4-piece streak on a diagonal
        Parameters:
            self -- the current object        
        '''
        # check the diagonal in one direction
        count = 1
        ci,cj = self.curr_ro,self.curr_co
        while ci <= (self.ro -2) and cj <= (self.co - 2)  \
              and self.lst[ci+1][cj+1] == self.currentplayer:
            count += 1
            ci += 1
            cj += 1
        ci,cj = self.curr_ro,self.curr_co
        while 1 <= ci and 1 <= cj and self.lst[ci-1][cj-1] == self.currentplayer:
            count += 1
            ci -= 1
            cj -= 1
        if count >= 4:
            return True
        # check the diagonal in another direction
        count = 1
        ci,cj = self.curr_ro,self.curr_co
        while ci >= 1 and cj <= (self.co - 2) and \
              self.lst[ci-1][cj+1] == self.currentplayer:
            count += 1
            ci -= 1
            cj += 1
        ci,cj = self.curr_ro,self.curr_co
        while ci <= (self.ro -2) and cj >= 1 and self.lst[ci+1][cj-1] == self.currentplayer:
            count += 1
            ci += 1
            cj -= 1
        if count >= 4:
            return True     
        return False

    def is_full(self):
        '''
        Method -- check if the chessboard is full
        Parameters:
            self -- the current object
        '''
        for i in range(self.co):
            if self.lst[self.ro-1][i] == -1:
                return False
        return True


    def check_click(self, x, y):
        '''
        Method -- check whether the current player win the game
                  get the score and save the score in file
                  show the current player is red or yellow on the screen
        Parameters:
            self -- the current object
            x, y -- the x coordinate and y coordinate of the position
                    where the player click
        '''
        if self.chessboard.is_press_valid(x, y):
            self.column_play_pick = self.chessboard.find_column_of_button(x)
            if self.change_lst():
                self.chessboard.draw_new_piece(self.curr_ro, self.curr_co, \
                                               COLOR[self.currentplayer])
                if self.horizontal() or self.vertical() or self.diagonal():
                    print(COLOR[self.currentplayer]+" wins!")
                    if self.currentplayer == 1:
                         self.point.add_point_yellow()
                         self.save_yellow_score()
                    else:
                        self.point.add_point_red()
                        self.save_red_score()
                    self.chessboard.window.bye()
                    return True
                elif self.is_full():
                    print("the board is full. No one wins!")
                    self.chessboard.window.bye()
                    return True
                self.currentplayer = (self.currentplayer + 1) % 2
                return False
        return True
                  


    def launcher_phase1(self):
        '''
        Method -- the first several phase of the launcher
        Parameters:
            self -- the current object
        '''
        self.initialize_lst()
        self.point.initialie_point_red(self.red_scorefile)
        self.point.initialie_point_yellow(self.yellow_scorefile)
        self.chessboard.draw_all_board()
        self.chessboard.draw_score(self.point.point_red,self.point.point_yellow)
          
    def launcher_manvsman(self):
        '''
        Method -- the process in man vs man game
        Parameters:
            self -- the current object
        '''
        self.launcher_phase1()
        def click(x,y):
            if self.check_click(x, y):
                return
            self.chessboard.draw_turn(self.currentplayer)
            
        self.chessboard.draw_turn(self.currentplayer)                     
        self.chessboard.window.onclick(click)

    def launcher_manvscomputer(self):
        '''
        Method -- the process in man vs computer game
        Parameters:
            self -- the current object
        '''
        self.launcher_phase1()
        self.chessboard.draw_turn_mvc(self.currentplayer)
        def click(x, y):
            if self.check_click(x, y):
                return
            self.chessboard.draw_turn_mvc(self.currentplayer)
            #computer's turn
            valid_column_list = []
            # find out which colunms are valid for the computer
            for i in range(self.co):
                if self.lst[self.ro-1][i] == -1:
                    valid_column_list.append(i)
            self.column_play_pick = valid_column_list[random.randint(0,len(valid_column_list)-1)]
            if self.change_lst():
                self.chessboard.draw_new_piece(self.curr_ro, self.curr_co, COLOR[self.currentplayer])
                if self.horizontal() or self.vertical() or self.diagonal():
                    print("Computer wins!")
                    if self.currentplayer:
                        self.point.add_point_yellow()
                        self.save_yellow_score()
                    else:
                        self.point.add_point_red()
                        self.save_red_score()
                    self.chessboard.window.bye()
                    return
                elif self.is_full():
                    print("the board is full. No one wins!")
                    self.chessboard.window.bye()
                    return
                self.currentplayer = (self.currentplayer + 1) % 2
                self.chessboard.draw_turn_mvc(self.currentplayer)

        self.chessboard.window.onclick(click)
                                    
               
        
        
                        
        
        
        
            
            
            
                    
                    
            
            
        
        
                    
