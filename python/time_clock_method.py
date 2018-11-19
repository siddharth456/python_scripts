# illustrating processor time and wall time

import time

# first the processor time

def procedure():
   time.sleep(2.5)

t0=time.clock()
procedure()
print(time.clock()-t0,"seconds process time")

# the wall time

t1=time.time()
procedure()
print(time.time()-t1,"seconds wall time")
    
