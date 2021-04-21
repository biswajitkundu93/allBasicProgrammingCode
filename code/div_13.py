num_list = [45, 55, 60, 37, 100, 105, 220, 26, 13, 39, 91, 130, 23, 117, 78]
result = list(filter(lambda x: (x % 13 == 0), num_list))
print("Numbers divisible by 15 are",result)