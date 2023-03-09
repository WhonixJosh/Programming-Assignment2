def selection_sort(in_array):
    for i in range(0, len(in_array) - 1):
        min = i
        for j in range(i + 1, len(in_array)):
            if in_array[j] < in_array[min]:
                min = j
                in_array[i], in_array[min] = in_array[min], in_array[i]
            
def bubble_sort(in_array):
    for i in range(0, len(in_array) - 1):
        for j in range(0, len(in_array) - i - 1):
            if in_array[j + 1] < in_array[j]:
                in_array[j], in_array[j+1] = in_array[j+1], in_array[j]

def hayes_sort(in_array):
    hayes_sorted_list = []
    index = 0
    max = in_array[0]
    for i in range(1, len(in_array) -1 ):
        if in_array[i] > max:
            max = in_array[i]
    for j in range(0,max + 1):
        if j in in_array:
            hayes_sorted_list.append(j)
            index = index + 1
    return hayes_sorted_list