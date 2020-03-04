import os
import re # 导入正则表达式模块 https://www.runoob.com/python/python-reg-expressions.html

def changeFilenameSubstring():
    """
    批量修改文件名中的指定子串
    如：把"数据结构01-01复杂度分析"改为"算法-01复杂度分析"
    """
    path = input("请输入文件夹完整路径(如/Users/macos/Photo/)：")
    filenames = os.listdir(path)
    print("原来的文件名如下：")
    print(filenames)
    print()

    for filename in filenames:
        # re.sub(pattern, repl, string)
        newFilename = re.sub('数据结构\d{2}', '算法', filename)
        # 切换到path目录，方便直接rename
        os.chdir(path) # https://www.runoob.com/python/os-chdir.html
        os.rename(filename, newFilename) # https://www.runoob.com/python/os-rename.html

    newFilenames = os.listdir(path)
    print("修改后的文件名如下：")
    print(newFilenames)
    print("\n任务完成！")

changeFilenameSubstring()