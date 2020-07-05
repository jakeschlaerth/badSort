import math

while True:
    try:
        alpha = float(input("Please input desired alpha parameter such that 0 < alpha < 1 :  "))
    except ValueError:
        print("invalid input. Please enter a decimal value between 0 and 1")
        continue
    if alpha < 0 or alpha > 1:
        print("invalid input. Please enter a decimal value between 0 and 1")
        continue
    if alpha <= .5:
        print("warning: this alpha parameter will not correctly sort data.")
        break
    break


def badSort(arr, left, right):
    n = right - left + 1
    if left + 1 == right:  # if the length of the sub-array being checked is 2
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

    if n > 2:  # if the length of the sub-array is > 2
        m = math.ceil(n * alpha)

        if m == n and n > 2:  # if m == n and n is > 2, n will never decrease and we will recurse infinitely
            m -= 1

        badSort(arr, left, (left + m - 1))
        badSort(arr, (right - m + 1), right)
        badSort(arr, left, (left + m - 1))


with open('data.txt', 'r') as infile:
    # iterate through each line
    output = ""
    for line in infile:
        # populate list by values separated by spaces, strip newline characters
        number_list = line.strip().split(" ")
        # typecast strings to ints
        for i in range(0, len(number_list)):
            number_list[i] = int(number_list[i])
        # remove first value
        del number_list[0]
        # sort
        badSort(number_list, 0, len(number_list)-1)
        # add values to output string
        for i in range(0, len(number_list)):
            output += str(number_list[i])
            output += " "
        # start newline after each line
        output += "\n"

    # write file
    with open("bad.out", 'w') as outfile:
        # cast my_sum as string, write to file
        outfile.write(str(output))
