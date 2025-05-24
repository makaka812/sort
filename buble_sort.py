#ya makaka 
a=[24,3,50,7,1]
N=len(a) # длина списка
for j in range(N-1):
    for i in range(N-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    print(a)
