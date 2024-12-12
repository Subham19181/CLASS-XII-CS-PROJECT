#Program 27

def bubble_sort_descending(arr):
    n = len(arr)
    total_swaps = 0

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                swapped = True
                total_swaps += 1
        if not swapped:  
            break

    return arr, total_swaps


def main():
    print("Enter integers separated by spaces:")
    user_input = input()
    arr = list(map(int, user_input.split()))
    
    sorted_arr, swaps = bubble_sort_descending(arr)

    print("Sorted List (Descending Order):", sorted_arr)
    print("Total Number of Swaps:", swaps)

if __name__ == "__main__":
    main()