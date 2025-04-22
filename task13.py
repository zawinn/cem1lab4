def twoSum(lst, target):
    temp = {}
    result = {}
    for i, v in enumerate(lst):
        temp_value = target - v
        if temp_value in temp:
            result[temp[temp_value]] = v
        else:
            temp[v] = i
    result = sorted(result.items())
    return result

lst = []
lst = input("Введите список элементов: ").split()
target = int(input("Введите искомую сумму: "))
for i in range(len(lst)):
    lst[i] = int(lst[i]) 
lst.sort()

result = twoSum(lst, target)
print(result)