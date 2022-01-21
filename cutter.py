import pandas as pd

class slicers:

	def __init__ (self,cut_lenght):

		self.source_file =  pd.read_csv('csv_files/test_file.csv')# Fuente del archivo csv
		self.num_records = self.source_file.shape[0] #Total de registros
		self.cut_lenght = cut_lenght # Ancho del corte


	def __str__(self):

		print(self.source_file,self.num_records,self.cut_lenght)


	
	def segment_file(self,initial_cut,end_cut):

		self.initial_cut = initial_cut
		self.end_cut = end_cut

		end_segment = self.source_file[int(initial_cut):int(end_cut)]

		msg = 'output_files/' + f'Segment {initial_cut} to {end_cut}'
		end_segment.to_csv(msg + '.csv',index=False) # Guardamos los reccortes

























