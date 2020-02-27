import os
import random




train_img_dir = "trainImage/"
train_img_list = [os.path.join("data/custom/images/", i) for i in sorted(os.listdir(train_img_dir))]
train_img_list = list(map(lambda x:x+"\n", train_img_list))

val_img_dir = "valImage/"
val_img_list = [os.path.join("data/custom/images/", i) for i in sorted(os.listdir(val_img_dir))]
val_img_list = list(map(lambda x:x+"\n", val_img_list))

with open("train.txt", "w") as f:
    f.writelines(train_img_list)
     
with open("val.txt", "w") as f:
    f.writelines(val_img_list)        