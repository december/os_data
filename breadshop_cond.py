#coding=utf-8
import threading
import Queue
import time
import random  

n = 5
m = 20
total = 0
cond = threading.Condition()
q = Queue.Queue(0);

class Customer(threading.Thread)
    def __init__(self):
       threading.Thread.__init__(self)
    def run(self):
    	global customer_count
    	while True:
    		self.number = total++
        if cond.acquire():
    		  q.put(self.number)
    		  print "Customer %d now waiting in the queue..." % (int(self.number))
          cond.notify()
    		cond.release()

class Saler(threading.Thread)
    def __init__(self, n):
       threading.Thread.__init__(self)
       self.number = n
    def run(self):
    	while True:
    		if cond.acquire(): 
    		  self.serve = q.pop()
    		  print "Saler %d now saling bread to Customer %d..." % (int(self.number), int(self.serve))
    		  cond.notify()
        cond.release()
        time.sleep(random.randrange(1, 3))

threads = []
semaphore = threading.Semaphore(1)
for i in range(1, n):  
   threads.append(Customer())  
for i in range(1, m):
    threads.append(Saler(i))
for t in threads: 
   thread.start()
      