#importing pyjokes library
import pyjokes
#fetching the joke
joke1=pyjokes.get_joke(language='en',category='all')
#displaying the joke
print(joke1)
joke2=pyjokes.get_joke(language='en',category='all')
print(joke2)
for i in range(5):
    print(i+1,".",joke1)