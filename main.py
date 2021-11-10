# This is a sample Python script.
import tkinter
from tkinter import HORIZONTAL

import cv2

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    cap = cv2.VideoCapture(0)

    v1 = 150
    v2 = 255

    master = tkinter.Tk()
    w1 = tkinter.Scale(master, from_=0, to=255)
    w1.set(v1)
    w1.pack()
    w2 = tkinter.Scale(master, from_=0, to=2255, orient=HORIZONTAL)
    w2.set(v2)
    w2.pack()
    # tkinter.mainloop()

    drawing = False  # true if mouse is pressed
    mode = True
    ix, iy = -1, -1


    def nothing(x):
        pass

    cv2.namedWindow('Controls', cv2.WINDOW_NORMAL)  # --- window to have all the controls

    cv2.createTrackbar("V1", "Controls", 0, 255, nothing)
    cv2.createTrackbar("V2", "Controls", 0, 255, nothing)

    cv2.createTrackbar("Threshold", "Controls", 0, 30, nothing)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        hul = cv2.getTrackbarPos("V1", 'Controls')
        huh = cv2.getTrackbarPos("V2", 'Controls')
        # Our operations on the frame come here
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # apply binary thresholding
        ret, thresh = cv2.threshold(img_gray, hul, huh, cv2.THRESH_BINARY)

        # Display the resulting frame
        cv2.imshow('frame', thresh)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
