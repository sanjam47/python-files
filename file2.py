#open() with mode
with open('abc.txt',mode='r') as new_file1:
    new_file1_content=new_file1.read()
    print(new_file1_content)

with open('abc.txt',mode='w') as new_file2:
    new_file2_content=new_file2.write('\n dasdfas')
    #print(new_file2.read())

with open('abc.txt',mode='a') as new_file3:
    new_file3_content=new_file3.write('dk;fadfkjdl;fs')
    print(new_file3_content)
    #print(new_file3.read())

with open('abc.txt',mode='r+') as new_file1:
    new_file1_content=new_file1.read()
    print(new_file1_content)
    new_file1.write('la;dfjl;s')
    print(new_file1.read())




