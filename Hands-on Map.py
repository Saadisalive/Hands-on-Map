#Add two lists using map aand lambda
number1 = [1,2,3]
numbers2 = [4,5,6]
result = map(lambda x, y: x + y, number1,numbers2)
print("Addition of two lists")
print(list(result))

#using map
nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq,nums))
print("Square of numbers in list")
print(square)