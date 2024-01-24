#open() is use to open the file in present directory or other directory.
myfile=open('abc.txt')
myfile1=open('/home/sanjam/Desktop/Assignment 1.sql')
#If the file is not present or you have not given right directory of file it would give FileNotFoundError.

#read is use to read file and print it's content.
print(myfile.read())
#But if we print second time it would display nothing because the cursor was at end after printing first time.
print(myfile.read())
#print(myfile1.read())

#So to correct this we can use seek() which can reset our cursor at particular pos.
myfile.seek(0)
print(myfile.read())

#We can also use readlines(). It gives us list of lines in the file.
myfile.seek(0)
list1=myfile.readlines()
print(list1)

#It is use to close the file.It is very important.
myfile.close()
myfile1.close()

#New way to open,use and read file
with open('abc.txt') as new_file:
    new_file_content=new_file.read()
print(new_file_content)

#open() with mode
with open('abc.txt',mode='r') as new_file1:
    new_file1_content=new_file1.read()
    print(new_file1_content)


