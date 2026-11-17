# import os 
# print(os.getcwd())
# os.chdir("C:/Users/mitta/OneDrive/Desktop/my pdfs/Presentations/Deviathon/Ai Frontier")
# print(os.listdir("."))
# os.makedirs("demo/sub",exist_ok=True)
# print(os.path.join('demo','file.txt'))

# import sys
# print(type(sys.argv))
# print(sys.version)
# print(sys.argv)
# sys.exit(0)

# from math import *

# print(sqrt(89))
# print(ceil(-0.89))
# print(pow(32,7))
# print(floor(12.999999))
# print(round(12.99999))
# print(pow(2,3))
# print(log(e))
# print(sin(radians(30)))
# print(degrees(atan(1)))
# print(degrees(acos(0.5)))
# print(asin(1))

# from random import *

# print(randint(1,10))
# print(random())
# colors=["red","blue","green"]
# print(choice(colors))
# shuffle(colors)
# print(colors)


# import datetime

# now= datetime.datetime.now()
# print(now)
# formatted=now.strftime("%Y-%m-%D %H:%M:%S")
# print("Formatted:",formatted)
# tomorrow=now+datetime.timedelta(days=1)
# print("Tomorrow:",tomorrow.date())


# from collections import Counter,defaultdict,deque

# c=Counter("banana")
# print(c)
# dd=defaultdict(int)
# dd["x"]+=1
# dd["y"]+=2
# print(dd["x"],dd["y"])

# dq=deque([1,3,4,5,6])
# dq.appendleft(99)
# dq.append(0)
# print(dq)
# print(type(dq))

# from collections import namedtuple

# person=namedtuple("Person",['name','age','city'])
# p1=person("Alice",30,"New York")
# p2=person ("raghav",40,"America")
# print(p1.name,p1.age,p1.city)
# print(p2[0],p2[1],p2[2])
# name,age,city=p1
# print(name,age,city)