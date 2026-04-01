# Python code​​​​​​‌‌‌‌​‌​‌‌‌​​‌​​​​​​‌‌‌‌​‌ below
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    primeList=[]
    for number in range(2,num):
        for factor in range (2 , int( number ** 0.5) + 1):
            if number % factor == 0:
                break
            else:
                primeList.append(number)
    return primeList

print(allPrimesUpTo(67))