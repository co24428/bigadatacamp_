# opencv summary

## directory
~~~
opencv
    L src
        Limg_test.py
    L data
        L video : test video
        L image : test image
        L mnist_image 
        L coffe_bean : my project image
        L output : output from coffee_bean
~~~

<hr>
## cv2 공통

### 입력 대기(출력 프레임 조정)
~~~
cv2.waitKey(n)
~~~
- n=0; 입력이 있을 때까지 무기한 대기
- n=n; n ms만큼 대기

## 이미지 관련 함수

### 이미지 객체 생성
~~~
cv2.imread("경로", option)
~~~
- 이미지 읽어오기(read)
- option : 
    - cv2.IMREAD_COLOR(원본, 3 channel), default value
    - cv2.IMREAD_GRAYSCALE(흑백, 1 channel)
    - cv2.IMREAD_UNCHANGED(원본, alpha channel까지)
    - (1, 0, -1) 순서대로 넘버링으로도 가능

- ex)
    - original = cv2.imread(fname, cv2.IMREAD_COLOR)

### 이미지 플로팅(show)
~~~
cv2.imshow("Name", image)
~~~
- 이미지 플로팅(show)
- 상단바의 이름이 "Name"으로 설정된다.
- ex)
    - cv2.imshow("origin_image", original)

### 이미지 저장
~~~
cv2.imwrite("경로/파일이름", image)
~~~
- 해당 경로에 파일이름으로 image를 저장

## 이미지(프레임) 처리 함수

### 이미지 resize(확대, 축소)
~~~
cv2.resize( target_image, dsize=(n,m), interpolation(보간법) )
cv2.resize( target_image, dsize=(0, 0), fx=0.3, fy=0.7, interpolation(보간법) )
~~~
- dsize (=res_image_size) : Tuple type (n,m)
    - (0,0) : fx, fy를 통해 비율로 조절
    - (n,m) : 원하는 픽셀크기로 조정
- interpolation(보간법) : 조정(확대, 축소)시 픽셀 처리 방법
~~~
cv2.INTER_NEAREST      : 이웃 보간법
cv2.INTER_LINEAR       : 쌍 선형 보간법, 주로 사용
cv2.INTER_LINEAR_EXACT : 비트 쌍 선형 보간법
cv2.INTER_CUBIC        : 바이큐빅 보간법
cv2.INTER_AREA         : 영역 보간법
cv2.INTER_LANCZOS4     : Lanczos 보간법
~~~

    - 가장 기본적인 것은 쌍선형
    - 확대시, 바이큐빅 or 쌍선형
    - 축소시, 영역 보간법
    - 영역 보간법으로 확대시 이웃 보간법과 비슷한 결과
- ex)
    - dst = cv2.resize(src, dsize=(64, 64), interpolation=cv2.INTER_AREA)
    - dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

###  이미지 반전
~~~
cv2.flip(image, n)
~~~
- n=0:상하, n=1: 좌우
- ex)
    - frame = cv2.flip(frame, 0)

## 동영상 관련 함수

### 동영상 객체 생성
~~~
cv2.VideoCapture("경로")
~~~
- ex)
    - cap = cv2.VideoCapture(fname)

### 기본적인 동영상 프로세스
- 동영상은 사진(frame)의 연속형
- 한 frame씩 읽으면서 처리 > 반복해서 띄워주는 것!!
~~~
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
~~~
- cv2.imshow() 이전에 프레임에 대한 처리를 코딩하면 된다.

### 동영상 저장
~~~
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # 동영상 width
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 동영상 height
fps = cap.get(cv2.CAP_PROP_FPS) # 동영상 fps
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 코덱 설정
out = cv2.VideoWriter('output.avi', fourcc, fps, (int(width),int(height))) # 객체 생성

while(cap.isOpened()):
    ...프레임 읽기/처리 코드...
    out.write(frame) # frame 객체에 저장
    ...
out.release() # 객체 해제
~~~
- 코덱 설정
~~~
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  
fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
~~~
    - 코덱 종류 : DIVX, XVID, MJPG, X264, WMV1, WMV2
    - Windows에서 .avi로 저장할 때, DIVX 사용
- 저장!!
~~~
cv2.VideoWriter("path/filename", 코덱, fps, (width, height))
~~~
- 동영상 저장을 할 때 width, height가 원본과 같아야 한다.
- fps는 조정가능
    - 동영상의 속도를 임의적으로 바꿀 수 있다.


## 기능에 따른 코드

### 배경 제거 & 움직임 인식
- 주요 코드

~~~
fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=500)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    
    fgmask = fgbg.apply(frame)
    cv2.imshow('fgmask',fgmask)
~~~

- createBackgroundSubtractorMOG2 : 배경을 지우고 움직이는 물체 검출하는 알고리즘
    - 알고리즘 별로 MOG2 부분이 수정 된다.
- varThreshold=n : 
    - 높아질수록 배경으로 처리되는 임계점이 늘어남(움직이는 것만 가져오기 좋아진다.)
    
~~~
in python 2
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
in python 3
fgbg =cv2.createBackgroundSubtractorMOG2()
~~~
- 참고 글 
    - https://webnautes.tistory.com/1248








