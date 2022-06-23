# 이미지의 사칙 연산

import cv2
import numpy as np

# 연산에 사용할 배열 생성
a = np.uint8([[200, 50]])
b = np.uint8([[100, 100]])

# unit8 타입의 값의 범위는 0~ 255 이므로 255를 넘는 값은 다시 0부터 카운팅

# NumPy 배열 직접 연산
add1 = a + b
sub1 = a - b
mult1 = a * 2
div1 = a / 3

# OpenCV API를 이용한 연산
add2 = cv2.add(a, b)
sub2 = cv2.subtract(a, b)
mult2 = cv2.multiply(a, 2)
div2 = cv2.divide(a, 3)

# 각 연산 결과 출력
print(add1, add2)
print(sub1, sub2)
print(mult1, mult2)
print(div1, div2)
