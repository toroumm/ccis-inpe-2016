



import cv2
import numpy as np
import os
import sys


import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from anns.som import SOM


def etc():
	path_file = '/home/jeferson/MEGA/IEAv/imagens_mosaico/'

	files = [16,32,64,128,256]
	epochs = [100,500,1000]

	bins = 50
	testes = 5

	for _file in files:

		full_file = str(_file)+'_1_8.txt'
		case = np.loadtxt(path_file + 'database/lbp/' + full_file )

		for ii in epochs:

			for i in xrange(0,testes):

				print _file, ii, i

				str_file = path_file+'nets/som/'+'teste_novo_'+full_file+'_'+str(bins)+'_'+str(ii)+'_'+str(i+1)

				a  = SOM(bins,case.shape[1])
	
				a.train_som(case,ii)

				result = a.predict(case)

				a.save_map(a,str_file)

				plt.hist(result,bins)

				plt.xlabel('Neurons')

				plt.ylabel('Hits')

				plt.title('Grid SOM')

				plt.grid(True)
		
				pp = PdfPages(str_file)

				plt.savefig(pp, format='pdf')

				pp.close()
	
			plt.cla()

			plt.clf()

			plt.close()


def make_result(net_file, lbp_file_geral, lbp_file_mark, img_file):

	net = SOM.load_map(net_file)

	data_geral = np.loadtxt(lbp_file_geral)
	
	data_mark = np.loadtxt(lbp_file_mark)

	img = cv2.imread(img_file)	

#///////////////////////////////////////////////////////////////////////////////////////////////////

etc()

sys.exit()

path_file = '/home/jeferson/MEGA/IEAv/imagens_mosaico/'

_file = '16_1_8.txt'

bins =50
epochs = 100
testes = 5
window = 300
shift = 100

for i in xrange(0,testes):

	net_file = path_file+'nets/som/som_'+_file+'_'+str(bins)+'_'+str(epochs)+'_'+str(i)+'.pk1'

	lbp_file_geral = path_file+'database/lbp/mosaico_completo_'+_file[:-4]+'_'+str(window)+'_'+str(shift)+'.txt'

	lbp_file_mark = path_file+'database/lbp/'+_file

	img_file = path_file+'univap-final_transparent_mosaic_COM-APOIO.tif'

	
	
	


