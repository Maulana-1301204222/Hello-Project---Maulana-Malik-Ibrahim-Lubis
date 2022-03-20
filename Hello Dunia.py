import datetime
jam = int(datetime.datetime.now().hour)
menit = int(datetime.datetime.now().minute)
if jam >= 5 and jam < 10:
  print("Selamat pagi world \nSemangat untuk mengejar masa depan")
elif jam >= 10 and jam < 16:
  print("Selamat siang dunia \nSemangat panas panasannya")
elif jam >= 16 and jam < 18:
  print("Selamat sore dunia \nSudah mau waktunya istirahat")
elif jam >= 18 and jam < 21:
  print("Selamat malam dunia \nSudah mau waktunya tidur")
else:
  print("Tidurlah kawan!! \nkarena besok kita memerlukan tenaga untuk menjalani kehidupan ini")
