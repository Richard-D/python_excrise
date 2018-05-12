import time,threading

def loop():
    print("name %s" % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print("thread %s >>> %s " %(threading.current_thread().name,n))
        time.sleep(1)
    print("Thread %s ended." %threading.current_thread().name)

t = threading.Thread(target=loop,name="LoopThread")
t.start()
t.join()
