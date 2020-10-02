from PIL import Image, ImageFilter


def main():
    bound = (550, 220, 680, 300)  # (x1,y1,x2,y2) 通过左上角和右下角的坐标来定位
    before = Image.open("ycy.jpg")
    after = before.filter(MyGaussianBlur(radius=60, bounds=bound))
    after.show()  # 显示图片
    after.save("out.jpg")
    print_()

def print_():
    print("Succeed")

class MyGaussianBlur(ImageFilter.Filter):
    name = "GaussianBlur"

    def __init__(self, radius=2, bounds=None):
        self.radius = radius
        self.bounds = bounds

    def filter(self, image):
        if self.bounds:
            clips = image.crop(self.bounds).gaussian_blur(self.radius)
            image.paste(clips, self.bounds)
            return image
        else:
            return image.gaussian_blur(self.radius)


main() # 运行主函数
