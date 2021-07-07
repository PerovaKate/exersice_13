# x = input('enter any number')
# if x == '7':
#     print('7 is a lucky number! Today is your lucky day')
# else:
#     print('Thank you! Have a nice day')

height = input('Ваш рост')
weight = input('Ваш вес')
bmi = int(weight)/int(height)**2*10000
print('''{0:2.2f}'''.format(bmi))
if bmi <= 18.4:
    print('Дистрофия')
elif bmi <= 25.0:
    print('Ваш ИМТ в норме')
elif bmi <= 30.0:
    print('У вас предожирение')
elif bmi <= 35.0:
    print('У вас ожирение 1 степени')
elif bmi <= 40.0:
    print('У вас ожирение 2 степени')
elif bmi >= 40.1:
    print('У вас ожирение 3 степени')

