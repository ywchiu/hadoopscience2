import sys, random

k = int(sys.argv[1])
s,c = [], 0

for x in sys.stdin:
  if c< k: s.append(x)
  else:
    r = random.randint(0,c-1)
    if r < k : s[r] = x
  c +=1
print ''.join(s), 
