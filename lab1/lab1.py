def game_selection():
	while True:
		print("To play checkers enter 1\nTo play international draughts enter 2 \
nTo play checkers with pieces enter 3\nEnter 4 to quit")
		x = int(input())
		if x == 1:
			main_checkers()
		elif x == 2:
			main_international_draughts()
		elif x == 3:
			main_checkers_pieces()
		elif x == 4:
			break
def print_checker_boundary_row():
	'''Prints out a row of characters representing the border between two rows of
spaces'''
	print("+-+-+-+-+-+-+-+-+")
	'''prints out a row of pipes representing the spaces between rows'''
def print_checker_space_row():
	print("| | | | | | | | |")
	'''main function for if checkers is chosen'''
def main_checkers():
	'''Tests for the functions'''
	print('Running the tests...')
	for i in range(7):
		print_checker_boundary_row()
		print_checker_space_row()
	print_checker_boundary_row()
def print_draughts_boundary_row():
	print("+-+-+-+-+-+-+-+-+-+-+")
def print_draughts_space_row():
	print("| | | | | | | | | | |")
def main_international_draughts():
for i in range(9):
	print_draughts_boundary_row()
	print_draughts_space_row()
print_draughts_boundary_row()
def x_pieces_1():
	print("|x| |x| |x| |x| |")
def x_pieces_2():
	print("| |x| |x| |x| |x|")
def y_pieces_1():
	print("|o| |o| |o| |o| |")
def y_pieces_2():
	print("| |o| |o| |o| |o|")
def main_checkers_pieces():
	x_pieces_2()
	x_pieces_1()
	x_pieces_2()
	for i in range(2):
		print_checker_space_row()
	y_pieces_1()
	y_pieces_2()
	y_pieces_1()
game_selection()
