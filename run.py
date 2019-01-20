# -*- coding: utf-8 -*-
# hands on generator
from pathlib import Path

SCREENSHOTS_PATH= "./screenshots/*.png"
TEMPLATE_PATH = "./template.html"
OUTPUTP_PATH= "./output.html"
TITLE = "ハンズオン"
INNER_TEMPLATE = '''
#__TitleOfSlide__ 
<img src='__ScreenshotPath__' /> 
---
'''

# get file list string and create array
def pathToList(path):
  p = Path(".")
  return list(p.glob(path))

def run():
  fullContents = ""
  templateSlide = open(TEMPLATE_PATH).read()
  screenshots = sorted(pathToList(SCREENSHOTS_PATH))
  for i, screenshot in enumerate(screenshots):
    page = INNER_TEMPLATE
    replaceList = {
      "__ScreenshotPath__": screenshot.as_posix(),
      "__TitleOfSlide__": " %s ." % str(i+1)
    }
    for key in replaceList:
      page = page.replace(key, replaceList[key])
    fullContents += page
  slide = templateSlide.replace("__Contents__", fullContents)
  slide = slide.replace("__Title__", TITLE)
  with open(OUTPUTP_PATH, 'w') as f:
    f.write(slide)

run()
