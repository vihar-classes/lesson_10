target = int(input("Enter the target number: "))
print(f"Now enter numbers from 1 to {target}. Type 'done' when finished.")

user_list = []
while True:
    val = input("> ")
    if val.lower() == 'done':
        break
    user_list.append(int(val))

missing = []
for i in range(1, target + 1):
    if i not in user_list:
        missing.append(i)

if not missing:
    print("You didn't miss any numbers!")
else:
    print("You missed:", missing)
