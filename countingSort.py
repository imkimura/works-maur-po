#Algoritimo de Counting Sort!

def countingSort(array):
	answer = [0 for i in range(len(array))]
	count = [0 for i in range(len(array))]

	#Criando vetor 'C'
	for i in array:
		count[i] += 1

	#Usando vetor 'C' e somando com indice anterior
	for i in range(len(array)):
		count[i] += count[i-1]

	#Adicionando no vetor de maneira organizada
	for i in range(len(array)):
		answer[count[array[i]]-1] = array[i]
		count[array[i]] -= 1

	return answer



array = [2, 5, 3, 0, 2, 3, 0, 3]
print("O vetor organizado eh: ", countingSort(array))
