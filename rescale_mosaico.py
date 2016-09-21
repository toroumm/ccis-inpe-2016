


import numpy as np
import cv2,os,sys

path_file = '/home/jeferson/MEGA/IEAv/imagens_mosaico/'


classes =12

label = [];

for i in xrange(0, classes):

    path_current = path_file+'frames/positive/'+str(i+1)+'/'

    list_img = os.listdir(path_current)


    for j in  xrange(0, len(list_img)):
        #img = cv2.imread(path_current+list_img[j])
        k = 0.1
        for kk in xrange(1,9):

            
            up = cv2.resize(img, (int(img.shape[0]*(1+k)), int(img.shape[0]*(1+k))))
            down = cv2.resize(img, (int(img.shape[0] * (1 - k)), int(img.shape[0] * (1 - k))))

            ss = cv2.resize(img, (int(img.shape[0] * (1 + k)), int(img.shape[0] * (1 - k))))
            aa = cv2.resize(img, (int(img.shape[0] * (1 - k)), int(img.shape[0] * (1 + k))))

            k+=0.1

            cv2.imwrite(path_file + 'rescale/' + str(i+1) + "_" + list_img[j] + '_' + str(kk) + '_0.png', img)
            cv2.imwrite(path_file + 'rescale/' + str(i+1) + "_" + list_img[j] + '_' + str(kk) + '_1.png', up)
            cv2.imwrite(path_file + 'rescale/' + str(i+1) + "_" + list_img[j] + '_' + str(kk) + '_2.png', down)
            cv2.imwrite(path_file + 'rescale/' + str(i+1) + "_" + list_img[j] + '_' + str(kk) + '_3.png', ss)
            cv2.imwrite(path_file + 'rescale/' + str(i+1) + "_" + list_img[j] + '_' + str(kk) + '_4.png', aa)

            label.append((i + 1))
            label.append((i + 1))
            label.append((i + 1))
            label.append((i + 1))
            label.append((i + 1))

            #print ss.shape, aa.shape, up.shape, down.shape


np.savetxt('/home/jeferson/Desktop/label',np.asarray(label))