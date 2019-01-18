# -*- coding: utf-8 -*-
# hands on generator
from pathlib import Path
from pprint import pprint 

# 漢字とカタカナによって構成される文字列を抽出
# get file list string and create array
def pathToList(path):
  p = Path(".")
  return list(p.glob(path))

# pathObjectToJson
def jsonFileToDict(file):
  f = open(file)
  return f


def dumpText(text, path):
  with open(path, 'w') as f:
    f.write(text)

