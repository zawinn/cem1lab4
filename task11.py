def twoSum(lst, target):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == target and i != j:
                result = (i, j)
                return result

lst = []
lst = input("Введите список элементов: ").split()
target = int(input("Введите искомую сумму: "))
for i in range(len(lst)):
    lst[i] = int(lst[i]) 
lst.sort()

result = twoSum(lst, target)  
print(result)

