from pprint import pprint
from typing import Self, List

ROW = 0
COLUMN = 1

class CGMatriz:
    def __init__(self, matriz: List[List]):
        self.matriz = matriz
        self.m = len(matriz)
        self.n = len(matriz[ROW])
    
    def __mul__(self, matriz: Self):
        if self.n != matriz.m:
            raise Exception("A multiplicação de matrizes não pode ser efetuada")

        m_result = [[0 for _ in range(matriz.n)] for _ in range(self.m)]
    
        for i in range(self.m):
            for j in range(matriz.n):
                for k in range(self.n):
                    m_result[i][j] += self.matriz[i][k] * matriz.matriz[k][j]

        return CGMatriz(m_result)
    
    def __str__(self):
        str_result = ""
        for i in range(self.m):
            str_result += "["
            for j in range(self.n):
                str_result += str(self.matriz[i][j])  
                if j+1 < self.n : str_result +=  ","
            if i+1 < self.m: str_result += "]\n" 
            else: str_result +="]" 
        return str_result
            

    
        

