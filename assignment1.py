#task1
def print_digits(n):
    if n < 10:
        print(n)
        return
    print_digits(n // 10)
    print(n % 10)

print_digits(5481)

#task2
def sum_recursive(arr, n):
    if n == 0:
        return 0
    return sum_recursive(arr, n - 1) + arr[n - 1]

def average(arr):
    return sum_recursive(arr, len(arr)) / len(arr)

arr = [3, 2, 4, 1]

#task3
def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)
    
print("Prime" if is_prime(7) else "Composite")
print("Prime" if is_prime(10) else "Composite")

#task4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
print(average(arr))  # 2.5

#task5
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))   # 5
print(fibonacci(17))  # 1597

#task6
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

print(power(2, 10))  # 1024

#task7
def reverse_print(arr, n):
    if n == 0:
        return
    print(arr[n - 1], end=" ")
    reverse_print(arr, n - 1)

arr = [1, 4, 6, 2]
reverse_print(arr, len(arr))  # 2 6 4 1

#task8
def is_digits(s):
    if s == "":
        return True
    if not s[0].isdigit():
        return False
    return is_digits(s[1:])

print("Yes" if is_digits("123456") else "No")
print("Yes" if is_digits("123a12") else "No")

#task9
def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])

print(string_length("hello"))      # 5
print(string_length("recursion"))  # 9

#task10
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(32, 48))  # 16
print(gcd(10, 7))   # 1