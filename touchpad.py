import sh
str=sh.xinput()

str=str.split('\n')

id='-1'
for line in str :
    if(line.find('Touchpad')+1):
        id=line.split('\t')[1].split('=')[1]
        break
        
if(id=='-1'):
    print('Not Found Touchpad!')
    exit()

str=sh.xinput('list-props',id)
str=str.split('\n')
str=str[1].split(':\t')

state=int(str[1])

if(state):
    sh.xinput('--disable',id)
else:
    sh.xinput('--enable',id)


