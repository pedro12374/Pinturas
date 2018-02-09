import cv2,os,glob

#os.chdir("Auvers sur Oise (1890)")

def ler_Pasta(caminho): #Mostra todos os aquivos com a extensao .jpg na pasta 'caminho'
	os.chdir(caminho)
	temp = glob.glob('*.png')
	return temp




def Contar_Pixels(ipt): #Conta quantos pixels de cada cor tem
	
	img = cv2.imread(ipt)
	#px = img[1,1]
	B = img[1,1][0]
	G = img[1,1][1]
	R = img[1,1][2]
	return R,G,B

def Distribuicao(V_Entrada,V_Saida,tamanho):
	for i in range(tamanho):
		temp = V_Entrada.count(i)
		V_Saida.append(temp)
	print 'ok'

def Gerar_Distribuicao(Nome,vetor_Saida,tamanho):
	temp = open(Nome+'.dat','w')
	for i in range(tamanho):
		temp.write( str(i)+ '\t'+str(vetor_Saida[i])+'\n')

fold = ler_Pasta("Auvers sur Oise (1890)")
TotR=[]
TotG=[]
TotB=[]
for i in fold:
	j = Contar_Pixels(i)
	TotR.append(j[0])
	TotG.append(j[1])
	TotB.append(j[2])

RF = []
GF = []
BF = []

Distribuicao(TotR,RF,256)
Distribuicao(TotG,GF,256)
Distribuicao(TotB,BF,256)
print RF,GF,BF
Gerar_Distribuicao("AR",RF,256)
Gerar_Distribuicao("AG",GF,256)
Gerar_Distribuicao("AB",BF,256)


