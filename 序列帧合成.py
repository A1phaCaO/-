import os
import cv2

# 定义行数和列数
height = int(input('请输入高度'))
width = int(input('请输入宽度'))

# 获取文件夹地址
path = input('请输入文件夹地址')
# 获取文件夹中的文件列表
path_list = os.listdir(path)
# 判断文件数量是否正确
if len(path_list) != width*height:
    print('图片数量错误')
    exit()
# 对文件列表进行排序
path_list.sort()

# 读取文件列表中的图片
img_list = [cv2.imread(path + '\\' + i, flags=cv2.IMREAD_UNCHANGED) for i in path_list]
# 初始化图片网格
img_gird = [[0]* width for _ in range(height)]

# 将图片列表中的图片放入图片网格中
for i in range(height):
    for j in range(width):
        img_gird[i][j] = img_list[i*width+j]


# 将图片网格中的图片进行拼接
h_concat = [cv2.hconcat(i) for i in img_gird]
v_concat = cv2.vconcat(h_concat)


# 保存拼接后的图片
cv2.imwrite('out.png', v_concat)