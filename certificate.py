#using pil libraries and pandas
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pandas as pd

#by using excel 
x1 = pd.ExcelFile('list2.xlsx')
df = x1.parse('Sheet1')


#by using csv
df = pd.read_csv("list2.csv")

for index, row in df.iterrows():  #for loop for making 'n' number of names
  print(index, row['Name'], row['email'])
  n=row['Name']
  def make_certificate(n):  #function for making n number of certifcates with name enabled on it
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype('LHANDW.ttf', size=64)
    width, height = img.size
    w, h = draw.textsize(n, selectFont)
    draw.text(((width - w) / 2, (height - h) / 2), n, '#7daef7', selectFont)
    img.save('{}.pdf'.format(n))
    img.save('{}.png'.format(n))
  make_certificate(n) #function call
