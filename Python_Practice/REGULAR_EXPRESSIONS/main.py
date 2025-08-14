import re

pattern = R"[A-Z] + "

text = '''
    '''
# # searches only for the first occurrence
# match = re.search(pattern,text)
# print(match)

matches = re.finditer(pattern,text)
for match in matches:
    print(match)