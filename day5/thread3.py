import threading

balance = 1000
lock = threading.Lock()


def f1_deposit():
	global balance
	with lock:
		balance = balance + 500


def f2_withdraw():
	global balance
	with lock:
		balance = balance - 200


t1 = threading.Thread(target=f1_deposit)
t2 = threading.Thread(target=f2_withdraw)
t1.start()
t2.start()
t1.join()
t2.join()
print(f"Balance : {balance}")