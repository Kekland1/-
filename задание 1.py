#1 задание
def custom_sort(A, B):
    index_map = {num: i for i, num in enumerate(B)}
    A.sort(key=lambda x: (index_map.get(x, len(B)), -x))
    return A
# Пример 
A = [2, 1, 4, 3, 6, 5]
B = [1, 3, 5]
result = custom_sort(A, B)
print(result)
