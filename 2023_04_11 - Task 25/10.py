#012345678
#1?34567?9
# r1    r2

for r1 in range(10):
    for r2 in range(10):
        x = int("1" + str(r1) + "34567" + str(r2) + "9")
        x = int(f"1{r1}34567{r2}9")
        if x % 17 == 0:
            print(x, x // 17)
