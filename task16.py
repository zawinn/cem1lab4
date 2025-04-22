import matplotlib.pyplot as plt 
import math

def first_func(x) -> float:
    return x*3/2 

def second_func(x) -> float:
    return math.log(x + 5)

def third_func(x) -> float:
    return math.sin(x) + 4

plt.figure(1, figsize=(12, 6))

x = [x + 2 for x in range(10)]
y1 = []
y2 = []

for i in x:
    y1.append(first_func(i))
    y2.append(second_func(i))

plt.plot(x, y1, marker='o', label="first")
plt.plot(x, y2, marker='o', label="second")
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend()
plt.grid(True)

x = [x + 2 for x in range(10)]
y = []

for i in x:
    y.append(third_func(i))

plt.figure(2) 
plt.plot(x, y, color='red', marker='o')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid(True)

plt.show()
