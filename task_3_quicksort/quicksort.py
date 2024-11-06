def partition(input, start, end):
    # middle pivot 
    p = int((start + end)/2)
    
    #print(f'pivot value is {input[p]}, pivot index = {p}')
    i = start
    j = end

    while i <= j:
        # search for value bigger than
        # pivot value on the left side
        while input[i] < input[p]:
            i+=1
        # search for value less than
        # pivot value on the right side
        while input[j] > input[p]:
            j-=1
        # if i and j didn't cross than
        # swap the values at index i and j 
        if i <= j:
            swap(input, i, j)
            i+=1
            j-=1
    return i
    

def quicksort(input, start, end):
    """
    Input:  Unsorted list of strings
    Output: Sorted list of strings
    The strings must be in a uniform
    case to be sorted alphabetically 
    Otherwise the sorting algorithm won't work 
    as expected because strings starting with lowercase 
    characters for example are greater than strings starting with uppercase.   
    """
    index = partition(input, start, end)
    if start < index - 1:
        quicksort(input, start, index - 1)
    if index < end:
        quicksort(input, index, end)


def quicksortIterative(input, start, end):
    """
    # Iterative quicksort 
    # input[] --> array to be sorted,
    # start  --> starting index,
    # end  --> ending index
    """

    # Create an auxiliary stack
    size = end - start + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of start and end to stack
    top = top + 1
    stack[top] = start
    top = top + 1
    stack[top] = end

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop end and start
        end = stack[top]
        top = top - 1
        start = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition( input, start, end )
        #print(f'Partition input[{start}:{end}] = {input[start:end]}')

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > start:
            top = top + 1
            stack[top] = start
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < end:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = end

def swap(input, i, j):
    tmp = input[j]
    input[j] = input[i]
    input[i] = tmp


def main():
    
    input = ['Banana','Apple','Pear','Apricot','Blueberries','Cherries','Coconut','Grape','Orange']
    print(input)
    quicksort(input,0,8)
    #quicksortIterative(input,0,8)
    print(input)

if __name__ == "__main__":
    main()



