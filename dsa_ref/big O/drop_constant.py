import time


def print_items(n):
    start_time = time.perf_counter()  # Start the timer

    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

    end_time = time.perf_counter()  # End the timer
    print(f"Execution Time: {end_time - start_time} seconds")
    execution_time_ms = (end_time -
                         start_time) * 1000  # Convert to milliseconds
    print(f"Execution Time: {execution_time_ms:.2f} milliseconds")


print_items(10)
# o(n+n) o(2n) we can drop 2 answer is o(n)
