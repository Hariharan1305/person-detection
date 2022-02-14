import cv2

bus_classifier = cv2.CascadeClassifier('Bus_front.xml')


camera = cv2.VideoCapture('bus_01.mp4')

count = 0

while (True):

    ret, img = camera.read()

    height, width = img.shape[0:2]

    img[0:70, 0:width] = [0, 0, 255]
    cv2.putText(img, 'Total bus counts :', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

    cv2.line(img, (0, height - 500), (width, height - 500), (0, 255, 255), 2)

    blur = cv2.blur(img, (3, 3))
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    bus = bus_classifier.detectMultiScale(gray)

    for (x, y, w, h) in bus:

        bikeCy = int(y + h/2)
        linCy = height - 500

        if (bikeCy < linCy + 6 and bikeCy > linCy - 6):
            count = count + 1
            cv2.line(img, (0, height - 500), (width, height - 500), (0, 0, 255), 5)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, 'bus', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(img, str(count), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

    cv2.imshow('LIVE', img)
    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()
camera.release()