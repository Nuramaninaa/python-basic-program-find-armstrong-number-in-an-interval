#python program to check prime number between interval

low_value = int(input("Enter the low number : "))
upper_value = int(input("Enter the upper number : "))


for number in range (low_value, upper_value + 1):
  sum = 0
  temp = number
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    if number == sum:
       print (number)
    