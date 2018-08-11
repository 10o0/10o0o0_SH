import re
secret_code = 'afsdfsdfgsgfsgsgsgxx1xxfsafxxlovexxfsagfasgxxyouxxfjsklafjls'
# a = 'xy1233'
# b = re.findall('x...',a)
# print b
#
# a = 'xy12x33'
# b = re.findall('x*',a)
# print b
#
#
# a = 'xy12x33'
# b = re.findall('x?',a)
# print b

b = re.findall('xx.*xx',secret_code)
print b
b = re.findall('xx.*?xx',secret_code)
print b
b = re.findall('xx(.*?)xx',secret_code)
print b