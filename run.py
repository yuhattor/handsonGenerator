# -*- coding: utf-8 -*-

# hands on generator
from pathlib import Path

SCREENSHOTS_PATH= "./screenshots/*.png"
TEMPLATE_PATH = "./template.html"
OUTPUTP_PATH= "./output.html"
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
  markDownText = ""
  fullSlide = open(TEMPLATE_PATH).read()
  for i, screenshot in enumerate(pathToList(SCREENSHOTS_PATH)):
    it = INNER_TEMPLATE
    markDownText += it.replace("__ScreenshotPath__", screenshot.as_posix()).replace("__TitleOfSlide__"," %s ." % str(i+1))
  result = fullSlide.replace("__Contents__", markDownText)
  
  with open(OUTPUTP_PATH, 'w') as f:
    f.write(result)
run()
