# def factorial(n):
#     if (n == 0 or n == 1) or n < 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(4))

# def sumOfDigits(n):
#     if n == 0:
#         return 0
#     return int(abs(n) % 10) + sumOfDigits(int(abs(n) // 10))

# print(sumOfDigits(-11111))

# def power(number, exponent):
#     if exponent == 0:
#         return 1
#     elif exponent < 0:
#         raise Exception("Power should be positive number")
#     else:
#         return number * power(number, exponent-1)

# print(power(100,100))

# def multiply( a , n ):
     
#     # Termination condition
#     if n == 0:
#         return(a[n])
#     else:
#         return (a[n] * multiply(a, n - 1))
 
# # Driver Code
# array = [1,2,3]
# n = len(array)
 
# # Function call to 
# # calculate the product
# print(multiply(array, n - 1))

# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])

# print(isPalindrome("tacocat"))
# print(isPalindrome("booo"))
x = "hello"
print(x.capitalize())