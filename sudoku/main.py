import  math
import xlrd

import numpy as np


workbook = xlrd.open_workbook("sudoku.xlsx")
sheet = workbook.sheet_by_index(0)
a,b=9,9
table = np.zeros((a, b))


for i in range (0,a):
    for j in range (0,b):
        table[i, j] = sheet.cell_value(i, j)

l=[0,3,6,9]

def borne (l,i):

    for j in range (0,len(l)):
        if l[j]>i :
            return [l[j-1],l[j]]
        elif i==0:
            return [0,3]
    if i==9 :
        return [6,9]



def existance(m,a):
    for k in range (0,len(a)):
        if m==a[k]:
            return 1
    return 0


def compar (m,n,l):

        a=[]
        for k in range (1,10):
            if existance(k,m)==0:
                if existance(k,n)==0:
                    if existance(k,l)==0:
                        a.append(k)

        return a

def test_table (table):
    for i in range (0,9):
        for j in range (0,9):
            if table[i,j]==0:
                return 0
    return 1


while(test_table(table)==0):

    for i in range(0, 9):
        for j in range(0, 9):

            if table[i, j] == 0:
                a = borne(l, i)
                b = borne(l, j)
                m = []
                n = []
                c = []
                for k in range(0, 9):
                    m.append(table[i, k])

                    n.append(table[k, j])
                for k in range(a[0], a[1]):
                    for v in range(b[0], b[1]):
                        c.append(table[k, v])
                e = compar(m, n, c)

                if (len(e) == 1):
                    table[i,j]=e[0]


print(table)