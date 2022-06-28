# EVANDER NAUFAL LASMANTO
# JAWABAN SOAL A

arrayData = ['12','9','30','A','M','99','82','J','N','B']
 
alphabets = []
numerics = []

for sortData in arrayData:
    if sortData.isnumeric():
        numerics.append(sortData)
    else:
        alphabets.append(sortData)
        
for i in range(0, len(numerics)) :
	numerics[i] = int(numerics[i])
	
sortResult = sorted(alphabets) + sorted(numerics)
print("Result: " + str(sortResult))