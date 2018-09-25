import re
import chardet
import sys


# https://www.yellowbridge.com/chinese/charsearch.php?zi=大
# https://www.yellowbridge.com/chinese/charsearch.php?zi=%E5%8d%83

char = ['大','小','一','二','三','十','百','千','多','不']
big5char = ['A46A','A470']

print(sys.stdin.encoding)
for c in char:
    encoded = c.encode('utf-8')
    print(chardet.detect((encoded)))
    print(encoded)

# print(big5char)
