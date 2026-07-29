def setup():
    global odai,odai_list,guess,life
    odai_list=[]
    guess=[]
    life=10
    #お題を決めよう
    print('お題を入力ゥゥゥゥゥ!there!')
    print('全て小文字で入力して下さい')
    odai=input()
#一文字ずつリストへぶちこむ
    for i in range(0,len(odai)):
        odai_list.append(odai[i])
#隠せ!
    for i in range(100):
        print('')

#予想した文字が入っているか
def letter_check():
    global hyouji
    hyouji=''
    for i in range(len(odai_list)):
        if odai_list[i] in guess:
            hyouji=hyouji+odai_list[i]
        else:
            hyouji=hyouji+'_'
        hyouji=hyouji+' '
    print(guess)
    print('')
    print(hyouji)

global shouhai
shouhai='draw'

#以下本編
def ask():
    print('もう一度プレイしますか?(y/n)')
    play_again=input()
    if play_again!='y' and play_again!='n':
        print('yかnで答えてね!')
        ask()
    else:
        if play_again=='y':
            setup()
            main()
        else:
            exit()
def main():
    global life,shouhai
    while shouhai!='lose' and life>0:
        print('ライフ:',life)
        print('小文字アルファベットを一つ入力し、推測')
        add_letter=input()
        if len(add_letter) != 1 or not add_letter.islower() or not add_letter.isalpha() or add_letter in guess:        
            print('小文字アルファベット1文字を入力して下さい!')
            print('一度入力した文字は入力しないでね!')
            print('')
        else:
            guess.append(add_letter)
            print('')
            if add_letter not in odai:
                life=life-1
        if shouhai=='draw':
            letter_check()
        if '_' not in hyouji:
            print('クリア!')
            print('お題は',odai,'でした')
            ask()
    print('ゲームオーバー!')
    print('もう一度プレイするには再起動してね!')
    print('')
    print('ちなみに答えは',odai,'でした')
    ask()
setup()
main()