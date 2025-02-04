# fibnoci
# n=res(n-1) +res(n-2)

num=6 

def fib_recursive(n):
  if n==0:
    return 0
  if n==1:
    return 1
  return fib_recursive(n-1) + fib_recursive(n-2)

print(f"fibnocci of {num} is {fib_recursive(num)}")