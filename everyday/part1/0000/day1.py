# 将图片右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
from __future__ import print_function
from PIL import Image, ImageFont, ImageDraw
image = Image.open('0001.png')   #加载图片
w, h = image.size             #获取图片像素
font = ImageFont.truetype('arial.ttf', 100)    #设置字体及大小
draw = ImageDraw.Draw(image)                   #定义画笔工具
draw.text((4*w/5, h/5), '5', fill=(255, 10, 10), font=font)    #在图片上进行绘画
image.save('0001.0001.png', 'png')                                   #保存

# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import random
# # 随机字母:
# def rndChar():
#     return chr(random.randint(65, 90))
# # 随机颜色1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# # 随机颜色2:
# def rndColor2():
#     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建Font对象:
# font = ImageFont.truetype('Arial.ttf', 36)
# # 创建Draw对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg')
# from __future__ import print_function
from PIL import Image
# im=Image.open('0002.png')
#print(im.format) #打印文件格式
#print(im.size)   #打印文件像素
#im.show()        #将加载的文件显示出来
#print(im.mode)   #颜色格式rgb
# print(im.format,im.size,im.mode)
# ------------------------------------------
#转换文件格式到jpeg

# import os,sys
# from PIL import Image

# for infile in sys.argv[0001:]:
#     f,e=os.path.splitext(infile)
#     outfile=f+'.jpg'
#     if infile != outfile:
#         try:
#             Image.open(infile).save(outfile)
#         except IOError:
#             print('cannot convert',infile)
#使用方法
#python day1.py 0001.png 0002.png
#在命令行中输入python 脚本名字 需要转换的文件名字和后缀，
#备注：需要放在同一目录下
# ------------------------------------------
#创建jpeg缩略图,提前引入之前的那个
# import os,sys
# from PIL import Image
# size=(128,128)
# for infile in sys.argv[0001:]:
#     outfile=os.path.splitext(infile)[0]+'.thumbnail'
#     if infile != outfile:
#         try:
#             im=Image.open(infile)
#             im.thumbnail(size)
#             im.save(outfile,'JPEG')
#         except IOError:
#             print("cannot create thumbnial for",infile)
#使用方法和上面的一样
# ------------------------------------------
#验证图像文件
# from PIL import  Image
# import sys
# for infile in sys.argv[0001:]:
#     try:
#         with Image.open(infile) as im:
#             print(infile,im.format,'%d*%d'%im.size,im.mode)
#             #     文件名   文件格式   像素大小       格式
#     except IOError:
#         pass
#使用方法同上
# ------------------------------------------
















