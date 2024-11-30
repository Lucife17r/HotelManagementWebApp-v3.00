'''fruits=['apple','pear','banana']

try:
    selection=fruits[int(input('select a fruit number (0-2):'))]
except ValueError:
    print('that is not a number')

except IndexError:
    print("That fruit number does not exist")

print("hello")'''

import re
'''k="The rain in gaurav tomar spain"

x=re.search("^The. *spain",k)
if x:
    print("yes")
else:
    print("no match")'''

'''import re
t='^gau....s$'
test='gauhhhrs'
k=re.match(t,test)
if k:
    print("match")

else:
    print("no match")'''

'''import re
line="gauravtomar@kdkd.com"
email= re.findall(r'^[\w\.-]+@[\w-]+\.[\w-]{2,4}$',line)
if email:
    print('yes')
else:
    print('no match')'''

import re
phonenumber= "706591-5607"

regex="\(\w(3)\)\w(3)-\(4)"

#regex="\w(3)\w(3)\w(4)"

#regex="\\w(3)-\\w(3)-\\w(4)"

if re.search(regex,phonenumber ):

    print("Valid phone number")

else:
    print("invalid phone number")


























