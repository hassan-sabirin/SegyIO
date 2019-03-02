import segyio
import numpy as np
for i in range(1,17):
	if i in [7,15,4,13,14]: # skip formats unknown/unhandled
		continue
	for endian in ['msb','lsb']:
		with segyio.open( 'test-data/Format%d%s.sgy' % (i,endian)) as src:
			for j,t in enumerate(src.trace[0]):
				print('Format',i,endian, 'Trace%d:' % j,t)
		print('')
