import numpy as np
import cv2, os,sys

def retangulo(event, x,y , flags, param):

    global xx, yy, press, img, fract_img, aux, pattern, number_image

    if event == cv2.EVENT_LBUTTONDOWN:
            print 'LBUTTON'
            #img = aux.copy()
            xx,yy = x,y
            press = True

    elif event == cv2.EVENT_MOUSEMOVE:

        if(press):
            print x, y, xx, yy
            fract_img = aux.copy()
            cv2.rectangle(fract_img,(xx,yy),(x,y), (0,0,200), 1)

    elif event ==cv2.EVENT_LBUTTONUP:
        fract_img = aux.copy()
        cv2.rectangle(fract_img, (xx, yy), (x, y), (0, 0, 200), 1)
        pattern = cv2.cvtColor(fract_img[yy:y,xx:x],cv2.COLOR_BGR2GRAY)
        number_image += 1
        xx, yy = 0, 0
        press = False

    elif event == cv2.EVENT_RBUTTONDBLCLK:
       # cv2.imwrite('/home/jeferson/Desktop/imagens_mosaico/frames/'+str(number_image)+'.png',pattern)
        print 'SALVO!!!'


path_img = '/home/jeferson/Desktop/imagens_mosaico/' #'/home/jeferson/MEGA/IEAv/imagens_mosaico/'


img = cv2.imread(path_img+ 'univap-final_transparent_mosaic_COM-APOIO.tif')


#asd = cv2.resize(img, (900,900))

#cv2.imwrite(path_im+'mosaico.png',asd)

#sys.exit()

number_image = int(len(os.listdir(path_img+'/frames/')))

size = 900
shift = 100
fx = 0
fxx= size
fy = 0
fyy = size

fract_img = img[fx:fxx,fy:fyy,:]

aux = fract_img.copy()

cv2.namedWindow('imagem')


cv2.setMouseCallback('imagem',retangulo)


while(1):
    cv2.imshow('imagem',fract_img)

    key = cv2.waitKey(1)
    if(key != -1):
        if(key == 1113938 or key == 65362 ):
            print 'cima'
            if(fx < size ):
                fx = 0
                fxx = size
            elif(fxx < shift):
                fxx = shift
            elif (fxx > shift and fx >= shift):
                fx -= shift
                fxx -= shift

        elif(key == 1113940 or key == 65364):
            print 'baixo'
            if(fxx + shift > img.shape[0]):
                fxx = img.shape[0]
            elif(fxx +shift <= img.shape[0]):
                fxx+= shift
                fx += shift

        elif (key == 1113937 or key == 65361):
            print 'esquerda'
            if(fy < size):
                fy = 0
                fyy = size
            elif(fyy <= shift):
                fyy = shift
            elif(fy - shift > 0 and fyy - shift >= shift):
                fyy -= shift
                fy -= shift

#int(shift/3)
        elif (key == 1113939 or key == 65363):
            print 'direita'
            if(fyy + shift + size > img.shape[1]):
                fyy = img.shape[1]
                fy = img.shape[1] -size
            elif(fyy + shift < img.shape[1] and fy + shift < img.shape[1]-shift):
                fyy+=shift
                fy+=shift


        print 'CHAVEEEEE', key

        print fx, fxx, fy, fyy

        fract_img = img[fx:fxx, fy:fyy]

        aux = fract_img.copy()

    if(key ==27):
        break