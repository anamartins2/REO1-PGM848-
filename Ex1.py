print('a) Declare os valores 43.5,150.30,17,28,35,79,20,99.07,15 como um array numpy.')
import numpy as np
vetor_np = np.array([43.5,150.30,17,28,35,79,20,99.07,15])
print('Vetor: ' + str(vetor_np))
print('Tipo')
print(type(vetor_np))
print(' b) Obtenha as informações de dimensão, média, máximo, mínimo e variância deste vetor.')
print('Dimensão do vetor')
print('Vetor:' + str(vetor_np))
dim = len(vetor_np)
print('Dimensão (dim): ' + str(dim))
print('Tipo dimensão')
print(type(dim))
media = np.mean(vetor_np)
min = np.min(vetor_np)
max = np.max(vetor_np)
var = np.var(vetor_np)
print('Media:'+ str(media))
print('Mínimo:'+ str(min))
print('Máximo:'+ str(max))
print('Variância:'+str(var))
print('-'*40)
print('c) Obtenha um novo vetor em que cada elemento é dado pelo quadrado da diferença entre cada elemento do vetor declarado na letra a e o valor da média deste.')
vetor2 = np.zeros(dim)
for el in range(dim):
    vetor2[el] = np.array((vetor_np[el] - np.mean(vetor_np))**2)
print ("O vetor dado pelo quadrado da diferença entre cada elemento do vetor: " +str (vetor2))
print('d) Obtenha um novo vetor que contenha todos os valores superiores a 30.')
sequencia = range(31,100,5)
print('REANGE: Sequencia 31 até 100 (passo: 5)')
print(sequencia)
print('Tipo')
print(type(sequencia))
sequencia = np.array(sequencia)
print('NUMPY: Sequencia 31 até 100 (passo: 5)')
print(sequencia)
print('Tipo')
print(type(sequencia))
print('-'*40)
print('e) Identifique quais as posições do vetor original possuem valores superiores a 30')
vetor_np = np.array([43.5,150.30,17,28,35,79,20,99.07,15])
bool_maior_30 = vetor_np>30
print('Vetor: ' + str(vetor_np))
print('Vetor booleano maior que 30: ' + str(bool_maior_30))

pos_maior_30 = np.where(vetor_np>30)
print('Posições com valores menores que 50: ' + str(pos_maior_30[0]))
print('-'*40)
print('f) Apresente um vetor que contenha os valores da primeira, quinta e última posição.')
vetor_np = np.array([43.5,150.30,17,28,35,79,20,99.07,15])
vetor_novo = np.array([vetor_np[0],vetor_np[4],vetor_np[8]])
print ("Valores da primeira, quinta e última posição: " +str(vetor_novo))
print('-'*40)
print('g) Crie uma estrutura de repetição usando o for para apresentar cada valor e a sua respectiva posição durante as iterações')
import numpy as np
vetor_np = np.array([43.5,150.30,17,28,35,79,20,99.07,15])
print(vetor_np)
print('Lista: ' + str(vetor_np))
print('Número de elementos do vetor: ' + str(len(vetor_np)))
it = 0
for el in range(0, len(vetor_np),1):
    it = it + 1
    print('Iteração: ' + str(it))
    print('Na posição ' + str(el) + ' há o elemento: ' + str(vetor_np[int(el)]))
print('-'*40)
print('h) Crie uma estrutura de repetição usando o for para fazer a soma dos quadrados de cada valor do vetor.')
sdq = np.zeros(dim)
somador=0
for el in range(0, len(vetor_np),1):
        sdq[el] = (vetor_np[el]) ** 2
        somador += sdq[el]
print("Elementos ao quadrado: " + str(sdq))
print("Soma de quadrados: " + str(somador))


print('-'*40)
print('i) Crie uma estrutura de repetição usando o while para apresentar todos os valores do vetor')
vetor_np = np.array([43.5,150.30,17,28,35,79,20,99.07,15])
print('Vetor: ' + str(vetor_np))
print('Dimensão: ' +str(len(vetor_np)))

pos = 0
while vetor_np[pos]!=12:
    print(vetor_np[pos])
    pos = pos+1
    if pos==len(vetor_np):
        print('Posição igual a: ' + str(pos) + ' - A condição estabelecida retornou true, vamos sair do while')
        break
print('-'*40)
print('j) Crie um sequência de valores com mesmo tamanho do vetor original e que inicie em 1 e o passo seja também 1.')
import numpy as np
seq= range(1,10,1)
sequencia = np.arange(1,10,1)
print('ARANGE:Sequencia 1 até 10 (passo: 1)')
print(sequencia)
print('Tipo')
print(type(sequencia))
print('-'*40)
print('k) Concatene o vetor da letra a com o vetor da letra j.')
import numpy as np
vetor_np = np.array([43.5,150.30,17,28,35,79,20,99.07,15])
sequencia=np.array([1,2,3,4,5,6,7,8,9])
vet_concat = np.concatenate((vetor_np, sequencia))
print(vet_concat)