def selection_sort(in_array):
    min = 0
    for i in range(0, len(in_array) - 2):
        min = i
        for j in range(i + 1, len(in_array) - 1):
            if in_array[j] < in_array[min]:
                min = j
                in_array[i], in_array[min] = in_array[min], in_array[i]
            
def bubble_sort(in_array):
    for i in range(0, len(in_array) - 2):
        for j in range(0, len(in_array)- 2 - i):
            if in_array[j + 1] < in_array[j]:
                in_array[j] = in_array[j+1]

def hayes_sort(in_array):
    index = 0
    max = in_array[0]
    for i in range(1, len(in_array) -1 ):
        if in_array[i] > max:
            max = in_array[i]