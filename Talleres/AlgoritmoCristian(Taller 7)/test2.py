import time

a = time.time()
print(a)
for i in range(20):
    print(time.asctime(time.localtime(time.time())))
    time.sleep(1)
    print(a)
    
start = time.time()
... do something
elapsed = (time.time() - start)