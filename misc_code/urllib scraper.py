import requests

# params = {'char':'3','word':'我','font':'小篆'}
#
# r = requests.post('http://char.iis.sinica.edu.tw/Search/YiChar_SQL.aspx?char=592&word=我&font=甲骨文')
#
#
# filename = 'requests.html'
# with open(filename, 'wb') as f:
#     f.write(r.content)


# from urllib.request import urlopen
# from urllib.parse import urlencode
# form_data = ({'char':'A7DA','type':'0'})
# with urlopen("http://char.iis.sinica.edu.tw/Search/char_SQL.aspx", form_data) as u:
# 	with open("test2.html", "w") as fi:
# 		fi.write(u.read().decode("utf-8"))

params = {'word':'大'}

r = requests.post('https://www.yellowbridge.com/chinese/sentsearch.php',params)


filename = 'requests.html'
with open(filename, 'wb') as f:
    f.write(r.content)


# https://www.yellowbridge.com/chinese/sentsearch.php?word=%E5%8D%83