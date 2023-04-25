import time
import numpy as np
import cv2
import mediapipe as mp
import datetime
import os
from PIL import Image

# from math import dist

# class handDetector():
#     def __init__(self, ):
# prathmesh7840@gmail.com

camera_port = 0
camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
x2_coordinate = []
x1_coordinate = []

handLms = 0
check = True
initial_check = True

success, image = camera.read()
imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = hands.process(imgRGB)

# def initial_check_def():
#     if True:
#         if results.multi_hand_landmarks:
#             for handLms in results.multi_hand_landmarks:
#                 for id, lm in enumerate(handLms.landmark):
#                     # print(f"Id: {id},Lm: {lm}")
#
#                     h, w, c = image.shape
#                     cx, cy = int(lm.x * w), int(lm.y * h)
#
#                     initial_coordinates = (cx, cy)
#                 return initial_coordinates
#
#
#
# if initial_check:
#     coordinates = initial_check_def()
#     initial_check = False
#     print(coordinates)
current_state = 'middle'
previous_state = 'middle'
while True:
    success, image = camera.read()
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
# initial_check = np.array((hand.landmark[mp_hands.HandLandmark.WRIST].x, hand.landmark[mp_hands.HandLandmark.WRIST].y))
    # print(results.multi_hand_landmarks)

    # image1 = Image.open('F:\Gesture_Detection\ss\12531-istock-637790866 (1).jpg')
    # image1.show()
    # cv2.imshow("image", image1)
    #     if results.multi_hand_landmarks:
    #         for handLms in results.multi_hand_landmarks:
    #             for id, lm in enumerate(handLms.landmark):
    #                 #print(f"Id: {id},Lm: {lm}")
    #                 h, w, c = image.shape
    #                 cx, cy = int(lm.x*w), int(lm.y*h)
    #                 initial_coordinates = (cx, cy)
    #                 print(initial_coordinates)
    #
    # print(initial_check)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(f"Id: {id},Lm: {lm}")
                h, w, c = image.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                cpx, cpy = int(lm.x*100), int(lm.y*100)
                # cv2.imshow("detected", mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS))
                #print(id, cx, cy)

                # cv2.line(image, (cx, cy), (cx, cy), (255, 0, 255), 25)
                #initial_check = np.array(
                #   (hands.landmark[mp_hands.HandLandmark.WRIST].x, hands.landmark[mp_hands.HandLandmark.WRIST].y))

                if id == 0:
                    cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    wrist_x = cpx
                    wrist_y = 100-cpy
                    x2_coordinate = np.sqrt(np.sum(np.square(int(cx) - int(cy))))
                    #print(f"X2 Coordinate: {x2_coordinate}")
                    if initial_check:
                       initial_coordinates_1 = np.array((cx, cy))
                       #initial_check = False
                    #print(f"Wrist Co-ordinate: {x2_coordinate}")

                if id == 8:
                    index_x = cpx
                    index_y = 100-cpy
                    previous_state = current_state
                    cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    x1_coordinate = np.sqrt(np.sum(np.square(int(cx) - int(cy))))
                    #x1_coordinate =
                    #print(f"X1 Coordinate: {x1_coordinate}")
                    if initial_check:
                        initial_coordinates_2 = np.array((cx, cy))
                    #     initial_check = False


                    #print(f"Pointer Co-ordinate: {x1_coordinate}")

                    #cv2.line(image, x2_coordinate, x1_coordinate, (0, 0, 0), 5)

                    # if x1_coordinate
                    #         #print(check)
                    #         print("Swipe Left")
                    # elif x1_coordinate = x1_coordinate - 5.0:
                    #     print("Swipe Right")

                    final_coordinates = (np.linalg.norm(x1_coordinate - x2_coordinate))
                    #print(final_coordinates)
                    #print(results.multi_handedness)

                    #if final_coordinates < 150 and x2_coordinate > 150:
                        #initial_check = True
                    #print("index_tip x:",index_x," y:",index_y,", wrist x:",wrist_x,", y:",wrist_y)
                    if index_x < 30:
                        #if initial_check:
                            #print(" Swipe Right! ")
                            current_state = 'right'
                            initial_check = False
                            wrist_coordinates = np.array((cx, cy))
                            pointer_coordinates = np.array((cx, cy))
                            #if np.array_equal(wrist_coordinates, initial_coordinates_1) and np.array_equal(pointer_coordinates, initial_coordinates_2):
                            #    print("Entered")
                            #    initial_check = True
                    elif index_x > 70:
                        current_state = 'left'
                        #if initial_check:
                        #print(" Swipe Left! ")
                        initial_check = False
                        wrist_coordinates = np.array((cx, cy))
                        pointer_coordinates = np.array((cx, cy))
                    else:
                        current_state = 'middle'


                            # if pointer_coordinates in range(x2_coordinate, float(50)) and wrist_coordinates in range(x1_coordinate, float(50)):
                            #     print("Entered")
                            #     initial_check = True
                    if current_state !=previous_state:
                        print(current_state)
                    # if final_coordinates > 250:
                    #     print(" Swipe Right! ")
                    # elif final_coordinates < 150:
                    #     print(" Swipe Left! ")

                    #elif x1_coordinate > x2_coordinate:
                    #    print("Swipe Right")
                    # pointer.append(id)
                    # pointer.append(cx)
                    # pointer.append(cy)

                    #print(cx, cy)

                #     if x2_coordinate > x1_coordinate:

                #else:
                #    None
                #     thumb.append(id)
                #     thumb.append(cx)
                #     thumb.append(cy)

                #x2_coordinate = x1_coordinate

                #while x1_coordinate >= x2_coordinate:
                #    print("Swipe Left")

                #else:
                #    print('Previous')
            #cv2.imshow(" ", mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS))
            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            #print(f"Detected: {detected}")

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(image, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)
    detected = mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
    #print(f"Detected: {detected}")

    cv2.imshow("Image", image)
    #initial_check = True
    #cv2.imshow("Detected", detected)
    # cv2.imshow("detected", mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS))
    cv2.waitKey(1)
