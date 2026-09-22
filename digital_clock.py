import time
def clock():
   my_time=int(input(" for how houch time you wanna slep??"))
   for x in range(my_time,0,-1):
      minutes=int(x/60)%60
      hours=int(x/3600)
      seconds=x%60
      print(f'{hours:02}:{minutes:02}:{seconds:02}')
      time.sleep(1)
   print(" time to wakee upp!!")
clock()
