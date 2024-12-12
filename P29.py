#Program 29

def insertion_sort_words(words):
    print("Initial List:", words)
    
    for i in range(1, len(words)):
        key = words[i]
        j = i - 1
        
        while j >= 0 and (
            len(words[j]) > len(key) or 
            (len(words[j]) == len(key) and words[j] > key)
        ):
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = key
        
        print(f"Pass {i}: {words}")
    
    return words


def main():
    print("Enter words separated by spaces:")
    user_input = input()
    words = user_input.split()
    
    sorted_words = insertion_sort_words(words)
    
    print(" ")
    print("Final Sorted List:", sorted_words)


if __name__ == "__main__":
    main()