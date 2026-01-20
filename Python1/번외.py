a = 10
b = a
b = 20

print(a)  # 10
print(b)  # 20
print(a == b)  # 10 == 20 -> False

# -------------------------------------
x = [1, 2, 3]
y = x
y[0] = 99

print(x)
print(y)

