import time
import re

x = ['is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks']
start = time.time()
print(sorted(x, key=lambda v: int(re.findall(r"\d+", v)[0])))
end = time.time()
print(end - start)

l = [ 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks', 'is67', 'be3st', 'f23or', 'ge9eks']
start = time.time()
print(sorted(l, key=lambda x: int("".join([i for i in x if i.isdigit()]))))
end = time.time()
print(end - start)



