import cv2

# 파일 경로
fname = './data/image/dog1.jpg'

# cv2.imread => 이미지 읽어오기
# cv2.imread("경로", option)
# option : 
#   cv2.IMREAD_COLOR(원본, 3 channel), default value
#   cv2.IMREAD_GRAYSCALE(흑백, 1 channel)
#   cv2.IMREAD_UNCHANGED(원본, alpha channel까지)
#   (1, 0, -1) 순서대로 넘버링으로도 가능
original = cv2.imread(fname, cv2.IMREAD_COLOR)
gray = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
unchange = cv2.imread(fname, cv2.IMREAD_UNCHANGED)

# cv2.imshow => 이미지 띄우기
# cv2.imshow("Name", image)
# 상단 네이밍이 "Name"으로 된다.
cv2.imshow('Original', original)
cv2.imshow('Gray', gray)
cv2.imshow('Unchange', unchange)

# cv2.imwrite("경로/파일이름", image)
# 해당 경로에 파일이름으로 image를 저장
cv2.imwrite("./data/output/gray_dog.png", gray)

# cv2.waitKey(n)
# n=0; 입력이 있을 때까지 무기한 대기
# n=n; n ms만큼 대기
cv2.waitKey(0)
cv2.destroyAllWindows()