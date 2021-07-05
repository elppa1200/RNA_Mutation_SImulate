####script to simulate evolution of a single DNA_sequence###
#         code by Alexander Kehr, 2015                     #
###         GNU General Public License                   ###
import random, time

dna_sequence = 'AGCTAGTCGACTACGTAGCATGTCAGCTGACATGTCGACT'
init_dna = dna_sequence
ticks = '10000'
lendna = len(dna_sequence)
lendna = int(lendna)
change_IDs = []
counter = 0

a = []

def dna_changeH(lendna):
    return(random.randrange(1, lendna))           

def dnaID (lendna):

    result = "false"
    
    while (result == "false"):
    
        ID = random.randrange(1, lendna)
    
        if ID in change_IDs:
            pass
    
        else:
            result = "true"
            change_IDs.append(ID)

def changeInto():
    into = random.randrange(0, 4)
    if into == 0:
        return("U")
    elif into == 1:
        return("G")                              
    elif into == 2:
        return("T")
    elif into == 3:
        return("C")

def wipevalues():
   change_IDs = []

def checkdna(dna_sequence):
    if 'A' in dna_sequence:
        pass
    elif 'G' in dna_sequence:
        pass
    elif 'C' in dna_sequence:
        pass
    elif 'T' in dna_sequence:
        pass
    else:
        return('err')

for i in range(int(ticks)):
    
    if checkdna(dna_sequence) == 'err': #예외 처리
        print("DNA contains errors: " + dna_sequence)
        break
    
    counter = counter + 1
    print("[STAGE " + str(counter) + "]") #Epoch
    
    epoch = dna_changeH(lendna) # haufigkeit는 돌연변이? 무슨 사건의 횟수 
    #랜덤한 수 list를 받는 걸 보니 각 DNA에 변이 일으키는 함수일듯 
    print("Epoch:" + str(epoch))
    
    for i in range(epoch): # 변이 횟수만큼
        dnaID(lendna)
    
    print('Change Index : ' + str(change_IDs))
    ch_Index=[]
    for i in range(len(change_IDs)):
        ch_Index.append(dna_sequence[change_IDs[i]])

    print('Changed : ' + str(ch_Index))

    
    for i in range(epoch):

        ch_ID = change_IDs.pop()

        if dna_sequence[ch_ID] == 'A':
            ch_ID1 = ch_ID - 1
        
            DNA_part1 = dna_sequence[0:ch_ID1]
            DNA_part2 = dna_sequence[ch_ID:len(dna_sequence)]
            if random.randrange(0, 11) >= 7:
                dna_sequence = DNA_part1 + 'U' + DNA_part2
            else : 
                dna_sequence = DNA_part1 + changeInto() + DNA_part2
        
        elif dna_sequence[ch_ID] == 'G':
            ch_ID1 = ch_ID - 1
        
            DNA_part1 = dna_sequence[0:ch_ID1]
            DNA_part2 = dna_sequence[ch_ID:len(dna_sequence)]
            if random.randrange(0, 11) >= 7:
                dna_sequence = DNA_part1 + 'A' + DNA_part2
            else : 
                dna_sequence = DNA_part1 + changeInto() + DNA_part2

        elif dna_sequence[ch_ID] == 'C':
            ch_ID1 = ch_ID - 1
        
            DNA_part1 = dna_sequence[0:ch_ID1]
            DNA_part2 = dna_sequence[ch_ID:len(dna_sequence)]
            if random.randrange(0, 11) >= 7:
                dna_sequence = DNA_part1 + 'T' + DNA_part2
            else : 
                dna_sequence = DNA_part1 + changeInto() + DNA_part2
        
        elif dna_sequence[ch_ID] == 'T':
            ch_ID1 = ch_ID - 1
        
            DNA_part1 = dna_sequence[0:ch_ID1]
            DNA_part2 = dna_sequence[ch_ID:len(dna_sequence)]
            if random.randrange(0, 11) >= 7:
                dna_sequence = DNA_part1 + 'G' + DNA_part2
            else : 
                dna_sequence = DNA_part1 + changeInto() + DNA_part2

        elif dna_sequence[ch_ID] == 'U':
            ch_ID1 = ch_ID - 1
        
            DNA_part1 = dna_sequence[0:ch_ID1]
            DNA_part2 = dna_sequence[ch_ID:len(dna_sequence)]
            if random.randrange(0, 11) >= 7:
                dna_sequence = DNA_part1 + 'A' + DNA_part2
            else : 
                dna_sequence = DNA_part1 + changeInto() + DNA_part2
    
            
        

        if init_dna[i] != dna_sequence[i] :
            a.append(dna_sequence[i])
    print("")
    print("##new DNA: " + dna_sequence + "##")
    print("")

    change_IDs = []
    
everage = len(a)
everage_A = a.count('A')/everage * 100
everage_U = a.count('U')/everage * 100
everage_G = a.count('G')/everage * 100
everage_C = a.count('C')/everage * 100
everage_T = a.count('T')/everage * 100
percen = everage_U + everage_G + everage_C + everage_T + everage_A


print('initial rna : '+ init_dna + '\nchanged rna : ' + dna_sequence)

print('everage : '+str(everage)+'\nU : ' + str(round(everage_U, 1))+'\nG : ' + str(round(everage_G, 1))+'\nC : ' + str(round(everage_C, 1))+'\nT : ' + str(round(everage_C, 1)) + '\nA : ' + str(round(everage_A, 1)))
print('total percentage : ' + str(percen))


# epoch 5000개 주고 한 epoch당 초기 dna랑 변경 dna 대조해서 달라진 dna 추출한 다음에 달라지는 경향 조사 