num1=0

while(num1<5):
    print(f'The number is {num1}')
    num1+=1
else:
    print('The number is >=5')

name1='Saaaaaaaaaaaaaaaaaaaaaaaaaamith'
for letter in name1:
    if(letter=='a'):
        continue
    print(letter,end='')