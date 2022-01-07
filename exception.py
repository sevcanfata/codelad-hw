a = 12
s = "hello"
try:
    tot = a+s
except TypeError:
    print("except")
finally:
    print("there is an error")
