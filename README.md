# connect-four-gameboard
Bullet-point summary:

1.	Class: Point
   	Attributes:    point_red(the score of the red player)
			point_yellow(the score of the yellow player)

	Methods:       add_point_red (red player add one point)
			add_point_yellow (yellow player add one point)
			initialie_point_red(get the red player's point 
					     as an int in a red score file)
			initialie_point_yellow(get the yellow player's point as 
						an int in a yellow score file)



	

	Class: Chessboard
	Attributes:	window (set up the screen)
			num_column (the number of columns the player input)
			num_row (the number of rows the player input)
			pieces(a turtle that draw the pieces)
			pieces.hideturtle() (hide the pieces turtle)
			triangle (a turtle that draw the triangle button)
			triangle.hideturtle() (hide the triangle turtle)
                   	big_board (a turtle that draw the big board)
			big_board.hideturtle() (hide the big_board turtle)
			turn (a turtle that draw to show the current player)
			turn.hideturtle()(hide the turn turtle)
                   	button_loc_x (the x coordinate of the button to draw)
			button_loc_y (the y coordinate of the button to draw)
			board_loc_x (the x coordinate of the first circle on 
				      the board to draw, a constant)
			board_loc_y (the y coordinate of the first circle on 
				      the board to draw, a constant)
	
	Methods:	draw_score (show the current score of red and yellow player)
			draw_turn (show the current player is red or yellow 
				       in man vs man game)
			draw_turn_mvc (show the current paly is player or computer 
                                     in man vs computer game) 
			draw_circle (draw the circle in the chessboard)
                	draw_triangle (draw the triangle as the user button in the chessboard)
			draw_board (draw the whole board) 
			draw_all_board (draw all the board and the triangle as the player button)
			is_press_valid (check if the player click on the button (the triangle))
                	find_column_of_button (check which column the player click) 
			draw_new_piece (draw a new circle where the player put their 
					 pieces on in the player's color

	

	Class: Game
	Attributes:	point (the Class Point)
			co (the number of columns the player input) 
			ro (the number of rows the player input) 
			currentplayer (which color the current player is, 0 for red, 1 for yellow) 
			curr_ro (which row the current player put his piece at) 
			curr_co (which column the current player put his piece at) 
                   	red_scorefile (the file that write the red player???s score) 
			yellow_scorefile (the file that write the yellow player???s score) 
			column_play_pick (which column the player put his piece at)
                   	lst (the list to show the current board, 0 for red, 1 for yellow, -1 for empty
    			     an empty list at first)
	
	Methods:	init_chessboard (initialize Chessboard)  
			initialize_lst (get the origianl list to present the pieces in chessboard,
                  			 0 for red, 1 for yellow, -1 for empty)
			save_red_score (save the red player's score in the red scorefile)
                	save_yellow_score (save the yellow player's score in the red scorefile)
			change_lst (change the list to the current situation list after
                  		    the player put their pieces in the chessboard) 
			horizontal (check if there is a 4-piece streak in a row) 
			vertical (check if there is a 4-piece streak in a colunm)
                	diagonal (check if there is a 4-piece streak on a diagonal) 
			is_full (check if the chessboard is full) 
			check_click (check whether the current player win the game
                  		      get the score and save the score in file
                  	  	      show the current player is red or yellow on the screen)
			launcher_phase1 (the first several phase of the launcher)
                	launcher_manvsman (the process in man vs man game) 
			launcher_manvscomputer (the process in man vs computer game)

2.	data structures :
	integers, floats, boolean, string, list, tuple, file

3.	non_class fiction:
	input_size()
	check the columns and rows the play input is valid and reasonable


some that can???t be unit-tested



I input the number of columns and rows in many numbers like 2 * 2, 2 * 3, 3 * 3, 3 * 4 and so on.
In every time, the whole chess board, the button for player on above the board as triangle,
the information about the turn of the player and the current score of the red and yellow player is shown correctly in the screen. 
So the  method raw_score, draw_turn, draw_turn_mvc, draw_circle, 
draw_triangle, draw_board, draw_all_board are all correct.

In every time, I click on other places in the screen besides the triangle buttons for many times,
nothing happened, so method is_press_valid is correct.

In every time, no matter in man vs man game or in man vs computer game,
I click the button in which column the piece is valid, it always showed in the right column 
and in right color, so method find_column_of_button, draw_new_piece are tested. Also, check_click, launcher_phase1, launcher_manvsman and launcher_manvscomputer are correct.

In every time, I click to let one of the column have no place to a new piece and nothing happen, the player
has to chose another column, so method is_full is correct. 

In every time, I try to let one of the player win for many times, once there is a 4-piece streak in a row or 
in a column or in a diagonal, the game is over, so method horizontal, vertical and diagonal are correct.

In every time, in 2 * 2, 2 * 3 and many chessboard smaller than 4 * 4
I try to get the whole chessboard full but no one wins, the game is over but one wins the game,
so the method change_lst is correct.

Every game no matter man vs man or man vs computer, we get the right winner and right score,
so the method check_click, launcher_phase1, launcher_manvsman, launcher_manvscomputer are correct.

