def count(alf, n, s):
    if n == 0: # строка составлена
        if s.count("К") == 1:  
            return 1
        else:
            return 0
    cnt = 0
    for ch in alf: # будем добавлять все символы по очереди
        cnt += count(alf, n - 1, s + ch)
    return cnt

print(count("ШКОЛА", 3, ""))
