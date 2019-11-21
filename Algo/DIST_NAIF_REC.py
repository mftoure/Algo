from math import inf


Cdel=2
Cins=2

def Csub(a,b):
	if(a==b):
		return 0
	if((a=='A' and b=='T') or (a=='T' and b=='A') or (a=='G' and b=='C') or (a=='C' and b=='G')):
		return 3
	return 4

def DIST_NAIF_REC(x,y,i,j,c,dist):
	if(i==len(x)-1 and j==len(y)-1):
		if(c<dist):
			dist=c
	else:
		if(i<len(x)-1 and j<len(y)-1):
			dist=DIST_NAIF_REC(x,y,i+1,j+1,c+Csub(x[i+1],y[i+1]),dist)
		else:
			if(i<len(x)):
				dist=DIST_NAIF_REC(x,y,i+1,j,c+Cdel,dist)
			if(j<len(y)):
				dist=DIST_NAIF_REC(x,y,i,j+1,c+Cins,dist)
	return dist

def DIST_NAIF(x,y):
	return DIST_NAIF_REC(x,y,0,0,0,inf)

x=['T','A','T','A','T','G','A','G','T','C']
y=['T','A','T','T','T']



print("Inst_0000010_44.adn :",DIST_NAIF(x,y))


x=['T','G','G','G','T','G','C','T','A','T']
y=['G','G','G','G','T','T','C','T','A','T']


print("Inst_0000010_7.adn :",DIST_NAIF(x,y))

x=['A','A','C','T','G','T','C','T','T','T']
y=['A','A','C','T','G','T','T','T','T']


print("Inst_0000010_8.adn :",DIST_NAIF(x,y))


