import os


# 创建一些文件夹来保存结果
init_dir = ["trainImage", "valImage", "trainImageXML", "valImageXML", "images", "labels"]

"""
"trainImage"：用来保存训练集的图片
"valImage"：用来保存验证集的图片
"trainImageXML"：用来保存训练集的 xml 文件
"valImageXML"：用来保存验证集的 xml 文件

"images"：训练集+验证集的图片
"labels"：训练集+验证集的 txt 文件
"""

for i in  init_dir:
	if not os.path.exists(i):
		os.mkdir(i)
		print(f"{i} create sucessful!")
	else:
		print(f"{i} is exists")

