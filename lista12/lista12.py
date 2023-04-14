from matplotlib import pyplot
import numpy
import pandas
import seaborn

figure = pyplot.figure()

dane_pojazdy = pandas.read_csv(r'C:\Users\Lenovo\Desktop\programowanie python\lista 12\plik.csv')
liczby_pojazdow = dane_pojazdy['LICZBA_POJAZDOW']
gminy = dane_pojazdy['GMINA']
id_gmin = dane_pojazdy['_id']

#wykres 1 - liniowy
ax1 = figure.add_subplot(221)
ax1.plot(liczby_pojazdow, gminy, label='liczba pojazdow')
ax1.set_xlabel('Liczba pojazdów w ciągu doby')
ax1.set_ylabel('Gmina')
ax1.set_title('Liczba pojazdów na gminę w województwie dolnośląskim')

#wykres 2 - kołowy
ax2 = figure.add_subplot(222)
ax2.pie(liczby_pojazdow, labels=gminy, autopct='%1.1f%%')
ax2.set_title('Procent pojazdów dla danej gminie w województwie dolnośląskim w odniesieniu do całego województwa')

#wykres 3 - histogram
ax3 = figure.add_subplot(223)
bins = [250,500,750,1000,1250,1500,2000,2500,3000,3500,4000,5000]
ax3.hist(liczby_pojazdow, bins=bins, edgecolor='black', color='orange', label='liczba gmin')
ax3.set_title('Liczba gmin w województwie donlośląskim dla danego zakresu pojazdów')
ax3.set_xlabel('Zakres liczby pojazdów')
ax3.set_ylabel('Liczba gmin')

#wykres 4 - rozrzutu
ax4 = figure.add_subplot(224)
ax4.scatter(liczby_pojazdow, gminy, color='green', label='liczba pojazdów')
seaborn.regplot(liczby_pojazdow, id_gmin)
ax4.set_ylabel('Gmina')
ax4.set_xlabel('Liczba pojazdów')
ax4.set_title('Liczba pojazdów na gminę w województwie dolnośląskim')

figure.legend(frameon=False, bbox_to_anchor=(1,0.9))
pyplot.show()