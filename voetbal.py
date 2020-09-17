# from bs4 import BeautifulSoup
# import requests

# page = requests.get("https://www.knvb.nl/competities/eredivisie/stand")
# soup = BeautifulSoup(page.content, 'html.parser')

# stand = soup.find_all(class_="value team")

# ranglijst = []
# for a in stand:
#     club = a.get_text().strip()
#     if (club != "Team"):
#         ranglijst.append(club)
# print(ranglijst)




# import xlrd
# fname = 'Ere2021.xlsx'

# # Open the workbook
# xl_workbook = xlrd.open_workbook(fname)

# # List sheet names, and pull a sheet by name
# #
# sheet_names = xl_workbook.sheet_names()
# #print('Sheet Names', sheet_names)

# xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

# # Or grab the first sheet by index 
# #  (sheets are zero-indexed)
# #
# xl_sheet = xl_workbook.sheet_by_index(0)
# #print ('Sheet name: %s' % xl_sheet.name)

# def haalOp(col_idx):
#     row_vals = []
#     for row_idx in range(1, xl_sheet.nrows):
#         cell_obj = xl_sheet.cell(row_idx, col_idx)
#         #cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
#         #print ('(row %s) %s (type:%s)' % (row_idx, cell_obj.value, cell_type_str))
#         row_vals.append(cell_obj.value)
#     return row_vals

# class Score:
#     def __init__ (self, col_idx):
#         self.name = cell_obj = xl_sheet.cell(0, col_idx)
#         # self.exp = haalOp(col_idx)
#         self.dist, self.vol = verschil(ranglijst, haalOp(col_idx))

#     def getScore(self):
#         score = f"{self.name} {self.dist} {self.vol}"
#         return score.title()

# def verschil(arr, ar2):
#     teller = 0
#     voltreffer = 0
#     for i in range (0, len(arr)):
#         subteller = 0
#         for j in range (0, len(ar2)):
#             if arr[i] == ar2[j]:
#                 subteller += abs(i - j)
#                 #print(f"{arr[i]} {abs(i-j)}")
#                 if (i==j):
#                     voltreffer += 1
#         teller += subteller

#     return (teller, voltreffer)

#for i in range (0,5):
 #   print(Score(i).getScore())

print("OK")

# def test_add():
#     assert (1 == 1), "Add doesn't work"