#this code is an AI driven appliction based on symptoms
#Malaria=['headache', 'fever', 'flu']
#Covid_19=['sore-throath', 'pink eyes', 'muscle and joint pain']

while True:
    Q_1=input('Are you sick??(y/n):')
    if Q_1.casefold()=='n':
        print('Thank you for using ZIMA')
        quit()
    else:
        Q_2=input('Do you feel feverish, cold, Headache, flu? (y/n):')
        if Q_2.casefold()== 'y':
            print('You show symptoms of Malaria')
            Q_3=input('Do you want to see a doctor??(y/n):')
            if Q_3.casefold()=='y':
                print('Link to a doctor')
                quit()
            else:
                print('Thank you for using Zima')
                quit()
        else:
            break
while True:
    Q_4=input('do you feel muscle and joint pains, pink eyes, sore-throath??(y/n):')
    if Q_4=='y':
        print('You have symptoms of Covid_19')
        Q_5=input('do you want to see a doctor??(y/n):')
        if Q_5.casefold()=='y':
            print('link to a doctor')
            quit()
        else:
            print('thank you for using ZIMA')
    else:
        print('Thank you for using ZIMA')
        break
quit()