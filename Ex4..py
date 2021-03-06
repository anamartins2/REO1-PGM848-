print('a) O arquivo dados.txt contem a avaliação de genótipos (primeira coluna) em repetições (segunda coluna) quanto a quatro variáveis (terceira coluna em diante). Portanto, carregue o arquivo dados.txt com a biblioteca numpy, apresente os dados e obtenha as informações de dimensão desta matriz.')
import numpy as np
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)
dados = np.loadtxt('dados.txt')
print('Dados')
print(dados)
nl,nc = np.shape(dados)
print('Número de linhas: ' + str(nl))
print('Número de colunas: ' + str(nc))
print('-'*40)
print('b) Pesquise sobre as funções np.unique e np.where da biblioteca numpy')
np.info(np.where)
np.info(np.unique)
print('-'*40)
print('c) Obtenha de forma automática os genótipos e quantas repetições foram avaliadas')
genotipos = np.unique(dados[:,0:1], axis=0)
rep= np.unique(dados[:,1:2], axis=0)
nlg,ncg = np.shape(genotipos)
print('Número de linhas: ' + str(nlg))
print('Número de colunas: ' + str(ncg))
print('Genótipos avaliados:' + str(genotipos))
print('Número de repetições:'+ str(rep))
print('-'*40)
print('d) Apresente uma matriz contendo somente as colunas 1, 2 e 4')
sub_matriz3 = dados[:,[0,1,3]]
print(sub_matriz3)
print('-'*40)
print('e) Obtenha uma matriz que contenha o máximo, o mínimo, a média e a variância de cada genótipo para a variavel da coluna 4. Salve esta matriz em bloco de notas.')

min = np.zeros((nlg,1))
max = np.zeros((nlg,1))
med = np.zeros((nlg,1))
vars = np.zeros((nlg,1))
it=0
for el in np.arange(0,30,3): #30 linhas do vetor original de acordo com o numero de repetições

    min[it,0] = np.min(sub_matriz3[el:el + 3, 2], axis=0)
    max[it,0] = np.max(sub_matriz3[el:el + 3, 2],axis=0)
    med [it,0] = np.mean(sub_matriz3[el:el + 3, 2],axis=0)
    vars[it,0] = np.var(sub_matriz3[el:el + 3, 2],axis=0)
    it += 1 #incrementa + 1 no it
print('Genótipos     Min     Max      Média    Variância')
matriz_concat = np.concatenate((genotipos,min,max,med,vars),axis=1)
print(matriz_concat)
#help(np.savetxt)
np.savetxt('matriz_ex3.txt', matriz_concat, delimiter=' ')
print('-'*40)
print('f) Obtenha os genótipos que possuem média (médias das repetições) igual ou superior a 500 da matriz gerada na letra anterior.')
dados2 = np.loadtxt('matriz_ex3.txt')
sub_matriz_concat= matriz_concat[:,3]
print(sub_matriz_concat)
bool_500 = sub_matriz_concat>=500
print(bool_500)
pos_500 = np.where(sub_matriz_concat>=500)
print(pos_500)
"Posições 0 e 6, ou seja, genótipos 1 e 7"
print('-'*40)
print('g) Apresente os seguintes graficos:')
#    - Médias dos genótipos para cada variável. Utilizar o comando plt.subplot para mostrar mais de um grafico por figura
#    - Disperão 2D da médias dos genótipos (Utilizar as três primeiras variáveis). No eixo X uma variável e no eixo Y outra.
import matplotlib.pyplot as plt
import os
dados = np.loadtxt('dados.txt')
media1 = np.zeros((nlg,1))
media2 = np.zeros((nlg,1))
media3 = np.zeros((nlg,1))
media4 = np.zeros((nlg,1))
media5 = np.zeros((nlg,1))
it=0
for el in np.arange(0,30,3): #0 a 30, passo 3(repetições).
    media1[it,0] = np.mean(dados[el:el + 3, 2], axis=0)
    media2[it,0] = np.mean(dados[el:el + 3, 3], axis=0)
    media3[it,0] = np.mean(dados[el:el + 3, 4], axis=0)
    media4[it,0] = np.mean(dados[el:el + 3, 5], axis=0)
    media5[it,0] = np.mean(dados[el:el + 3, 6], axis=0)
    it += 1

dadosm = np.concatenate((genotipos,media1,media2,media3,media4,media5),axis=1)
nlm,ncm = np.shape(dadosm)
print('Número de linhas:', nlm)
print('Número de colunas:', ncm)
fig = plt.figure('Histograma')
plt.subplot(2,3,1) #terão 2 linhas, 3 colunas (5 gráficos e este vai ocupar a posição 1
plt.bar(dadosm[:,0],dadosm[:,1])
plt.title('Variável 1')
plt.xticks(dadosm[:,0]) #inserindo no eixo os genótipos
plt.style.use('ggplot')


plt.subplot(2,3,2)
plt.bar(dadosm[:,0],dadosm[:,2])
plt.title('Variável 2')
plt.xticks(dadosm[:,0])

plt.subplot(2,3,3)
plt.bar(dadosm[:,0],dadosm[:,3])
plt.title('Variável 3')
plt.xticks(dadosm[:,0])

plt.subplot(2,3,4)
plt.bar(dadosm[:,0],dadosm[:,4])
plt.title('Variável 4')
plt.xticks(dadosm[:,0])

plt.subplot(2,3,5)
plt.bar(dadosm[:,0],dadosm[:,5])
plt.title('Variável 5')
plt.xticks(dadosm[:,0])
plt.show()
#nome = 'histograma4'
#fig.savefig((nome+'.png'), bbox_inches="tight")
#os.startfile(nome+'.png')
print('-'*40)
###Gráfico de dispersão
plt.style.use('ggplot')
fig = plt.figure('Dispersão')
plt.subplot(2,2,1)
cores = ['black','blue','red','green','yellow','pink','cyan','orange','darkviolet','slategray']
for el in np.arange(0,nlm,1):
    plt.scatter(dadosm[el,1], dadosm[el,2],s=50,alpha=0.8,label = dadosm[el,0],c = cores[el])
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.subplot(2,2,2)
plt.title('Gráfico de dispersão')## coloquei só um título porque estava tampando parte do gráfico.
for el in np.arange(0,nlm,1):
    plt.scatter(dadosm[el,2], dadosm[el,3],s=50,alpha=0.8,label = dadosm[el,0],c = cores[el])
plt.xlabel('Variável 2')
plt.ylabel('Variável 3')
plt.subplot(2,2,3)
for el in np.arange(0,nlm,1):
    plt.scatter(dadosm[el,1], dadosm[el,3],s=50,alpha=0.8,label = dadosm[el,0],c = cores[el])
plt.xlabel('Variável 1')
plt.ylabel('Variável 3')
plt.legend()
plt.show()