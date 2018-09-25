# import re
# # # import chardet
# # import sys
# #
# #
# # # https://www.yellowbridge.com/chinese/charsearch.php?zi=大
# # # https://www.yellowbridge.com/chinese/charsearch.php?zi=%E5%8d%83
# #
# # # char = ['大','小','一','二','三','十','百','千','多','不']
# # # big5char = ['A46A','A470']
# # # id = ['43','49']
# # #
# # #
# # #
# # # print(sys.stdin.encoding)
# # # for c in char:
# # #     encoded = c.encode('utf-8')
# # #     print(chardet.detect((encoded)))
# # #     print(encoded)
# #
# # # print(big5char)
# # import codecs
# #
# #
# # char = ['大','小']
# # s = char[1].encode('hkscs').hex()
# # print(s)
# #
# # print(bytes(s))
# # print(s.decode('big5hkscs'))
# #
# # print(bytearray.fromhex(b'a4j'))
# #
# # id = ['43','49']
# # era = ['甲骨文','金文','楚系文字']
# # l=[]
# # #
# # # for i in range(len(char)):
# # #     for e in era:
# # #         l.append("http://char.iis.sinica.edu.tw/Search/YiChar_SQL.aspx?char={}&word={}&font={}".format(id[i],char[i],e))
# # #
# # # for i in l:
# # #     print(i)

# str1 = 'hello'
# print(str1[2:])

l = [[1, 2], [2, 3], [4, 5]]

out = open('out.csv', 'w')
for row in l:
    for column in row:
        out.write('%d,' % column)
    out.write('\n')
out.close()