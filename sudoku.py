## This file describes and controls the Sudoku game logic.

from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
from board_check import check_squares, check_columns, check_rows
import numpy as np
import csv


BOARD_SETTINGS = ['debug', 'easy', 'medium', 'hard', 'insane', 'error']
MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9
board_fname = generate_random_board()
board_file = np.loadtxt(board_fname, delimiter=' ')


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
		nine_by_nine = np.repeat([np.arange(1, 10)], 9, axis=0)
		flat = nine_by_nine.ravel()
		np.random.shuffle(flat)
		squares = flat.reshape(9, 3, 3)
		mask = np.random.randint(0, 2, size=squares.shape).astype(np.bool)
		random_zeros = np.random.rand(*squares.shape)*0
		squares[mask] = random_zeros[mask]
		check_squares(squares)
		first_square_row = np.hstack(squares[:3])
		second_square_row = np.hstack(squares[3:6])
		third_square_row = np.hstack(squares[6:])
		board_by_rows = np.vstack((
								first_square_row, 
								second_square_row, 
								third_square_row
							 ))
		check_rows(board_by_rows)
		check_columns(board_by_rows)
		with open('sudoku.board', 'w') as boardfile:
			board_writer = csv.writer(boardfile, delimiter=" ")
			for row in board_by_rows:
				board_writer.writerow(row)
		return board
	

class SudokuUI(Frame):
	def __init__(self):
		pass


class SudokuSolver(object):
	def __init__(self):
		pass