# 人脸检测，识别静态图片
# 导入opencv-python库（由于历史原因，只能叫cv2）
import cv2

picName = input("请输入你要识别人类的图片名称(如:pic1.jpg): ")
img = cv2.imread(picName, 1)  # 1表示以彩色的方式读入图片

# 导入人脸级联分类器引擎，'.xml'文件包含已经训练出来的人脸特征
face_engine = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 用分类器引擎识别人脸，返回的faces为人脸坐标列表，1.2表示放大比例，7表示重复识别次数
faces = face_engine.detectMultiScale(img, scaleFactor=1.2, minNeighbors=7)
# print(faces)
# [[ 952  302  149  149]
#  [1299  477  121  121]
#  [1468  568  114  114]]

for (x, y, w, h) in faces:
    # 画出人脸框，蓝色(255,0,0)，画笔宽度为2
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 展示效果图
print("正在展示识别后的效果图(在窗口内按q退出)")
while True:
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print ("I'm done")
        break;

cv2.destroyAllWindows()
cv2.imwrite('output.jpg', img) # 保存识别的图片

