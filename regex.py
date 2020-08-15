import re
file = open('regex_sum_887471.txt')
input = file.read()

numbers = re.findall('[0-9]+',input)
numbers = [int(number) for number in numbers]
sums = sum(numbers)

print(sums)
