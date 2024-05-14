def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Пример использования функции
my_list = [1, 3, 5, 7, 9, 11, 13]
element_to_find = 7
result = binary_search(my_list, element_to_find)
if result != -1:
    print(f"Элемент {element_to_find} найден в индексе {result}.")
else:
    print("Элемент не найден.")
