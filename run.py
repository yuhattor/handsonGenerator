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

def generateSlides():
  path = Path(".")
  full_contents = ""
  title = input("Please Enter Title: ")
  template_slide = open(TEMPLATE_PATH).read()
  screenshots = sorted(list(path.glob(SCREENSHOTS_PATH)))
  for i, screenshot in enumerate(screenshots):
    page = INNER_TEMPLATE
    replace_properties = {
      "__ScreenshotPath__": screenshot.as_posix(),
      "__TitleOfSlide__": " %s ." % str(i+1)
    }
    for key in replace_properties:
      page = page.replace(key, replace_properties[key])
    full_contents += page
  slide = template_slide.replace("__Contents__", full_contents)
  slide = slide.replace("__Title__", title)
  with open(OUTPUTP_PATH, 'w') as f:
    f.write(slide)

generateSlides()
