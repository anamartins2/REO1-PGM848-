def media (vetor):
    somador = 0
    it= 0
    for el in vetor:
        somador+= el
        it+=1
        mean = somador/it
        return mean
def variancia (vetor):
    somador = 0
    it = 0
    sq = 0
    for el in vetor:

        somador += el
        it += 1
        sq += el**2

    var = (sq - ((somador**2/it)))/(it-1)
    return var