#Program 28

def print_diamond(n):
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

    for i in range(n - 1, 0, -1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)


def main():
    n = int(input("Enter the number of rows for the upper half of the diamond: "))
    
    print_diamond(n)


if __name__ == "__main__":
    main()