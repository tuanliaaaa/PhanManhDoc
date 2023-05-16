hang = int(input("nhập số hàng: "))
cot = int(input("nhập số cột: "))
size = int(input("nhập số size: "))
matrixfirst_final=[0]*cot
f=[0,1]
import numpy as np


def bond(a, b):
    bondReturn = 0
    for i in range(cot):
        bondReturn += a[i] * b[i]
    return bondReturn


def cont(a, b, c):
    return 2 * bond(a, b) + 2 * bond(b, c) - 2 * bond(a, c)


def inputMatrix(k):
    for i in range(hang):
        k.append([int(x) for x in input().split(" ")])


def createAA(matrixProperties, matrixAcc):
    matrixAA = []
    for i in range(cot):
        row = []
        for j in range(cot):

            sumAA = 0
            for k in range(hang):
                if (matrixProperties[k][i] == 1 and matrixProperties[k][j] == 1):
                    sumAA += sum(matrixAcc[k])
            row.append(sumAA)
        matrixAA.append(row)
    return matrixAA


def createAC(matrixAA):
    matrixAC = []
    matrixAC.append(matrixAA[0])
    matrixAC.append(matrixAA[1])
    for i in range(2, cot):
        indexMax = 0
        Max = cont(matrixAA[i],matrixfirst_final, matrixAC[0])
        for j in range(len(matrixAC) ):
            if(j!=len(matrixAC)-1):
                if (cont(matrixAC[j], matrixAA[i], matrixAC[j + 1]) > Max):
                    Max = cont(matrixAC[j], matrixAA[i], matrixAC[j + 1])
                    indexMax = j+1
            else:
                if (cont(matrixAC[j], matrixAA[i], matrixfirst_final) > Max):
                    Max =  cont(matrixAC[j], matrixAA[i], matrixfirst_final)
                    indexMax = j+1
        f.insert(indexMax,i)
        matrixAC.insert(indexMax, matrixAA[i])

    hoanvimatrxAC=[[]]*cot
    for j in range(cot):
        l=[]
        for i in f:
            l.append(matrixAC[j][i])
        hoanvimatrxAC[j]=l
    return hoanvimatrxAC


matrixProperties = []
matrixAcc = []
print("nhập ma trận thuộc tính:")
inputMatrix(matrixProperties)
print("nhập ma trận acc:")
inputMatrix(matrixAcc)
matrixAA = createAA(matrixProperties, matrixAcc)
print("MatrixAA: ")

print(np.array(matrixAA))
matrixAC = createAC(matrixAA)
print("MatrixAC: ")
print(np.array(matrixAC))

new_list = []

for element in f:
    new_element = element + 1
    new_list.append(new_element)

print(new_list)





