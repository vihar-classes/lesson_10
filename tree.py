rows = int(input("How many rows for the top half? "))
choice = input("Type 'D' for Diamond, 'R' for Reverse, or 'N' for Normal: ").upper()

if choice == 'D':
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

elif choice == 'R':
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

else:
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
