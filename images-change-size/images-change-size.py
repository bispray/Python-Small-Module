import os
import time
from PIL import Image

path = "C:/Users/DELL/Desktop/jk/ggjtp" # 原图所在位置
save_path = "C:/Users/DELL/Desktop/jk/ssgrademan" # 处理之后图片位置

files = os.listdir(path)  # 返回path目录下的所有文件名
sum = 0 # 统计处理完成的数量
# 遍历每一张图片并修改其尺寸
for i in files:
  document = os.path.join(path, i)  # 返回path和i拼接之后的路径，即第i张图片
  img = Image.open(document)  # 读取第i张图片
  img_resize = img.resize((350, 550))  # 修改尺寸(宽，高)
  fileName = str(i)
  img_resize.save(save_path + os.sep + fileName)  # 保存路径，其中os.sep为系统分隔符
  sum += 1
  print("当前正在对" + "\033[31m" + fileName + "\033[0m" + "进行处理,已处理" + "\033[31m" + str(sum) + "\033[0m" + "个图片")