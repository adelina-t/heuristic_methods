import sys
import utils

from data import Data

best_solution = {'weight': 0,
				 'value': 0,
				 'objects': []
				}

data_set = None

array = []

def clear_array():
	global array
	array = []

def init_array(solution_size):
	global array
	array = [0] * solution_size

def ok(pozition):
	for i in xrange(pozition):
		for j in xrange(i+1, pozition+1):
			if array[i] == array[j]:
				return False
	weight = sum([data_set.obj_weights[x] for x in array[:pozition]])
	# asta e posibil sa nu mearga, check
	if weight > data_set.kweight:
		return False

	return True

def save_if_best(solution_size):
	global best_solution
	value = sum([data_set.obj_values[x] for x in array])
	weight = sum([data_set.obj_weights[x] for x in array])
	if value > best_solution['value'] and weight <= data_set.kweight:
		best_solution= {'value': value,
					    'weight': weight,
					    'objects': array[:]}
	#aici trebuie verificat si daca sunt egale and so on

def _backtrack(pozition, solution_size):
	global array
	start = 0
	if pozition != 0:
		start = array[pozition - 1] + 1 
	for value in xrange(start,data_set.no_objects):
		array[pozition] = value
		if ok(pozition):
			if pozition == solution_size - 1:
				save_if_best(solution_size)
			else:
				_backtrack(pozition + 1, solution_size)

@utils.calculate_runtime
def backtrack(data_file):
	global data_set
	data_set = Data()
	data_set.populate_from_file(data_file)
	clear_array()
	for size in xrange(1, data_set.no_objects + 1):
		init_array(size)
		_backtrack(0, size)
	return best_solution
