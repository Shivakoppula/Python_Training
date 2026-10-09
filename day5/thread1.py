
import time


def task(name):
	print(f"{name} started")
	time.sleep(2)
	print(f"{name} completed")

start = time.perf_counter()
task("Task 1")
task("Task 2")
task("Task 3")
# total execution time is ~ 6 secs
end = time.perf_counter()


print(f'Total time:{end - start:.2f} secs')