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
# char = ['大','小']
# s = char[1].encode('hkscs').hex()
# # # print(s)
# # #
# print(bytes(s))
# print(s.decode('big5'))
# # #
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
#
# l = [[1, 2], [2, 3], [4, 5]]
#
# out = open('out.csv', 'w')
# for row in l:
#     for column in row:
#         out.write('%d,' % column)
#     out.write('\n')
# out.close()
#
# for i in range(100):
#     s = '{:03}'.format(i)
#     print(s)

s = '日军軍者意无無力它与與长長把机機十民第公此已工使情明性知全三又关關点點正业業外将將两兩高间間由问問很最重并並;併物手应應战戰向嚮头頭文体體政美相见見被利什二等产産或新己制製身果加西斯月话話合回特代内信表錶化老给給世位次度门門任常先海通教儿兒原东東声聲提立及比员員的一是不了在人有我他这个们中来上大为和国地到以说时要就出会可也你对生能而子那得于着下自之年过发后作里用道行所然家种事成方多经么去法学如都同现当没动面起看定天分还进好小部其些主样理心她本前开但因只从想实'

char_line1 = ['大','小','一','二','三','十','百','千','多','不','人','夫','子','男','女','王','主','我','你','他','口','說','目','見','耳','聞','手','工','腳','行','來','入','出','上','下','中','在','左','右','有','吃','飯','菜','豆','肉','牛','豬','雞','魚','茶','國','家','校','文','學','狗','貓','馬','鳥','虫','日','月','天','地','海','木','火','土','金','水','氣','幹','雨','山','川','米','田','花','石','玉','村','店','車','衣','白','黑','紅','藍','藍','黃','是','心','好','愛','喜','幸','生','死','力','疾']

for i in s:
    if i not in char_line1:
        try:
            s=i.encode('big5').hex()
            print(s,end=' ')
        except:
            print(i)
#
# for i in char_line1:
#     print(i,end='')