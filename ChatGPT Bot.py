import time

print('Hello,My name is ChatGPT Bot')
time.sleep(1.5)
print('I was created in 2023,by Rby')
time.sleep(1.5)
print('What language do you want me to speak?')
time.sleep(1.5)
print('如果你想要简体中文，输入C')
print('If you want me to speak English,type E')
l = input()
if l == 'C':
    print('你叫什么名字？')
    name = input()
    time.sleep(1.5)
    print(name, ',多好的一个名字啊')
    print('你相信我能数数吗？让我来证明给你看')
    num = int(input("请输入一个数："))
    for i in range(num + 1):
        time.sleep(0.7)
        print(i)
    print('你惊讶吗！！哈哈哈')
    print('你的兴趣爱好是什么？能和我分享一下吗？')
    like = input()
    for i in range(len(like)):
        print(like[i])
    if like == '吃屎':
        print('请你文明一点，谢谢')
    elif like == '睡觉':
        print('你真懒！！')
    elif like == '吃饭':
        print('真无聊--------------')
    else:
        print('真是一项非常好的爱好呢！')
    print('你喜欢编程吗？')
    a = input()
    if a == '喜欢':
        print('让我来考考你把！')
        print('在Python中，如何使用for循环遍历一个列表')

        print('a) for each in list:')
        print('b) for i in range(len(list)):')
        print('c) for i in list:')
        time.sleep(1.0)
        answer1 = input()
        max_ch = 2
        ch = 0

        while ch < max_ch:
            answer1 = input('请输入答案：')
            if answer1 == 'c':
                print('恭喜你答对了！！')
                time.sleep(1.0)
                break
            else:
                print('再试试')
                ch += 1

        if ch == max_ch:
            print('很遗憾，尝试次数已用完。')
        print('答案对错并没有关系，我还要去服务别人了，886！！！')
    else:
        print('真的吗？作为一个人工智能助手，虽然我没有情感，但是我此时也感受到了伤心呜呜呜呜呜呜-')
        time.sleep(1.0)
        time.sleep(1.0)
        print('我们改天再聊吧，886！！！')
if l == 'E':
    print('What is your name,tell me please')
    name = input()
    time.sleep(1.0)
    print(name, ',What a wonderful name it is')
    print('Do you believe that I can count? Let me prove it !')
    num = int(input("Type in a number："))
    for i in range(num + 1):
        time.sleep(0.7)
        print(i)
    print('Are you amazed!haha!')
    time.sleep(1.0)
    print('What are your hobbies and interests? Can you share them with me?')
    like = input()
    for i in range(len(like)):
        print(like[i])
    if like == 'eating poap':
        print('Could you please be more polite? Thank you')
    elif like == 'sleep':
        print('You are so lazy！！')
    elif like == 'eat':
        print('So boring--------------')
    else:
        print('That is indeed a very good hobby！')
    print('Do you like Programming')
    a = input()
    if a == 'yes':
        print('Let me test you!')
        print('In Python, how to use a for loop to iterate through a list.')

        print('a) for each in list:')
        print('b) for i in range(len(list)):')
        print('c) for i in list:')
        time.sleep(1.0)
        answer1 = input()
        max_ch = 2
        ch = 0

        while ch < max_ch:
            answer1 = input()
            if answer1 == 'c':
                print('congratulations！')
                time.sleep(1.0)
                break
            else:
                print('Try again')
                ch += 1

        if ch == max_ch:
            print('Unfortunately, the number of attempts has been exhausted.')
            time.sleep(1.0)
        print('It does not matter if the answer is right or wrong, I still need to go and assist someone '
              'else.，bye~！！！')
    else:
        print('Really? As an artificial intelligence assistant, even though I do not have emotions, I can still '
              'sense sadness at this moment. Sob sob sob  sob sob')
        print('Let"s talk later，bye~！！！')


def waving_hand():
    for _ in range(3):
        print("     o/")
        print("     /|")
        print("     / \\")

        time.sleep(0.5)

        print("\033[H\033[J", end="", flush=True)

    for x in range(2):
        print(" " * x + "o/")
        print(" " * x + "/|")
        print(" " * x + "/ \\")

        time.sleep(0.5)
        print("\033[H\033[J", end="", flush=True)

    print("   o/")
    print("   /|")
    print("   / \\")


waving_hand()
time.sleep(2.0)
print('-------License-------')
print('This computer program is protected by international copyright conventions. Any unauthorized copying or '
      'distribution of this program or any part thereof will be subject to severe civil and criminal penalties, '
      'and will be prosecuted to the maximum extent permitted by law')
print(
    '本计算机程序受国际版权公约保护，如果未经授权而擅自复制或传播本程序或其中的任何部分，将受到严厉的民事及刑事制裁，还将在法律许可的范围内受到最大程度的起诉')
print('Copyright (c)2023 rbyAI Inc.')
time.sleep(1.0)
print('----------------------------')
time.sleep(1.0)
print('    All Right Reserved')
