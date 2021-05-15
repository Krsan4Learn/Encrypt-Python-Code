# Code With Python3 For Encrypt Python Code
# By Al Krsan
# Blog :  https://thedigitalagee.blogspot.com
# Youtube : https://www.youtube.com/c/krsan4learn

import marshal

file = input("Type Name File With Extension --> : ")
Open_Raed = open(file).read()
Compel = compile(Open_Raed, '', 'exec')
Dumps = marshal.dumps(Compel)
Start = open('UnCode-' + file, 'w')
Start.write('import marshal\n')
Start.write('exec(marshal.loads(' + repr(Dumps) + '))')
Start.close()
print('[+] Done')
