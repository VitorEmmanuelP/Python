import openpyxl.drawing.image
from openpyxl import  load_workbook

book = load_workbook(f'MODELO.xlsx')
sheet = book.active

img = openpyxl.drawing.image.Image('img.png')

img.anchor = 'B1'

sheet.add_image(img)

book.save('AD.xlsx')