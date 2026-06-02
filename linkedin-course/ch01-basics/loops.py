# for loops
for number in range(1, 10, 2):
    print("Attempt ", number, (number+1)*".")

# for else loops
successful = False
for number in range(3):
    print("Attempt ", number)
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# while loops
command = ""
while command != "quit":
    command = input(">>>")
    print("ECHO", command)
