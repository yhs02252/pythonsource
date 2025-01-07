from openpyxl import Workbook

# 엑셀 저장 모듈


def write_excel_template(filename, sheetname, listdata):
    wb = Workbook()
    ws = wb.active

    # 제목별 너비 조절
    ws.column_dimensions["A"].width = 100
    ws.column_dimensions["B"].width = 20

    # 시트명 변경
    ws.title = sheetname

    # 데이터 추가
    for item in listdata:
        ws.append(item)

    wb.save("./" + filename)
    wb.close()


# test
# if __name__ == "__main__":
#     listdata = [
#         [1, 10, 8, 5, 14, 26, 12],
#         [2, 7, 3, 7, 15, 24, 18],
#         [3, 9, 5, 8, 8, 12, 4],
#         [4, 7, 8, 7, 17, 21, 18],
#         [5, 7, 8, 7, 16, 25, 15],
#         [6, 3, 5, 8, 8, 17, 0],
#         [7, 4, 9, 10, 16, 27, 18],
#         [8, 6, 6, 6, 15, 19, 17],
#         [9, 10, 10, 9, 19, 30, 19],
#         [10, 9, 8, 8, 20, 25, 20],
#     ]
# write_excel_template("temp1.xlsx", "test", listdata)
