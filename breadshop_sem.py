#coding=utf-8
import threading
import Queue
import time
import random  

n = 5
m = 20
total = 0
q = Queue.Queue(0);

class Customer(threading.Thread)
    def __init__(self, sem):
       threading.Thread.__init__(self)
       self.threadSemaphore = sem
    def run(self):
    	global customer_count
    	while True:
    		self.number = total++
    		self.threadSemaphore.acquire()  
    		q.put(self.number)
    		print "Customer %d now waiting in the queue..." % (int(self.number))
    		self.threadSemaphore.release()

class Saler(threading.Thread)
    def __init__(self, sem, n):
       threading.Thread.__init__(self)
       self.threadSemaphore = sem
       self.number = n
    def run(self):
    	while True:
    		self.threadSemaphore.acquire()  
    		self.serve = q.pop()
    		print "Saler %d now saling bread to Customer %d..." % (int(self.number), int(self.serve))
    		self.threadSemaphore.release()
          	time.sleep(random.randrange(1, 3))

threads = []
semaphore = threading.Semaphore(1)
for i in range(1, n):  
   threads.append(Customer(semaphore))  
for i in range(1, m):
    threads.append(Saler(semaphore, i))
for t in threads: 
   thread.start()
