import random

class Data(object):

	def populate_from_file(self, file_path):
		try:
			f = open(file_path)
			self.kweight = int(f.readline())
			self.no_objects = int(f.readline())
			self.obj_weights = [int(x) for x in f.readline().split()]
			self.obj_values = [int(x) for x in f.readline().split()]
		except IOError as e:
			print "Cannot open %s." % file_path
			raise e

	def __repr__(self):
		return "Weight: %s \nNo. of obj: %s \nObject weights %s \n" \
			   "Object values %s \n" \
			   % (self.kweight, self.no_objects,
			   	  self.obj_weights, self.obj_values)

	def __str__(self):
		return self.__repr__()

	@staticmethod
	def generate_data_to_file(size):
		file_path = "data_sample_%s" % size
		f = open(file_path, 'w')

		random.seed()
		f.write(str(random.randint(size * 50 ,size * 100)) + "\n")
		f.write(str(size) + "\n")
		
		array = ""
		for x in xrange(size):
			array = array + "%s " % (random.randint(60,120))
		f.write(array + "\n")
		array = ""
		for x in xrange(size):
			array = array + "%s " % (random.randint(1,100))
		f.write(array + "\n")
