import random
import time
def make_enaru():#オリジナルゑなるを作ります
    letter=['あ','い','う','え','お','か','き','く','け','こ','さ','し','す','せ','そ','た','ち','つ','て','と','な','に','ぬ','ね','の','は','ひ','ふ','へ','ほ','ま','み','む','め','も','や','ゆ','よ','わ','ん']
    gainen=''
    for i in range(random.randint(2,7)):
        tuikagainen=letter[random.randint(0,39)]
        gainen=gainen+tuikagainen
    gainen='ゑなる'+gainen
    print(gainen)

def aisatsu():#オープニングです
    print('そんなに言うなら')
    print('ゑなるゲームで勝負しようよ!')
    time.sleep(1)
    print('')
    print('ゑなるに言葉を足して新しい概念で殴り合うよ')
    print('リズムに合わせてオリジナルゑなるで戦おう!')
    print('3・2・1・2・3・2・1・2')
    time.sleep(1)
#以下ゲーム本編
def main():
    shouhai='draw'
    aisatsu()
    while shouhai!='lose':
        make_enaru()
        your_enaru=input('')
        if 'ゑなる' in your_enaru:
            print('')
            print(your_enaru)
        else:
            print('君の負け!')
            time.sleep(0.8)
            print('オリジナルゑなるで戦ってね!')
            print('もう一度ゲームをプレイするには再起動してね!')
            shouhai='lose'
                
main()