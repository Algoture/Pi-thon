import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller
import pygame

pygame.init()
click_sound = pygame.mixer.Sound('Sound.mp3')
thick = -1
cap = cv2.VideoCapture(0)
cap.set(3, 1080)
cap.set(4, 720)

detector = HandDetector(0.8)
keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", " ", "<-", "B", "N","M",","]
]

finalText = ""
keyboard = Controller()

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, tuple(button.pos), tuple([x + w, y + h]), (0, 0, 0), -1)
        cv2.putText(img, button.text, (x + 20, y + 65),cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 3)
    return img

class Button():
    def __init__(self, pos, text, size=[75, 75]):
        self.pos = pos
        self.size = size
        self.text = text

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([110 * j + 50, 110 * i + 50], key))

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    img = drawAll(img, buttonList)

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size
            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, tuple([x - 5, y - 5]), tuple([x + w + 5, y + h + 5]), (255, 255, 0), -1)
                cv2.putText(img, button.text, (x + 20, y + 65),cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                l, _, _ = detector.findDistance(8, 12, img, draw=True)
                print(l)
                if l < 52:
                    if button.text == "<-" :
                        finalText = finalText[:-1]
                        click_sound.play()
                        keyboard.press('\b')
                    else:
                        keyboard.press(button.text)
                        click_sound.play()
                        finalText += button.text
                        sleep(0.15)
    cv2.rectangle(img, tuple([50, 350]), tuple([700, 450]), (0, 0, 0), -1)
    cv2.putText(img, finalText, (60, 430),cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
