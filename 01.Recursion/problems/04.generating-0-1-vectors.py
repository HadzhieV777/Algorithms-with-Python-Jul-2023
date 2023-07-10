# 4. Generating 0/1 Vectors
def gen01(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[index] = num
        gen01(index + 1, vector)


n = int(input())

vector = [0] * n

gen01(0, vector)
