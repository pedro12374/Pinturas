import cv2,os,glob,time
start_time = time.time()
from PIL import Image
import numpy as np
totR=[]
totB=[]
totG=[]
def ler_Pasta(caminho): #Mostra todos os aquivos com a extensao .jpg na pasta 'caminho'
	os.chdir(caminho)
	temp = glob.glob('*.jpg')
	return temp

def Contar_Pixels(ipt): #Conta quantos pixels de cada cor tem
	img = cv2.imread(ipt)
	altura = len(img)
	largura = len(img[0])
	for i in range(altura):
		for j in range(largura):
			px = img[i,j]
			totB.append(px[0])
			totG.append(px[1])
			totR.append(px[2])

def Calcular_Media(vetor): #Faz uma media do vetor colocado
	temp = sum(vetor)/len(vetor)
	return temp

def Gerar_Media(Nome,r,g,b): #Gera um arquivo png com intitulado com o "Nome", usando os valores de rgb colocados
	im = Image.new("RGB", (128, 128))
	pix = im.load()
	for x in range(128):
	    for y in range(128):
	        pix[x,y] = (r,g,b)
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


os.chdir('Van.gogh.paintings')
dire = os.listdir(os.getcwd())

for i in dire:
	os.chdir("/home/haerter/Pinturas/Van.gogh.paintings")
	k = ler_Pasta(i)
	print "ok 1 " + i
	for j in k:
		totR=[]
		totB=[]
		totG=[]
		Contar_Pixels(j)
		R = Calcular_Media(totR)
		G =	Calcular_Media(totG)
		B = Calcular_Media(totB)
		Gerar_Media('med-'+j,R,G,B)
		print "Pintura Gerada " + j
