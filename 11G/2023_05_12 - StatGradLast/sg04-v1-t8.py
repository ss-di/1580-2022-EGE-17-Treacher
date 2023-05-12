import itertools

s = 'ВИКТОР'

all_perm = list(itertools.permutations(s))

all_perm.sort()

print(all_perm[265])


s = 'CBA'

all_perm = list(itertools.permutations(s))

print(all_perm)

