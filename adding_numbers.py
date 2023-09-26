#adding the numbers

number = 0
for numbers in range(1,101):
    number+=numbers
print(number)


# adding even

number = 0
for i in range(0, 101, 2):
    number+=i
print(number)

#or,

total = 0
for j in range(0,101):
    if j%2==0:
        total+=j
print(total)