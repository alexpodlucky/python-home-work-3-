def digit_sum(n):
  if n < 10:
    return n
  else:
    return ((n % 10) + digit_sum(n // 10))
def run():
  num = int(input('Enter an int: '))
  print(f'sum of digits of {num} is {digit_sum(num)}.')
  

if __name__ == '__main__':
  run()