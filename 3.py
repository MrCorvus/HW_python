odd_number = list(range(1, 1000, 2))
for idx in range(len(odd_number)):
    odd_number[idx] **= 3

x = int(odd_number[idx])
sum_of_digits = 0
total_amount = 0
total_amount2 = 0

for i in odd_number:
    x = i
    while i > 0:
        y = i % 10
        sum_of_digits += y
        i //= 10
    if sum_of_digits % 7 == 0:
        sum_of_digits = 0
        total_amount += x
    if sum_of_digits % 7 > 0:
        sum_of_digits = 0
        continue

for i in odd_number:
    x = i + 17
    while x > 0:
        y = x % 10
        sum_of_digits += y
        x //= 10
    if sum_of_digits % 7 == 0:
        total_amount2 += (i + 17)
    if sum_of_digits % 7 > 0:
        sum_of_digits = 0
        continue

print(total_amount)
print(total_amount2)