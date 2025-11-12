import time

a = 10000000
start_time = time.perf_counter()
print("starting time is ", start_time)
for i in range(a):
  print(i)
print("done")

end_time = time.perf_counter()
print("ending time is ", end_time)
total_time = end_time - start_time
print("total time is ", total_time)
print(f"Execution Time: {end_time - start_time:.6f} seconds")
execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
print(f"Execution Time: {execution_time_ms:.2f} milliseconds")
