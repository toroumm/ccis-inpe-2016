

from anns.som import SOM



import numpy as np
import cv2, os, sys, pickle




def list_files(list_dir,extension, size_extension):
    net = []
    full = os.listdir(list_dir)
    for i in xrange(0, len(full)):
        if(full[i][-size_extension:] == extension):
            net.append(full[i])

    return net

path = '/home/jeferson/MEGA/IEAv/imagens_mosaico/'

path_net = path+'nets/som/'

path_database = path+'database/lbp/'

path_save_result = path+'results/som/'

mosaico = cv2.imread(path+'univap-final_transparent_mosaic_COM-APOIO.tif')

nets_files = list_files(path_net, 'pk1', 3)

base = '16_1_8.txt'

data_teste = np.loadtxt(path_database+base)

data_base = np.loadtxt(path_database+'mosaico_completo_'+base[:-4]+'_300_100.txt')

size = 300
shift = 100

lista_treino =[]
lista_teste = []
ll =0
for net in nets_files:

    img = np.copy(mosaico)

    if(base in net):

        s = SOM.load_map(path_net+net)

        print s, path_net+net

        pred_teste = s.predict(data_teste)

        bins = np.unique(pred_teste)

        pred_img = s.predict(data_base)

        a1,b1 = np.histogram(pred_teste,bins=50)
        a2,b2 = np.histogram(pred_img,bins=50)

        lista_treino.append(a1)
        lista_teste.append(a2)
        #print np.histogram(pred_teste)
        #print np.unique(pred_img), len(np.unique(pred_img))

        k=0

        for i in xrange(0, img.shape[0],shift):

            for j in xrange(0, img.shape[1],shift):

                    #asd = img[i:i+size,j:j+size]

                    #cv2.imshow('img',asd)

                    #cv2.waitKey(3)

                if(pred_img[k] in bins):

                    img[i:i+size, j:j+size] =  (100,100,100)

                k+=1
                if(k > pred_img.shape[0]):
                    break


        img = cv2.resize(img,(1000,1000))

        cv2.imwrite(path_save_result+net[:-3]+'png',img)

        #sys.exit()

np.savetxt(path_save_result+'metadata/hists_treino_'+base,np.asarray(lista_treino))

np.savetxt(path_save_result+'metadata/hists_teste_'+base,np.asarray(lista_teste))
