import pytesseract
from PIL import Image

img = Image.open('englang.png')


file_name = img.filename
file_name = file_name.split('.')[0]

# custom_config = r'--oem 3 --psm 13'
# custom_config = r'--oem 3 --psm 3'

# https://github.com/tesseract-ocr/tessdata/blob/main/rus.traineddata  - с этого репозитория скачал дополнительный русский язык 
# и получилось перевести текст на русском языке 
# sudo mv -v rus.traineddata /usr/share/tesseract-ocr/4.00/tessdata/ - перевел скачанный словарь при помощи этой команды
# нужную папку на Ubuntu 22.04

text = pytesseract.image_to_string(img, lang = 'eng')

# Так же автоматически записываем (+создаем файл) в новый файл уже расшифрованный текст 
with open(f'Result {file_name}.txt', 'w') as text_file:
    text_file.write(text)