program=[]
inputable=['<','>','+','-','.',',']
memory=[]
for i in range(20):
    memory.append(0000)
cursor=0
pointer=0
runed=0
helped=0
def typing():
    global cursor,helped
    
    inputed=input()
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
    global cursor,pointer,runed,helped
    
    for i in range(20):
        print()
        
    if runed==0:
        print('type','help','to see helps')
        print('help','と入力でヘルプを見る')
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
        print('< decrease pointer/ポインターの値を1減らす \n> increase pointer/ポインターの値を1増やす \n+ increase pointed memory/ポインターが指すメモリーの値を1増やす\n- decrease pointed memory/ポインターが指すメモリーの値を1減らす \nc< cursor move left/カーソルを左へ移動させる \nc> cursor move right/カーソルを右へ移動させる \ndel delete the character pointed to by the cursor/カーソルの位置の文字を消す')
        helped=0
        

def syori():
    global pointer,program
    
    for i in range(len(program)):
        if program[int(i)]=='<':
            if pointer>0:
                pointer-=1
        elif program[int(i)]=='>':
            if pointer<len(memory):
                pointer+=1
        elif program[int(i)]=='+':
            memory[pointer]+=1
        elif program[int(i)]=='-':
            memory[pointer]-=1
    
    
while True:
    screen()
    typing()