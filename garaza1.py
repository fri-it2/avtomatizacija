#!/usr/bin/python
import numpy as np,matplotlib.pyplot as plt
print '*** Statistika garaze - 11.06.2017 ***'

ime=raw_input('Vstavi ime zapisa:')
zapis=open(ime, 'r')		#odpri izvorno datoteko
string=zapis.readline()		#odstranim prvo, ki je slaba

graf=[]
dan=0				#stevec dni
dnevna=0
while string!="": 		#zanko ponavljam, dokler ne pridem do praznega znaka
	string=zapis.readline()
	if string[0:1]!=",":
		dan=dan+1
		graf=graf+[dnevna]
		dnevna=0
		print string,
	else:
		dnevna=dnevna+1

print graf
plt.plot(graf)
plt.title(ime)
plt.xlabel('Dan v letu')
plt.ylabel('Stevilo vseh dnevnih vstopov')
plt.show()

#konec programa

