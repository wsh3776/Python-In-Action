import os

def renameFiles():
    """
    批量重命名文件:
    忽略文件夹，且不会出现文件覆盖的问题
    """
    path = input("请输入文件夹完整路径(如/Users/macos/Photo/)：")
    name = input("请输入文件开头名(如pic)：")
    startNumber = input("请输入迭代开始数(如0)：")
    suffix = input("请输入后缀名(如txt、jpg)：")
    filenames = os.listdir(path)

    changeList = []   # 记录哪些文件被修改了
    newNameList = []  # 预期生成的新文件名列表
    count = 0
    length = 0
    for filename in filenames:
        if os.path.isdir(os.path.join(path, filename)) or filename == '.DS_Store': # join合并路径名，会帮你自动考虑“/”
            continue
        length += 1

    for i in range(length):
        tmp = name + str(i + int(startNumber)) + "." + suffix
        newNameList.append(tmp)

    print("正在批量处理\n...")
    count, num = 0, 0

    # 核心代码
    for filename in filenames:
        # 如果是子文件夹，则不执行
        if os.path.isdir(os.path.join(path, filename)) or filename == '.DS_Store':
            continue
        oldName = os.path.join(path, filename)

        # 如果filename已经在新文件名列表中，则不需要重命名
        if filename in newNameList:
            continue

        # 找到合适的newName，防止覆盖原有的同名文件
        while True:
            tmp = name + str(count + int(startNumber)) + "." + suffix
            newName = os.path.join(path, tmp)
            if tmp in filenames:
                count += 1
            else:
                break

        changeList.append("文件" + filename + "被修改为" + tmp)
        os.rename(oldName, newName)
        count += 1
        num += 1

    print("任务完成，共修改了" + str(num) + "个文件\n")
    cmd = input("您是否需要查看修改的文件名(Y/N)：")
    if cmd == "Y":
        if (len(changeList) > 0):
            for i in range(len(changeList)):
                print(changeList[i])
        else:
            print("本次任务没有修改任何文件")

renameFiles()
