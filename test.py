import re
tpl = r"^[0-9 .+*\/-]*$"
d = '1'
if re.findall(tpl, d):
    print(1)