def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


print_items(10)
# here t.c is o(n^2 + n ) we drop n which is non  dominant hence answer is O(n^2)
