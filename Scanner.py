import cv2,os,glob,time
start_time = time.time()
from PIL import Image
import numpy as np
'''
path = os.getcwd()
os.chdir(path+'/Auvers sur Oise (1890)')
path = os.getcwd()
k = glob.glob('*.jpg')
print k
'''
#Paint = open('Pinturas.tsv','w')
#for pintura in range(len(k)):
totR = []
totG = []
totB = []
GsR = []
GsG = []
GsB = []
def ler_Pasta(caminho):
	os.chdir(caminho)
	temp = glob.glob('*.jpg')
	return temp

def Contar_Pixels(img):

	altura = len(img)
	largura = len(img[0])
	for i in range(largura):
		for j in range(altura):
			px = img[j,i]
			totR.append(px[2])
			totB.append(px[0])
			totG.append(px[1])

def Calcular_Media():
	temp1 = sum(totR)/len(totR)
	temp2 = sum(totG)/len(totG)
	temp3 = sum(totB)/len(totB)
	result = [temp1,temp2,temp3]
	return result

def Gerar_Media(Nome,valores):
	im = Image.new("RGB", (128, 128))
	pix = im.load()
	for x in range(128):
	    for y in range(128):
	        pix[x,y] = (valores[0],valores[1],valores[2])
	im.save(Nome+".png", "PNG")

def Distribuicao(V_Entrada,V_Saida,tamanho):
	for i in range(tamanho):
		temp = V_Entrada.count(i)
		V_Saida.append(temp)
	print 'ok'

def Gerar_Distribuicao(Nome,vetor_Saida,tamanho):
	temp = open(Nome+'.dat','w')
	for i in range(tamanho):
		temp.write( str(i)+ '\t'+str(vetor_Saida[i])+'\n')


img = cv2.imread('test1.jpg')








print("--- %s seconds ---" % (time.time() - start_time))





#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()