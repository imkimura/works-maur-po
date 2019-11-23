#Algoritimo de Counting Sort!

def countingSort(array):
	output = [0 for i in range(len(array))]
	count = [0 for i in range(len(array))]
	answer = ["" for _ in array] 

	for i in array:
		count[i] += 1

	for i in range(len(array)):
		count[i] += count[i-1]

	for i in range(len(array)):
		output[count[array[i]]-1] = array[i]
		count[array[i]] -= 1

	for i in range(len(array)):
		answer[i] = output[i]
	return answer 




array = [2, 5, 3, 0, 2, 3, 0, 3]
print("O vetor organizado eh: ", countingSort(array))
