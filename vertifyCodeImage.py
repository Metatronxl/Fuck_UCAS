#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/8/27
# @Author : lei.X

from PIL import Image
import requests
from io import BytesIO
from pytesseract import image_to_string
import os
import random

def getImage():
    response = requests.get("http://sep.ucas.ac.cn/changePic")
    img = Image.open(BytesIO(response.content))
    img.show()

    #降噪处理
    threshold = 140
    table = []
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    imgry = img.convert('L')
    out = imgry.point(table,'1')

    text = image_to_string(out)
    print("test:",text)

def makdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path+": create success")
        return
    print(path + ": exsits")
    return

def download_verticy_img(path):
    response = requests.get("http://sep.ucas.ac.cn/changePic")
    fileName = str(random.randint(0,100000))+".jpg"

    with open(path+"/"+fileName,'wb') as f:
        f.write(response.content)



if __name__ == '__main__':
    # getImage()
    path = "/Users/xulei2/Desktop/code"
    makdir(path)
    for i in range(100):
        download_verticy_img(path)