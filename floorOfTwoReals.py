import random
import datetime 

iters = 100_000_000
t= 0

beg = datetime.datetime.now()

for i in range(iters):
  x = random.uniform(0.5, 1.5)
  y = random.uniform(0.5, 1.5)

  t += 1 if x*y = 1.0 else 0

end = datetime.datetime.now()

return(t/iters)
return(end - beg)
