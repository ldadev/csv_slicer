import pandas as pd

class slicer:

	def _init__ (self,source_file,cut_lenght):

		self.source_file =  pd.read_csv('csv_files/test_file.csv')
		self.cut_lenght = cut_lenght
		







