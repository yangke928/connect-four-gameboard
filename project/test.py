'''
    Ke Yang
    CS5001
    Project
    test code
    April 1st

    Here we inherit from the unittest.TestCase class
    so we have access to its attributes and methods
'''
import unittest
import os
from chessboard import*
from game import *
from point import *

class PointTest(unittest.TestCase):
    def test_init(self):
        c = Point()
        self.assertEqual(c.point_red, 0)
        self.assertEqual(c.point_yellow, 0)

    def test_score(self):
        c = Point()
        # Add one point, go from zero to 1
        c.add_point_red()
        c.add_point_yellow()
        self.assertEqual(c.point_red, 1)
        self.assertEqual(c.point_yellow, 1)

        # Initialize score from file with a non-
        # existent file; score goes back to zero

        if os.path.exists('nofilered.txt'):
            os.remove('nofilered.txt')
        c.initialie_point_red('nofilered.txt')
        self.assertEqual(c.point_red, 0)

        if os.path.exists('nofileyellow.txt'):
            os.remove('nofileyellow.txt')
        c.initialie_point_yellow('nofileyellow.txt')
        self.assertEqual(c.point_yellow, 0)

        # Initialize score from file with a score of
        # 10
        with open('testscorered.txt', 'w') as outfile:
            outfile.write('10')
        c.initialie_point_red('testscorered.txt')
        self.assertEqual(c.point_red, 10)
        os.remove('testscorered.txt')

        with open('testscoreyellow.txt', 'w') as outfile:
            outfile.write('10')
        c.initialie_point_yellow('testscoreyellow.txt')
        self.assertEqual(c.point_yellow, 10)
        os.remove('testscoreyellow.txt')

        
        
class GameTest(unittest.TestCase):
    def test_init(self):
        g = Game('noredscore.txt', 'noyellowscore.txt', 7, 6)
        self.assertEqual(g.co, 7)
        self.assertEqual(g.ro, 6)
        self.assertEqual(g.currentplayer, 0)
        self.assertEqual(g.curr_ro, 0)
        self.assertEqual(g.curr_co, 0)
        self.assertEqual(g.red_scorefile, 'noredscore.txt')
        self.assertEqual(g.yellow_scorefile, 'noyellowscore.txt')
        self.assertEqual(g.column_play_pick, 0)
        self.assertEqual(g.lst, [])

    def test_lst(self):
        # test the list when the player input 2 columns and 2 rows
        g = Game('noredscore.txt', 'noyellowscore.txt', 2,2 )
        g.initialize_lst()
        self.assertEqual(g.lst, [[-1,-1],[-1,-1]])
        # test the list when the player input 3 columns and 3 rows
        h = Game('noredscore.txt', 'noyellowscore.txt', 3,3 )
        h.initialize_lst()
        self.assertEqual(h.lst, [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]])
        # test the list when the player input 3 columns and 2 rows
        m = Game('noredscore.txt', 'noyellowscore.txt', 3,2 )
        m.initialize_lst()
        self.assertEqual(m.lst, [[-1,-1,-1],[-1,-1,-1]])
        # test the list when the player input 2 columns and 3 rows
        n = Game('noredscore.txt', 'noyellowscore.txt', 2,3 )
        n.initialize_lst()
        self.assertEqual(n.lst, [[-1,-1],[-1,-1],[-1,-1]])

    def test_save_score(self):
        g = Game('noredscore.txt', 'noyellowscore.txt', 2,2 )
        # check that the function creates the expected red score
        # file contents.
        g.save_red_score()
        with open ('noredscore.txt', 'r') as infile:
            information_red = infile.read()
        self.assertEqual(str(g.point.point_red), information_red)

        # check that the function creates the expected yellow score
        # file contents.
        g.save_yellow_score()
        with open ('noyellowscore.txt', 'r') as infile:
            information_yellow = infile.read()    
        self.assertEqual(str(g.point.point_yellow), information_yellow)

    def test_change_lst(self):
        # check when the player input 2 columns and 2 rows
        # the column player picked is 0 as in the attribute
        x = Game('noredscore.txt', 'noyellowscore.txt', 2,2 )
        x.initialize_lst()
        x.change_lst()
        self.assertEqual(x.lst, [[0,-1],[-1,-1]])

        # check when the player input 2 columns and s rows
        # the column player picked is 1 as in the attribute
        y = Game('noredscore.txt', 'noyellowscore.txt', 2,3 )
        y.initialize_lst()
        y.column_play_pick = 1
        y.change_lst()
        self.assertEqual(y.lst, [[-1,0],[-1,-1],[-1,-1]])

        # check when the player input 3 columns and 2 rows
        # the column player picked is 2 as in the attribute
        z = Game('noredscore.txt', 'noyellowscore.txt', 3,2 )
        z.initialize_lst()
        z.column_play_pick = 2 
        z.change_lst()
        self.assertEqual(z.lst, [[-1,-1,0],[-1,-1,-1]])


    def test_is_full(self):
        # check when the player input 2 columns and 2 rows
        # the list is [[0,0],[0,0]]
        g = Game('noredscore.txt', 'noyellowscore.txt', 2,2 )
        g.lst = [[0,0],[0,0]]
        result = g.is_full()
        self.assertEqual(result, True)
        # check when the player input 2 columns and 2 rows
        # the list is [[0,0],[-1,0]]
        g = Game('noredscore.txt', 'noyellowscore.txt', 2,2 )
        g.lst = [[0,0],[-1,0]]
        result = g.is_full()
        self.assertEqual(result, False)

        # check when the player input 3 columns and 3 rows
        # the list is [[0,0,0],[0,0,0],[-1,0,0]]
        g = Game('noredscore.txt', 'noyellowscore.txt', 3,3 )
        g.lst = [[0,0,0],[0,0,0],[-1,0,0]]
        result = g.is_full()
        self.assertEqual(result, False)


class ChessboardTest(unittest.TestCase):
    def test_init(self):
        s = Chessboard(7, 6)
        s.num_colunm = 7
        s.num_row = 6
        s.button_loc_x = 0
        s.button_loc_y = 0
        s.board_loc_x = -150
        s.board_loc_y = -145
        
def main():
    unittest.main(verbosity = 3)

main()
        

        
        
        

        

        
        
