def factorial(num):
    if type(num)!=int:
        return None
    if num < 0:
        return None
    result=1
    a=num
    while a > 1:
        result=result*a
        a-=1
    return result


print(factorial(5))