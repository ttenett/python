import base64
import codecs

# # article 파일 열기
# file = open('C:\\Users\\yeonjeong\\TIL\\01_python\\project\\news\\article', 'r')
# temp = file.read()
# file.close()
# print(temp)

# # html 파일열기
# file2 = open('news\summary.html', 'r', delcoding='CP949')
# file.close
# print(file2)

# 파일에서 텍스트 읽기
with codecs.open('C:\\Users\\yeonjeong\\TIL\\01_python\\project\\news\\article', 'r', encoding='utf-8') as f:
    content = f.read()


