# python3
# Elīza Kanska 221RDB095


def build_heap(data):
    swaps = []
    # TODO: Create heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)

    def down(j):
        nonlocal swaps
        min = j
        right_child = 2 * j + 2
        left_child = 2 * j + 1
        
        if data[right_child] < data[min] and right_child < n:
            min = right_child
        if data[left_child] < data[min] and left_child < n:
            min = left_child
        
        if min != j:
            data[j], data[min] = data[min], data[j]
            swaps.append((j, min))
            down(min)
            
    not_a_leaf = (n - 2) // 2
    
    for j in range(not_a_leaf, -1, -1):
        down(j)
        
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    n = input().strip()

    # input from keyboard
    if n == 'I':
        n = int(input())
        data = list(map(int, input().split()))
        
    elif n == 'F':
        file = input()
        with open("tests/" + file, 'r') as fin:
            n = int(fin.readline().strip())
            data = list(map(int, fin.readline().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
