##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
import sys

x = open('data.csv', 'r').readlines()
x = [row[0:-1].split('\t') for row in x]
a = []
c = []
for i in x:
    a.append(i[4].split(","))
for j in a:
    for k in j:
        b = k.split(":")
        c.append(b[0])
uniquepatters = set(c)
cant_registros = [(l, c.count(l)) for l in sorted(uniquepatters)]

for i in cant_registros:
    print("%s,%d" %(i[0], i[1]))