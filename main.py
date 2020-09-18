def digit_sum(n):
  if n <= 0:
    return 0
  else:
    return ((n % 10) + digit_sum(int(n / 10)))
def run():
  num = int(input('Enter an int: '))
  print('sum of digits of '+ str(num) + ' is', int(digit_sum(num) + "."))
  

if __name__ == '__main__':
  run()