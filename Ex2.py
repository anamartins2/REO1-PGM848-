import numpy as np
print('a) Declare a matriz abaixo com a biblioteca numpy.')
matriz = np.array([[1,3,22],[2,8,18],[3,4,22],[4,1,23],[5,2,52],[6,2,18],[7,2,25]])
print('Matriz')
print(matriz)
print('-'*40)
print('b) Obtenha o número de linhas e de colunas desta matriz')
# Obtendo a dimensão de uma matriz
nl,nc = np.shape(matriz)
print('Número de linhas: ' + str(nl))
print('Número de colunas: ' + str(nc))
print('-'*40)
print ('c) Obtenha as médias das colunas 2 e 3.')
#Média coluna 2
vetor_col_2 = matriz[:,1]
media1 = np.mean(vetor_col_2)
print('Media da coluna 2:'+ str(media1))
#Média coluna 3
vetor_col_3 = matriz[:,2]
media2 = np.mean(vetor_col_3)
print('Media da coluna 3:'+ str(media2))
print('-'*40)
print('d) Obtenha as médias das linhas considerando somente as colunas 2 e 3')
print(matriz)
sub_matriz0 = matriz[:,1:]
print(sub_matriz0)
media_submatriz0 = np.mean(sub_matriz0)
print(media_submatriz0)
print('A média das linhas considerando as colunas 2 e 3 é:'+ str (media_submatriz0))
print('-'*40)
print('e) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença ea terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade inferior a 5.')
sub_matriz = matriz[:,1]
print('Submatriz - matriz[0:,1]')
print(sub_matriz)
valores_menores_5 = matriz[sub_matriz<5]
print('Valores menos que 5')
print(valores_menores_5)
print('Portanto, os genótipos com valores inferiores a 5 são: 1,3,4,5,6 e 7')
print('-'*40)
print('f) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de peso de 100 grãos superior ou igual a 22.')
sub_matriz2 = matriz[:,2]
print('Matriz considerando a terceira coluna')
print(sub_matriz2)
valores_maiores_22 = matriz[sub_matriz2>=22]
print('Os genótipos 1,3,4,5 e 7 possuem peso superior ou igual a 22')
print(valores_maiores_22)
print('-'*40)
print('g) Considerando que a primeira coluna seja a identificação de genótipos, a segunda nota de severidade de uma doença e a terceira peso de 100 grãos. Obtenha os genótipos que possuem nota de severidade igual ou inferior a 3 e peso de 100grãos igual ou superior a 22.')
print('Valores Iguais ou Maiores que 3 e Menores que 7')
valores = matriz[(sub_matriz<=3) & (sub_matriz2>=22)]
print(valores)
print('Os genótipos 1,4,5 e 7 possuem nota de severidade inferior ou igual a 22 e peso maior ou igual a 22')
print('-'*40)
print('h) Crie uma estrutura de repetição com uso do for (loop) para apresentar na tela cada uma das posições da matriz e o seu respectivo valor. Utilize um iterador para mostrar ao usuário quantas vezes está sendo repetido. Apresente a seguinte mensagem a cada iteração "Na linha X e na coluna Y ocorre o valor: Z".Nesta estrutura crie uma lista que armazene os genótipos com peso de 100 grãos igual ou superior a 25')
matriz = np.array([[1,3,22],[2,8,18],[3,4,22],[4,1,23],[5,2,52],[6,2,18],[7,2,25]])
nl,nc = np.shape(matriz)

print('matriz')
print(matriz)
contador=0
matriz2 = np.zeros((nl,nc))
for i in np.arange(0,nl,1):
    for j in np.arange(0,nc,1):
        contador = +1
        print('Iteração: '+ str(contador))
        print('Na linha ' + str(i) + ' e coluna ' + str(j) + ' há o elemento: ' + str(matriz[int(i),int(j)]))
        matriz2 [int(i),int(j)] = (matriz[int(i),int(j)])
print('-'*40)
peso = []
contador = 0
for i in np.arange(0, nl, 1):
    if matriz[i, 2] >= 25:
        peso.append(matriz[i, 0])
        for j in np.arange(0, nc, 1):
            contador += 1
            print('Iteração:' + str(contador))
            print('A linha: ' + str(i) + ' e coluna ' + str(j) + ' corresponde ao valor: ' + str(matriz[int(i), int(j)]))
print(peso)
print('Os genótipos'+ str(peso)+' apresentam peso maior ou igual a 25')