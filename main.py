# input an integer value
n = int(input("Enter the number whose sum you want to find: "))
total_sum = 0  # Changed 'sum' to 'total_sum' as 'sum' is a built-in function

# Iterates from 1 up to n
for i in range(1, n + 1):
    total_sum = total_sum + i

print("\nFinal Sum =", total_sum)
