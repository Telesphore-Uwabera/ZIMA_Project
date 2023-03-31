#this code is an AI driven appliction based on symptoms
#Malaria=['headache', 'fever', 'flu']
#Covid_19=['sore-throath', 'pink eyes', 'muscle and joint pain']

'''while True:
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
            quit()
    else:
        print('Thank you for using ZIMA')
        break
quit()'''


import webbrowser

# Define the symptoms and illnesses.
symptoms = {
    'fever, headache and chills': 'malaria',
    'diarrhea, vomiting, leg cramps, thrist,  irritability': 'cholera',
    'cough, sneezing, runny nose, sore throat, high temperature': 'covid-19',
    # Add more symptoms and illnesses here
}

# Ask the user to choose a symptom
while True:
    print('Please choose a symptom:')
    for i, symptom in enumerate(symptoms.keys()):
        print(f'{i+1}. {symptom}')
    try:
        choice = int(input('Enter a number: '))
        symptom = list(symptoms.keys())[choice-1]
        break
    except (ValueError, IndexError):
        print('Invalid input, please try again.')

# Prompt the user with the name of the illness
illness = symptoms[symptom]
print(f'You may have {illness}.')

# Ask the user if they want to see a doctor
while True:
    choice = input('Do you want to see a doctor? (yes/no) ').casefold()
    if choice == 'yes':
        webbrowser.open('https://www.nyarugengehospital.gov.rw/services/doctors')
        break
    elif choice == 'no':
        while True:
            try:
                learn_more = input('Do you want to learn more about your illness? (yes/no): ').casefold()
                if learn_more == 'yes':
                    webbrowser.open('https://www.who.int/news-room/questions-and-answers/item/malaria?gclid=Cj0KCQjwiZqhBhCJARIsACHHEH-v6nXsP2nyyCfMyx17mZ4hMxV1Vcw-QqL1uDO6V9MlFXCXmJCBV4EaAuUNEALw_wcB')
                    break
                elif learn_more == 'no':
                    break
                else:
                    print('Invalid input, please try again.')
            except ValueError:
                print('Invalid input, please try again.')
        break  # Exit the loop and end the program after the user chooses to learn more
    else:
        print('Invalid input, please try again.')

# Close the program with a message
print('Thank you for using ZIMA')

