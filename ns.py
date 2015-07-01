import random
import sys
import utils

from data import Data

data_set = None

def generate_initial_sol(max_size):
	array = []
	for i in xrange(max_size):
		array.append(random.choice([True, False]))

	return array

def generate_neighborhood_max(solution):
	neighborhood_max = 0
	neighborhood_max_sol = solution

	for i in xrange(len(solution)):
		new_sol = transform(solution, i)

		objects = [x for x in xrange(data_set.no_objects) if solution[x] is True]
		value = sum([data_set.obj_values[x] for x in objects])
		weight = sum([data_set.obj_weights[x] for x in objects])

		if value > neighborhood_max and weight < data_set.kweight:
			neighborhood_max = value
			neighborhood_max_sol = new_sol
	return neighborhood_max_sol


def transform(solution, poz):
	transformed_solution = solution[:]
	transformed_solution[poz] = not transformed_solution[poz]

	return transformed_solution

def _nsearch():
	sol = generate_initial_sol(data_set.no_objects)
	value = sum([data_set.obj_values[x] for x in xrange(data_set.no_objects) if sol[x] is True])
	weight = sum([data_set.obj_weights[x] for x in xrange(data_set.no_objects) if sol[x] is True])
	objects = [x for x in xrange(data_set.no_objects) if sol[x] is True]
	best_sol = {'weight': weight,
				'value': value,
				'objects': objects
			   }

	while True:
		new_sol = generate_neighborhood_max(sol)

		value = sum([data_set.obj_values[x] for x in xrange(data_set.no_objects) if new_sol[x] is True])

		if value > best_sol['value']:
			weight = sum([data_set.obj_weights[x] for x in xrange(data_set.no_objects) if new_sol[x] is True])
			best_sol['weight'] = weight
			best_sol['value'] = value
			best_sol['objects'] = objects
			sol = new_sol
		else:
			return best_sol

@utils.calculate_runtime
def nsearch(data_file):
	global data_set
	data_set = Data()
	data_set.populate_from_file(data_file)
	return _nsearch()

best_sol, run_time = nsearch(r'.\data_sets\data_set_100')

print best_sol, run_time
