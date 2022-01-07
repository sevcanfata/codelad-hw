print("-----------reverse name-------------")


def find_palindrome(name):
    if name == name[::-1]:
        print("ıts palindrome")
    else:
        print("no")


names = ("ismet", "ravar", "kukuk", "hara")

for name in names:
    find_palindrome(name)

print("-----check prime number-----")


def check_prime_number(num):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
    return isPrime

primeNums = []
for val in range(2, 15):
    if check_prime_number(val):
        primeNums.append(val)
print(primeNums)

print("-------whether a number in a range--------------")
def whether_num(num, i):
    isinthere = True
    if not num in range(i):
        isinthere = False
    return isinthere

print(whether_num(56, 42))

print("-----reverse string----")
def reverse_string(word):
    word = word[::-1]
    return word
print(reverse_string("sevcan"))

print("-----sum-------")
def summary(list):
    tot = 0
    for i in list:
        tot += i
    return tot

list1=[2,4,6,12,34,2,343,12,45,23,42]
print(summary(list1))
print(sum(list1))

print("----find max value-----")
def find_max_value(list):
    biggest_three = []
    for i in range(3):
        max_val = max(list)
        biggest_three.append(max_val)
        list.remove(max_val)
    return biggest_three

print(find_max_value(list1))

