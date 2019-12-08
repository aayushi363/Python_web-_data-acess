import re


hand = open('regex_sum_313003.txt')
sum = 0

for line in hand:
    numbers = re.findall('[0-9]+', line)
    
    for number in numbers:
        sum = sum + int(number)

print(sum)
