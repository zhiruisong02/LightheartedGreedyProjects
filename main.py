def digit_sum(n):
  if n<10:
    return n
  else:
    return n%10+digit_sum(n//10)

def run():
  n = input ("Enter an int: ")
  n = int(n)
  n1 = digit_sum(n)
  print(f"sum of digits of {n} is {n1}.")

if __name__=="__main__":
    run()