n=0
s='ШКОЛА'
for a in s:
  for b in s:
    for c in s:
        if (a+b+c).count('К')==1:
          n+=1
print(n)
