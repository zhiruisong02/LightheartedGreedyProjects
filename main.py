def digit_sum(n):
  if n<10:
    return n
  else:
    r = n//10
    m = n%10
    return m+digit_sum(r)

def run():
  n = input ("Enter an int: ")
  n = int(n)
  n1 = digit_sum(n)
  print(f"sum of digits of {n} is {n1}.")

if __name__=="__main__":
    run()