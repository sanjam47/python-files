try:
    num2=input('Enter a no:')
    add=10+num2
except Exception as e:
    print(e)
else:
    print(add)
finally:
    print('I always run.')


try:
    num2=input('Enter a no:')
    add=10+num2
except:
    print('You are not entering a no.')
else:
    print(add)
finally:
    print('I always run.')
    
