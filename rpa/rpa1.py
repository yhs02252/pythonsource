# RPA(Robotic Process Automation) : 자동화 프로그램
# ex) 엑셀자동화 프로그램
# 엑셀 라이브러리 : pip install openpyxl
# 이미지 삽입 : pip install pillow

# 엑셀 파일 생성 가능
from openpyxl import Workbook

# wb 객체 생성
wb = Workbook()

wb.save("./rpa/sample1.xlsx")
wb.close()
