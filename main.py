def digit_sum(n):
   if n <= 0:
       return 0
   else:
       return ((n % 10) + digit_sum(n / 10))

num = int(input('Enter an int : '))
print('Sum of digits of '+ str(num) + ' is', int(digit_sum(num)))