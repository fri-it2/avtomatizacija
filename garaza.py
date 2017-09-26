#!/usr/bin/python
import numpy as np,matplotlib.pyplot as plt
print '*** Statistika garaze - 11.06.2017 ***'

ime=raw_input('Vstavi ime zapisa:')
zapis=open(ime, 'r')		#odpri izvorno datoteko
string=zapis.readline()		#odstranim prvo, ki je slaba

graf=[]
razlicni=[]
neplaca=[]
dan=0				#stevec dni
dnevna=0
razlicna=0
neplacnik=0
while string!="": 		#zanko ponavljam, dokler ne pridem do praznega znaka
	string=zapis.readline()
	if string[0:1]!=",":
		dan=dan+1
		graf=graf+[dnevna]
		razlicni=razlicni+[razlicna]
		neplaca=neplaca+[neplacnik]
		dnevna=0
		razlicna=0
		neplacnik=0
		kode=[]
		print string,
	else:
		i=4
		j=0
		n=0
		while i>0:
			j=j+1
			if string[j:j+1]==",":
				i=i-1
			if string[j:j+2]==",,":
				n=1
		koda=int(string[j+1:j+11])
		kode=kode+[koda]
		dnevna=dnevna+1
		i=0
		j=0
		while i<len(kode):
			if koda==kode[i]:
				j=j+1
			i=i+1
		if j<2:
			razlicna=razlicna+1
			if n>0:
				neplacnik=neplacnik+1

print graf
plt.plot(graf,'g-')
plt.plot(razlicni,'r-')
plt.plot(neplaca,'b-')
plt.title(ime)
plt.xlabel('Dan v letu')
plt.ylabel('Vsi(zelena) Razlicni(rdeca) Neplacniki(plava)')
plt.show()

#konec programa

