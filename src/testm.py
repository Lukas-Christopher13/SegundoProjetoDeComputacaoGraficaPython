from utils.cg_matriz import CGMatriz

cgm = CGMatriz([
    [2,2,2],
    [2,2,2],
    [2,2,2]
])

matriz = CGMatriz([
    [3,3],
    [3,3],
    [3,3]
])

result = cgm * matriz
print(result)