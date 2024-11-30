from datetime import datetime

s=datetime.now()

d=s.time()

n=d.strftime("%I:%M:%S %p")


print(n)