'''Ke Yang
   cs5001
   Project
   April 1st
'''


class Point:
    '''Class Point
       Attributes: point_red, point_yellow
       Methods: add_point_red, add_point_yellow, add_point_yellow
                initialie_point_red, initialie_point_yellow
    '''
    def __init__(self):
        '''
        Constructor -- creates new instance of point
        Parameters:
            self -- the current object
        '''        
        self.point_red = 0
        self.point_yellow = 0

    def add_point_red(self):
        '''
        Method -- red player add one point
        Parameters:
            self -- the current object
        '''
        self.point_red += 1

    def add_point_yellow(self):
        '''
        Method -- yellow player add one point
        Parameters:
            self -- the current object
        '''
        self.point_yellow += 1

    def initialie_point_red(self, filename):
        '''
        Method -- get the red player's point as an int in a file
        Parameters:
            self -- the current object
            filename -- the name of the red score file
        '''
        try:
            with open (filename, "r") as infile:
                information = infile.read()
                if not information:
                    self.point_red = 0
                else:
                    self.point_red = int(information)
        except OSError:
            self.point_red = 0

    def initialie_point_yellow(self, filename):
        '''
        Method -- get the red player's point as an int in a file
        Parameters:
            self -- the current object
            filename -- the name of the yellow score file
        '''
        try:
            with open (filename, "r") as infile:
                information = infile.read()
                if not information:
                    self.point_yellow = 0
                else:
                    self.point_yellow = int(information)
        except OSError:
            self.point_yellow = 0
       


                    
            
