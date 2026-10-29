program=[]
inputable=['<','>','+','-','.',',','[',']']
memory=[]
for i in range(20):
    memory.append(0000)
cursor=0
pointer=0
runed=0
helped=0
message=''
kekka=[]
def typing():
    global cursor,helped
    ikkatu=[]
    ikkatu_ok=1
    inputed=input()
    if len(inputed)>1:
        for i in inputed:
            if i not in inputable:
                ikkatu_ok=0
                break
            else:
                ikkatu.append(i)
        if ikkatu_ok==1:
            program.extend(ikkatu)
            cursor+=len(ikkatu)
            
                
    new_letter=''
    if inputed in inputable:
        new_letter=inputed
        program.insert(cursor,new_letter)
        cursor+=1
    elif inputed=='c<':
        cursor-=1
    elif inputed=='c>':
        cursor+=1
    elif inputed=='run':
        syori()
    elif inputed=='del':
        if 0<=cursor<len(program):
            program.pop(int(cursor))
    elif inputed=='help':
        helped=1


def screen():
    global cursor,pointer,runed,helped,message,kekka
    
    for i in range(20):
        print()
        
    if runed==0:
        print('type','help','to see helps')
        print('help','と入力でヘルプを見る')
    print(''.join(kekka))
    for i in range(20):
        memory[i]=str(memory[i])
    print(' '.join((memory)))
    for i in range (20):
        memory[i]=int(memory[i])
    draw_cursor=[]
    for i in range(pointer):
        draw_cursor.append(' ')
    draw_cursor.append('^')
    print(' '.join(draw_cursor))
    print()
    print(''.join(program))
    draw_cursor=[]
    for i in range(cursor):
        draw_cursor.append(' ')
    draw_cursor.append('^')
    print(''.join(draw_cursor))
    runed+=1
    if helped==1:
        print("< decrease pointer/ポインターの値を1減らす \n> increase pointer/ポインターの値を1増やす \n+ increase pointed memory/ポインターが指すメモリーの値を1増やす\n- decrease pointed memory/ポインターが指すメモリーの値を1減らす \n[ Jump to the matching ] if the current cell is 0/ポインターが指すメモリーが0なら、対応する ] までジャンプする \n] Jump to the matching [ if the current cell isn't 0/ポインターが指すメモリーが0でないなら、対応する [ までジャンプする \n. Output the character represented by the current cell's value/ポインターが指すメモリーの数をASCIIコードとして読み込む \n, Store the input character's ASCII value in the current cell/入力された文字をASCIIコードとしてポインターが指すメモリーに代入する \nc< cursor move left/カーソルを左へ移動させる \nc> cursor move right/カーソルを右へ移動させる \ndel delete the character pointed to by the cursor/カーソルの位置の文字を消す \n")
        helped=0
    if message!='':
        print(message)
        message=''
        

def syori():
    global pointer,program,memory,message,kekka
    checking=0
    
    memory=[]
    kakko={}
    stakku=[]
    kekka=[]
    for i in range(20):
        memory.append(0000)
    
    for i,command in enumerate(program):
        if command=='[':
            stakku.append(i)
        elif command==']':
            if len(stakku)==0:
                message="missing'['/対応する'['がありません"
                return 
            start=stakku.pop()
            
            kakko[start]=i
            kakko[i]=start
    if len(stakku)>0:
        message="missing']'/対応する']'がありません"
        return
    
    while checking<len(program):
        if program[checking]=='<':
            if pointer>0:
                pointer-=1
        elif program[checking]=='>':
            if pointer<len(memory)-1:
                pointer+=1
        elif program[checking]=='+':
            memory[pointer]+=1
        elif program[checking]=='-':
            memory[pointer]-=1
        elif program[checking]=='[':
            if memory[pointer]==0:
                checking=kakko[checking]
        elif program[checking]==']':
            if memory[pointer]!=0:
                checking=kakko[checking]
        elif program[checking]=='.':
            kekka.append(chr(memory[pointer]))
        elif program[checking]==',':
            comma=input()
            if len(comma)==1:
                comma=ord(comma)
                memory[pointer]=comma
            
        checking+=1
    
    
while True:
    screen()
    typing()