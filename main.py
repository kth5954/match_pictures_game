from cs1graphics import *
from time import *
import random

canvas = Canvas(640, 580)
canvas.setTitle("Memento")

path = "images/"
names = ("1.jpg", "2.jpg", "3.jpg",
         "4.jpg", "5.jpg", "6.jpg")

# 가로 90pixel, 세로 120 pixel jpg 파일을 불러오세요.
# 아이언맨, 토르, 스파이더맨, 캡틴아메리카, 블랙펜서, 헐크

cards = []  # jpeg 이미지
num_pads = []  # 숫자 0~23
correct_list = []  # 맞춘 카드 리스트

tries = 1
# cards initialization
def initialize():
    for i in range(6):
        for k in range(4):
            img = Image(path + names[i])
            temp_tuple = (img, names[i])
            cards.append(temp_tuple)

    for i in range(24):
        card = Layer()
        rect = Rectangle(90, 120, Point(0, 0))
        text = Text(str(i), 18, Point(0, 0))
        card.add(rect)
        card.add(text)
        num_pads.append(card)

    # 2-2-1. shuffle the card list
    random.shuffle(cards)


def print_cards():
    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range(len(num_pads)):
        # 2-2-2. rewrite the condition for visualization.
        if i in correct_list:
            cards[i][0].moveTo(i_w + w, i_h + h)
            canvas.add(cards[i][0])
        else:
            num_pads[i].moveTo(i_w + w, i_h + h)
            canvas.add(num_pads[i])

        w += 100
        if w % 600 == 0:
            w = 0
            h += 130


def is_valid(num1, num2):
    if 0 <= num1 <= 23 and 0 <= num2 <= 23:
        if num1 in correct_list or num2 in correct_list:
            print("The number is already in correct list!")
            return False
        elif num1 == num2:
            print("The numbers are same!")
            return False
        return True
    print("Please input the number included in range 0~23.")
    return False


def check(num1, num2):
    if cards[num1][1] == cards[num2][1]:
        correct_list.append(num1)
        correct_list.append(num2)
        print("Correct!")
        print_cards()
        return True
    else:
        print("Wrong.....")
        print_cards()
        return False


initialize()
for i in range(24):
    correct_list.append(i)
print_cards()
sleep(3)
correct_list = []
print_cards()

print("### Welcome to the Python Memento game!!! ###")
while len(correct_list) < 24:
    if tries == 1:
        s = "1st"
    elif tries == 2:
        s = "2nd"
    elif tries == 3:
        s = "3rd"
    else:
        s = "%dth" % tries
    print("%s try. You got %f pairs." %(s, len(correct_list)/2))
    tries += 1
    num1 = int(input("Input the first card number  : "))
    num2 = int(input("Input the second card number  : "))
    if is_valid(num1, num2) is False:
        continue
    check(num1, num2)
    print_cards()
    sleep(1)
print("### The end!!! ###")
