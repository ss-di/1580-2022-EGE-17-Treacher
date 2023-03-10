import sys
sys.stdin = open('1.txt')

sch = {}
n_sch = int(input())
for i in range(n_sch):
    id, name = input().split()
    id = int(id)
    sch[id] = name

clas = {}
n_class = int(input())
for i in range(n_class):
    id, id_s, name = input().split()
    id = int(id)
    id_s = int(id_s)
    clas[id] = (id_s, name)

use_s = set()
use_c = set()
ans = []
n = int(input())
for i in range(n):
    id, id_c, name, sname = input().split()
    id = int(id)
    id_c= int(id_c)
    id_s = clas[id_c][0]
    ans.append([id_s, sch[id_s], id_c, clas[id_c][1], id, name, sname])
    use_s.add(id_s)
    use_c.add(id_c)

for id_c in clas.keys():
    if id_c not in use_c:
        id_s = clas[id_c][0]
        ans.append([id_s, sch[id_s], id_c, clas[id_c][1] ])
        use_s.add(id_s)
        
for id_s in sch.keys():
    if id_s not in use_s:
        ans.append([id_s, sch[id_s] ])

ans.sort()

for i in ans:
    print(*i)