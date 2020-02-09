from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pandas as pd

x1 = pd.ExcelFile('list2.xlsx')
df = x1.parse('Sheet1')


#by using csv
df = pd.read_csv("list2.csv")

for index, row in df.iterrows():
  print(index, row['Name'], row['email'])
  n=row['Name']
  def make_certificate(n):
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype('LHANDW.ttf', size=64)
    width, height = img.size
    w, h = draw.textsize(n, selectFont)
    draw.text(((width - w) / 2, (height - h) / 2), n, '#7daef7', selectFont)
    img.save('{}.pdf'.format(n))
    img.save('{}.png'.format(n))
  make_certificate(n)
