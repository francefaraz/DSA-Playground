import time


def print_items(n):
  start_time = time.perf_counter()
  for i in range(n):
    for j in range(n):
      print(i, j)
  end_time = time.perf_counter()
  print(f"time taken is {end_time-start_time} in seconds")
  print(f"time taken is {(end_time-start_time)*1000:.2f} in milliseconds")


print_items(10)
