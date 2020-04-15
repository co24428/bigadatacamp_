from cv2 import cv2

fname = './data/video/fbi.avi'

# cv2.VideoCapture("경로")
cap = cv2.VideoCapture(fname)

while(cap.isOpened()): # 읽을 프레임이 있으면 반복
    ret, frame = cap.read() # 프레임 read
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 프레임 처리
    cv2.imshow('frame',gray) # show

    # q 입력시 멈춤
    # 프레임 읽은 후 55ms를 대기
    # 55 값을 바꿔줌으로 처리 속도를 바꿀 수 있다.
    if cv2.waitKey(55) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()