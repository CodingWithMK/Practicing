###Calculating the multiplication and sum of two numbers###

number1 = 20
number2 = 30
number3 = 40
number4 = 30

solution1 = (number1 * number2)

if solution1 <= 1000:
    print(solution1)

solution2 = (number3 + number4)
print(solution2)

###Calculating the multiplication and sum of two numbers in a function###

def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        sum = (num1 + num2)
        return sum

result = multiplication_or_sum(20, 30)
print("The result is", result)

result = multiplication_or_sum(40, 30)
print("The result is", result)

###Sum of current and previous number###

previous_num = 0
current_num = 0 
sum = current_num + previous_num

for i in range(10):
    current_num = i
    previous_num = (i - 1) 
    sum = (current_num + previous_num)

    print("Current Number:", (current_num), "Previous Number:", (previous_num), "Sum:", (sum))

previous_num = i


###Printing Chareacters From A Strings Index###

print_a_character_from_a_string = input("Enter a word: ")

print(len(print_a_character_from_a_string))

for i in range(0,7,2):
    print(print_a_character_from_a_string[i])


###Removing Characters From A String###

remove_chars = 'pynative'

print(remove_chars[4:])
print(remove_chars[2:])


###Checking If First And Last Number Is The Same###

number_x = [10, 20, 30, 40, 10]
number_y = [75, 65, 35, 75, 30]

def compare_numbers_x(number_x):

    if number_x[0] == number_x[4]:
        result = True
    else:
        result = False
    
    return result

print(compare_numbers_x(number_x))

def compare_numbers_y(number_y):

    if number_y[0] == number_y[4]:
        result = True
    else:
        result = False
    
    return result

print(compare_numbers_y(number_y))


###Displaying Numbers From A List Divisible By 5###


numbers = [10, 20, 33, 46, 55]

print(numbers)

def DivisibleByFive(numbers):
    for index in numbers:
        result = print(index // 5)
    return result

print(DivisibleByFive(numbers))

print(numbers[0])
print(numbers[1])
print(numbers[4])


###Display The Count Of Given Substrings In A String###

str_x = "Emma is a good Developer. Emma is a writer"

print("The substring Emma appeared", str_x.count("Emma"), "times.")


###Print A Pattern From 1 To 5###
rows = 5
for i in range(rows + 1):
    for j in range(i):
        print(i, end='')
    print('')


###Check If The Given Number Is  A Palindrome###
my_num = '323'

def reversed_num(my_num):
    if my_num[::-1] == my_num:
        return True
    else:
        return False

print(reversed_num(my_num), "The reversed number of 323 is a palindrome!")


###Create A New List From Other Lists###
list_1 = [10, 20, 25, 30, 35]
list_2 = [40, 45, 60, 75, 90]

result_list = []

for index in list_1:
    if index % 2 != 0:
        result_list.extend(list_1)
    
for index in list_2:
    if index % 2 == 0:
        result_list.extend(list_2)
           

print(result_list)


def CreateNewList(list_1, list_2):
    for index in list_1:
        if index % 2 != 0:
            result_list.append(index)
    
    for index in list_2:
        if index % 2 == 0:
            result_list.append(index)

    return result_list    

print(CreateNewList(list_1, list_2))


###Extract Each Digit From An Integer In The Reverse Order###
my_num = "7536"
my_num_rev = ""

def ReverseNum(my_num_rev):
    if type(my_num) == str:
        my_num_rev = " ".join(my_num)
        return str(my_num_rev)[::-1]

    
print(ReverseNum(my_num_rev))


###Calculating Income Tax###

income_1 = 10000
income_2 = 10000
income_3 = 25000

for i in range(income_2):
    i = income_2 * (10 / 100)
for j in range(income_3):
    j = income_3 * (20 / 100)

sum = i + j
print(sum)


###Printing The Multiplication Table From 1 To 10###
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=' ')
        
    print('')


###Prtinting A Downward HalfPyramid Pattern###
rows = 5
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print('*', end='')
    print('')


###Writing A Function That Returns An Integers Raise To The Power Of A Exponent###

#Case1
def RaiseToPower(base_num, exp_num):
    for num in range(base_num):
        result = base_num ** exp_num
        return result  
        

print(RaiseToPower(2, 5))

#Case2
def RaiseToPower_1(base_num1, exp_num1):
    for num in range(base_num1):
        result = base_num1 ** exp_num1
        return result

print(RaiseToPower_1(5, 4))