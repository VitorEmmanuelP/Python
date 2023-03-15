import re
gmail = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha Ha Ha
MetaCharacters ( Need to be escaped )
  ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
900-555-4321
800-555-4321

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''

# creates the pattern to be seached
#seach = r'abc'
#seach = r'coreyms\.com'  #  if want to search must have the '\'

a = '''
Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com
'''

nome = r'[A-Za-z]+\s[A-Za-z]{3,}'
numero = r'\d{3}(-|.)\d{3}(-|.)\d{4}'
endereco = r'[0-9]{3}\s[0-9{1}a-zA-Z]+\sSt\.,\s[a-zA-Z]+\s[A-Z]{2}\s[0-9]+'
gmail_regex = r'[A-Za-z]+@[A-Za-z]+\.com'

pattern = re.compile(endereco)
# search matches
# matches = pattern.finditer(gmail)

# for match in matches:
#     print(match)

with open('data.txt','r') as file:
    content = file.read()
    matches = pattern.finditer(content)
    for match in matches:
        print(match)

