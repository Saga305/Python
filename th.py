import threading as th
#import a timeStamp module to gettime according to the time zone
import timeStamp as ts

l = []
lock = th.Lock()

def update_time(timeZone):
	#lock = threading.Lock() #What if we create a lock instance here?
	#print("lock address: ",lock)

	print("Thread {} is going to acqiure a lock".format(th.current_thread().getName()))

	#acquiring a lock
	lock.acquire()
	print("Thread {} has acquired a lock".format(th.current_thread().getName()))
	
	#append a timestamp in a list
	l.append(ts.getTimeStamp(timeZone))

	print("Thread {} is going to release a lock".format(th.current_thread().getName()))
	#releasing a lock
	lock.release()
	
 
if __name__ == "__main__":
	print("Thread {} is executing.".format(th.current_thread().getName()))
	# creating thread AEST
	aest = th.Thread(target=update_time,name="AEST", args=(ts.ausZone,))

	# creating thread MMT
	mmt = th.Thread(target=update_time,name="MMT", args=(ts.istZone,))

	# creating thread EST
	est = th.Thread(target=update_time,name="EST", args=(ts.estZone,))
 
	# starting thread AEST
	aest.start()

	# starting thread MMT
	mmt.start()

	# starting thread EST
	est.start()
 
	# wait until thread AEST is completely executed
	aest.join()

	# wait until thread MMT is completely executed
	mmt.join()

	# wait until thread EST is completely executed
	est.join()

	#Print list
	print(l)
