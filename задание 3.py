##3 задание
def max_sum_of_two(nums):
    nums.sort()
    return nums[-1] + nums[-2]

# Пример использования функции
my_list = [3, 7, 2, 10, 4]
result = max_sum_of_two(my_list)
print(result)
