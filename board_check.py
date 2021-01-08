import numpy as np
import csv


def check_squares(squares):
	for square in squares:
	    values = square[square > 0]
	    unique_values, counts = np.unique(values, return_counts=True)
	    duplicates = unique_values[counts > 1]
	    if duplicates.size:
	        for duplicate in duplicates:
	            index = np.where(square == duplicate)
	            square[index] = 0


def check_columns(board):
	columns = np.transpose(board)
	for column in columns:
	    values = column[column > 0]
	    unique_values, counts = np.unique(values, return_counts=True)
	    duplicates = unique_values[counts > 1]
	    if duplicates.size:
	        for duplicate in duplicates:
	            index = np.where(column == duplicate)
	            column[index] = 0


def check_rows(board):
	for row in board:
	    values = row[row > 0]
	    unique_values, counts = np.unique(values, return_counts=True)
	    duplicates = unique_values[counts > 1]
	    if duplicates.size:
	        for duplicate in duplicates:
	            index = np.where(row == duplicate)
	            row[index] = 0


if __name__ == '__main__':
	generate_random_board()