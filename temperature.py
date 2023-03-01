Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> temperature= input(('Input the temperature (included °C  or °F or K)\n> '))
... temperature= temperature.split(' ')
... temperature[1]= temperature[1].lower()
... # print(temperature)
... 
... if temperature[1] == '°c':
...     # print('C')
...     temperature.insert(2, round(int(temperature[0])))
... 
... elif temperature[1] == '°k':
...     # print('F')
...     temperature.insert(2, round((int(temperature[0])-32)*5/9))
... 
... elif temperature[1] == 'k':
...     # print('K')
...     temperature.insert(2, round(int(temperature[0])-273.15))
... 
... else:
...     print('3rr0r')
... 
... temperature.insert(3, round(temperature[2]*9/5+32))
... temperature.insert(4, round(temperature[2]+273.15))
... 
