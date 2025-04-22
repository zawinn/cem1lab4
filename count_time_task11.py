import time

def twoSum(lst, target):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == target and i != j:
                result = (i, j)
                return result

lst = []
for i in range(1, 1000000):
    lst.append(i)

target = int(input("Введите искомую сумму: "))
for i in range(len(lst)):
    lst[i] = int(lst[i]) 
lst.sort()

start = time.time()
result = twoSum(lst, target)  
end = time.time()
print(f"{end - start}")
print(result)

