def setup():
    global masume,hyouji,turn,shouhai,wins,pattern
    masume=['_','_','_','_','_','_','_','_','_']
    wins=[
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
        ]
    hyouji=''
    turn='o'
    shouhai='draw'

def display():
    for i in range(100):
        print('')
    print('012')
    print(345)
    print(678)
    print('')
    for j in range(3):
        hyouji=''
        for i in range(3):
            hyouji+=str(masume[j*3+i])
        print(hyouji)

def play_again():
    print('もう一度遊びますかぁ〜ん?(y/n)')
    answer=input()
    if answer != 'y' and answer != 'n':
        print('yかnで答えてね!')
        play_again()
    elif answer=='n':
        exit()
    else:
        setup()
        display()
        main()

setup()
display()

def check():
    global shouhai
    for pattern in wins:
        if masume[pattern[0]]==masume[pattern[1]]==masume[pattern[2]] and masume[pattern[0]]!='_':
            print(turn,'の勝ち')
            shouhai='end'

def main():
    global shouhai
    while shouhai=='draw':
        global turn
        draw=input()
        if draw.isdigit() and 0<=int(draw)<=8 and masume[int(draw)]=='_':
            masume[int(draw)]=turn
            display()
            check()
            if shouhai=='draw':
                if turn=='o':
                    turn='x'
                else:
                    turn='o'
                print('ターン:',turn)
        else:
            print('そ↑こ↓には置けません')
        if '_' not in masume:
            print('引き分けだゾ')
            shouhai='end'
    play_again()
    
main()