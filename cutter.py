import pandas as pd

class slicers:

	def __init__ (self,cut_lenght):

		self.source_file =  pd.read_csv('csv_files/test_file.csv')
		self.cut_lenght = cut_lenght



	def __str__(self):

		print(f'Logitud del corte {self.cut_lenght} y archivo fuente \n {self.source_file.head}')













