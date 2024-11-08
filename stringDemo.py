str1 = 'Hello'
str2 = "everyone!"
str3 = '''\nWelcome to: '''
str4 = """\nPython class
Math class
... """
# init ways
print(str1, str2, str3, str4)   
a = "Hello World!"
print(len(a)) # 12
a =" Hello World! "
print(a.strip()) # returns "Hello World!" remove space start and end
a = "hello World!"
print(a.lower()) # returns "hello world!"
print(a.upper()) # returns "HELLO WORLD!"
print(a.capitalize()) # returns "Hello World!"
a = "Hello World!"
print(a.replace("World", "friends")) # Hello friends!
a = "Bao, Khang, Huyen"
print(a.split(",")) # ['Bao', ' Khang', ' Huyen']
str1 = "Python class"
x = "Python" in str1
print(x) # True
str = 'Hello World!'
print(str.startswith('hello')) # False
print(str.endswith('!')) # Truestr = 'Hello World!’
print(str.find('hello')) # -1
print(str.find('Hello')) # 0
print(str.rfind('World')) # 6
print(str.rfind('!')) # 11
str = 'Hello World!'
print(str.count('o')) # 2
print(str.count('l')) # 3
print(str.count('a')) # 0
str ='0912218,Tran Quang A,1991,CNTT'
arrS = str.split(',')
for s in arrS: print(s)
str1 = ','
str2 = str1.join(arrS)
print(str2)
str = 'FIT-UTE'
print(str.isalnum()); # False (vì chứa '-')                
str ='FITUTE'
print(str.isalpha()); # True
str ='0912218'
print(str.isdigit()); # True                    
str = 'FIT-UTE'
print(str.center(20)) # FIT-UTE
print(str.center(20,
'*'))# ******FIT-UTE*******
print(str.rjust(20,
'*')) # *************FIT-UTE
print(str.ljust(20,
'*')) # FIT-UTE************
str1 = 'Khang'; str2 = 'Bao'
print('Hello {0}, my name is {1}'.format(str1, str2)) # Hello Khang, my name is Bao
print ("My name is %s and my weight is %d kg!" % ('Khang', 71) )
str = u'\u265E \u265F'
print(str); # ♞