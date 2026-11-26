data = [10, 20, 70, 5, 135, 67, 88, 22]

for i in range(len(data) - 1):
    for j in range(len(data) - 1 - i):
        if data[j] > data [j + 1]:
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

print ("Hasil pengurutan dari terkecil ke terbesar : ")
print (data)
