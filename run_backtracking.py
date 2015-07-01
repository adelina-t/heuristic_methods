import backtracking
import data
import os


if __name__ == '__main__':
	for size in [8,10,15]:
			file_path = "data_set_%s" % (size)
			file_path = os.path.join("data_sets", file_path)

			best_sol, run_time = backtracking.backtrack(file_path)
			print "LOG problem size: %s run_time %s" % (size, run_time)
