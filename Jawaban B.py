# EVANDER NAUFAL LASMANTO
# JAWABAN SOAL B

def patern_count(string, obj):
    count = 0
    start = 0
    
    while True:
        start = string.find(obj, start) + 1
        if start > 0:
            count+=1
        else:
            return count

teks = input("Input teks: ")
pattern = input("Input pattern: ")

teks = ''.join(str(x) for x in teks)
pattern = ''.join(str(x) for x in pattern)
print("Result: ", patern_count(teks, pattern))