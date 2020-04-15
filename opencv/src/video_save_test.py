import cv2

fname = './data/video/cat.avi'

cap = cv2.VideoCapture(fname)

#재생할 파일의 넓이 얻기
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#재생할 파일의 높이 얻기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#재생할 파일의 프레임 레이트 얻기
fps = cap.get(cv2.CAP_PROP_FPS)

print('width {0}, height {1}, fps {2}'.format(width, height, fps))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
# 코덱 종류 : DIVX, XVID, MJPG, X264, WMV1, WMV2
# Windows에서는 DIVX 사용

out = cv2.VideoWriter('output.avi', fourcc, 30, (int(width),int(height)))
# out = cv2.VideoWriter('output.avi', fourcc, fps, (int(width),int(height)))
# 비디오 저장을 위한 객체를 생성한다. 
# cv2.VideoWriter("path/filename", 코덱, fps, (width, height))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret: # 읽혔다면!
        # 이미지 반전,  0:상하, 1 : 좌우
        frame = cv2.flip(frame, 0)
        # frame = cv2.flip(frame, 1)

        out.write(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
