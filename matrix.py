A = [
    [1, 4, 7, 3, 2],
    [5, 3, 8, 1, 4],
    [1, 3, 5, 7, 2],
    [4, 5, 6, 3, 1],
    [5, 4, 3, 2, 1]
]

B = [
    [7, 8, 9, 3, 1],
    [6, 7, 5, 1, 2],
    [5, 6, 4, 2, 3],
    [4, 8, 7, 5, 4],
    [3, 9, 6, 7, 5]
]

hasil_perkalian = []

for i in range(5):
    baris = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += A[i][k] * B[k][j]
        baris.append(total)
    hasil_perkalian.append(baris)

print("Hasil = ")
for baris in hasil_perkalian:
    print(baris)
