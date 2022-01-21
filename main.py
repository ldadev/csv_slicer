from cutter import slicers

if __name__== "__main__":

	slicer = slicers(100)

	for cutting_interval in range(1,slicer.num_records +50,slicer.cut_lenght):
		
		if (cutting_interval > slicer.cut_lenght) and cutting_interval <= slicer.num_records +50:

			initial_cut = cutting_interval - (slicer.cut_lenght)
			end_cut  = cutting_interval
			if end_cut > slicer.num_records:
				slicer.segment_file(initial_cut + 1,slicer.num_records)
			else:
				slicer.segment_file(initial_cut,end_cut)






