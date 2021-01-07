## This file describes and controls the Sudoku game logic.

import tkinter

BOARD_SETTINGS = ['debug', 'easy', 'medium', 'hard', 'insane', 'error']
MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

class SudokuError(Exception):
	"""A game specific error"""
	pass

class SudokuGame(object):
	def __init__(self, board_file):
		

class SudokuBoard(object):
	"""The Sudoku game board"""
	def __init__(self, board_file):
		self.board = board_file

	def __create_board(self, board_file):
		# Need to create a 9x9 matrix with NumPy that can be modified based on difficulty.

		# board = [line.strip() for line in board_file if len(line) == 9]
		# if len(board) < 9:
		# 	board = []
		# 	raise SudokuError("Each line must have a length of 9.")
		
		# board = []

		# for line in board_file:
		# 	line = line.strip()

		# 	if len(line) != 9:
		# 		board = []
		# 		raise SudokuError("Each line must have a length of 9.")

		# 	board.append([])

		# 	for c in line:
		# 		if not c.isdigit():
		# 			raise SudokuError("Valid characters must be 0-9.")

		# 	board[-1].append(int(c))

		# if len(board) != 9:
		# 	raise SudokuError("Each puzzle must be 9x9.")

		# return board
		

class SudokuSolver(object):
	def __init__(self):
		pass