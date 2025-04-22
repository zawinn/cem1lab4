import time

def twoSum(lst, target):
    temp = {}
    result = {}
    for i, v in enumerate(lst):
        temp_value = target - v
        if temp_value in temp:
            result[temp[temp_value]] = v - 1
        else:
            temp[v] = i
    result = sorted(result.items())
    return next(iter(result))

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