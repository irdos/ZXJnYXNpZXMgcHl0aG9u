import random
print("Bale diastasi tetragwnou pou tha dimiourgithei:")
hm = 1
while hm == 1:
    megethostetragwnou = int(input())
    if megethostetragwnou >= 4:
        break
    else:
        print("Bale arithmo => 4:")
print("Plithos thesewn: ", megethostetragwnou**2)
rows, cols = (megethostetragwnou, megethostetragwnou) 
p = 0
orizontiacount = 0
kathetacount = 0
diagwniacount = 0
while p < 100:

    tetragwno = [[0 for i in range(cols)] for j in range(rows)] 
    for row in tetragwno: 
        print(row) 
    i = 0
    misomegethostetragwnou = megethostetragwnou**2/2
    
    if (misomegethostetragwnou % 2) != 0:
        misomegethostetragwnou += 0.5
    


    while i < (misomegethostetragwnou):
            seira = random.randint(0, megethostetragwnou - 1)
            stili = random.randint(0, megethostetragwnou - 1)
            
            if tetragwno[seira][stili] != 1:
                tetragwno[seira][stili] = 1
                i += 1

    for row in tetragwno: 
        print(row) 
    i = 0
    j = 0
    
    while i < (megethostetragwnou - 1):
        j = 0
        while j < (megethostetragwnou - 1):
            try:
                if (tetragwno[i][j] == 1 and tetragwno[i][j + 1] == 1 and tetragwno[i][j + 2] == 1 and tetragwno[i][j + 3] == 1):
                    orizontiacount += 1
            except:
                pass
            
            try:    
                if (tetragwno[i][j] == 1 and tetragwno[i + 1][j] == 1 and tetragwno[i + 2][j] == 1 and tetragwno[i + 3][j] == 1):
                    kathetacount += 1
            except:
                pass
            try:
                if (tetragwno[i][j] == 1 and tetragwno[i + 1][j + 1] == 1 and tetragwno[i + 2][j + 2] == 1 and tetragwno[i + 3][j + 3] == 1):
                    diagwniacount +=1
            except:
                pass
            try:
                if (tetragwno[i][j] == 1 and tetragwno[i - 1][j - 1] == 1 and tetragwno[i - 2][j - 2] == 1 and tetragwno[i - 3][j - 3] == 1):
                    diagwniacount +=1
            except: 
                pass
                
            
            j += 1
            
        i += 1

    
    p += 1
mesosorosorizontia = orizontiacount / 100
mesosoroskatheta = kathetacount / 100
mesosorosdiagwnia = diagwniacount / 100
mesosorosola = mesosorosdiagwnia + mesosoroskatheta + mesosorosorizontia
print("Mesos oros orizontia: ", mesosorosorizontia)
print("Mesos oros katheta: ", mesosoroskatheta)
print("Mesos oros diagwnia: ", mesosorosdiagwnia)
print("Mesos oros ola: ", mesosorosola)