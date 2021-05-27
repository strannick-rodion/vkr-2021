import sympy
import numpy as np
from sympy import *

A = np.array([[1, 3, 4, 2],
              [S(1)/3, 1, S(1)/2, S(1)/3],6
              [S(1)/4, 2, 1, 4],
              [S(1)/2, 3, S(1)/4, 1]])



pprint(A)
def multMatr(Mat1,Mat2):
    n = Mat1.shape[1]
    m = Mat2.shape[0]
    Mat =Mat1.copy()
    a=[]
    for j in range(0,m):
        for i in range(0,m):
            a=[]
            for l in range(0,n):
                a.append(Mat1[j][l]*Mat2[l][i])
                #print(Mat1[j][l],Mat2[l][i])
            #print("+++")
            Mat[j][i] = max(a) 
        #print(a)
    #pprint(Mat)
    return(Mat)

def oplusMatr(Mat1,Mat2):
    n = Mat1.shape[1]
    m = Mat2.shape[0]
    Mat =Mat1.copy()

    for j in range(0,m):
        for i in range(0,m):
            Mat[j][i] = max(Mat1[j][i],Mat2[j][i])
    return(Mat)

def powMatr(Mat1,n):
    Mat=Mat1.copy()
    for j in range(n-1):
        Mat=multMatr(Mat,Mat1)
    return Mat
def Kleene(Mat1):
    n = Mat1.shape[1]
    Mat = Mat1.copy()
    Mat = oplusMatr(Mat, (np.eye(n)))
    for i in range(2,n):
        MatTemp=powMatr(Mat1,i)
        Mat=oplusMatr(Mat,MatTemp)
    return Mat
def scalMatr(Mat1,a):
    m = Mat1.shape[0]
    Mat =Mat1.copy()
    for j in range(0,m):
        for i in range(0,m):
            Mat[j][i] = a*Mat1[j][i]
    return(Mat)

A=scalMatr(A,S(1)/2)
print("A=",A)
A2=powMatr(A,2)
print("A2=",A2)
A3=powMatr(A,3)
print("A3=",A3)
A4=powMatr(A,4)
print("A4=",A4)
k=Kleene(A)


print("k =",k)
