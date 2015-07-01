import time

from functools import wraps

def calculate_runtime(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		start = time.time()
		f(*args, **kwargs)
		stop = time.time()

		return stop - start

	return wrapper
