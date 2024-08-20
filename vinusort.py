array = [2, 5, 7, 99, 11, 1010, 87, 554, 28472, 21, 1, 0]

def vinusort(arr):
    temp_array = []
    for n in array:
        if n > temp_array[len(array)-1]:
            temp_array.append(n)
        else:
            temp_array[1]

    for n in temp_array:
        print(n)

vinusort(array)