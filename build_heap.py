# python3
# Elīza Kanska 221RDB095


def build_heap(data):
    swaps = []
    # TODO: Create heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)

    def down(j):
        nonlocal swaps
        min_indx = j
        right_child = 2 * j + 2
        left_child = 2 * j + 1
        
        if data[right_child] < data[min_indx] and right_child < n:
            min_indx = right_child
        if data[left_child] < data[min_indx] and left_child < n:
            min_indx = left_child
        
        if data[min_indx] < data[j]:
            data[j], data[min_indx] = data[min_indx], data[j]
            swaps.append((j, min_indx))
            down(min_indx)
            
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
        assert len(data) == n
        swaps = build_heap(data)
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    # input from file
    elif n == 'F':
        file = input()
        with open("tests/" + file, 'r') as fin:
            n = int(fin.readline().strip())
            data = list(map(int, fin.readline().split()))
            assert len(data) == n
            swaps = build_heap(data)
            print(len(swaps))
            for i, j in swaps:
                print(i, j)   


if __name__ == "__main__":
    main()
