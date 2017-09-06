#use a function to create a board
def play_board(board):
	print'   |   |'
	print' ' + board[7] + ' | ' + board[8] +' | ' + board[9]
	print'   |   |'
	print'-----------'
      	print'   |   |'
	print' ' + board[4] + ' | ' + board[5] + ' | ' + board[4]
	print'   |   |'
	print'------------'
	print'   |   |'
	print' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]
	print'   |   |'

board=['X']*10
print'This is the  outlook ot the board'
play_board(board)

#function to take the players input from the key board
def player_choice():
	choice=''
	while not(choice =='O' or choice =='X'):
		choice=raw_input('Do you want to use "X" or "O" to play the game? ')
		choice=choice.upper()

	if choice == 'X':
		return('X','O')
	else:
		return('O','X')

#function call
#player_choice()

#function that takes the boards position n fills it with players choice
def place_choice(board,choice,position):
	board[position]=choice

#function to take in a board n input n checks if the  input matches a win in the game
def triump_check(board,inpt):
	return((board[7]==inpt and board[8]==inpt and board[9]==inpt) or #topsde
		(board[4]==inpt and board[5]==inpt and board[6]==inpt) or #middle
		(board[1]==inpt and board[2]==inpt and board[1]==inpt) or #downside
		(board[1]==inpt and board[5]==inpt and board[9]==inpt) or #leftright diag
		(board[3]==inpt and board[5]==inpt and board[7]==inpt) or  #rightleft diag
		(board[7]==inpt and board[4]==inpt and board[1]==inpt) or #left top down
		(board[8]==inpt and board[5]==inpt and board[2]==inpt) or #middle top down
		(board[9]==inpt and board[6]==inpt and board[3]==inpt)) #right top down

#using The Random function  toh decide which player starts the  game first
import random
def play_first():
	if random.randint(0,1)==0:
		return 'Player 1 starts now!'
	else:
		return 'Player 2 starts now!'

#play_first()

#fuction that replys if space on board is available
def chk_position(board,position):
	return board[position] == ' '

#checking if the board is full
def bod_full(board):
	for i in range(1,10):
		if chk_position(board,i):
			return False
	return True

#function to check the players choice
def playerchoice(board):

	position=' '

	while position not in '1 2 3 4 5 6 7 8 9'.split() or not chk_position(board,int(position)):
		position=raw_input('Enter your next position btw 1-9: ')
	return int(position)
#function to query the user if he wants to play again
def replay():
	print raw_input('Do you wish to play again? yes or no ').lower().startswith('y')

#games main code

print('Welcome to TIC_TAC_TOE')

while True:
	the_board=[' ']*10
	player1choice , player2choice = player_choice()
	play_turn=play_first()
	print play_turn ,'Will play now!'

	gameon=True

	while gameon:
#player 1 turn
		if play_turn=="Player 1 starts now!":

			play_board(the_board)
			position=playerchoice(the_board)
			place_choice(the_board,player1choice,position)

			if triump_check(the_board,player1choice):
				play_board(the_board)
				print'Congratz player 1 gets 10 points'
				gameon= False

			else:
				if bod_full(the_board):
					play_board(the_board)
					print'The game is a DRAW!'
					break
				else:
					play_turn='Player 2 starts now!'

#player 2 turn
		else :
			play_board(the_board)
			position=playerchoice(the_board)
			place_choice(the_board,player2choice,position)

                        if triump_check(the_board,player2choice):
                                play_board(the_board)
                                print'Congratz player 2 gets 10 points'
                                gameon= False

                        else:
                                if bod_full(the_board):
                                        play_board(the_board)
                                        print'The game is a DRAW!'
                                        break
                                else:
                                        play_turn='Player 1 starts now!'

	if not replay():
		break
