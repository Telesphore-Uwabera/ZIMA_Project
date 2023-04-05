# !/usr/bin/python3
import webbrowser
from login import my_cursor

database = my_cursor.fetchall()


def check_login(name, passwd):
    new = database
    for user in new:
        if name in user and passwd in user:
            # Return the password if the name is found
            return True


print('WELCOME TO ZIMA')

while True:
    try:
        login = input('Do you have an account? (y/n): ').casefold()
        if login not in ['y', 'n']:
            raise ValueError
        else:
            break
    except ValueError:
        print("Invalid input. Please input 'y' or 'n'.")

if login == 'y':
    while True:
        try:
            name = input("Please enter your name: ")
            passwd = input("Enter password: ")
            check_login(name, passwd)
            if check_login(name, passwd):
                print("Login successful")
                break
            else:
                print("Wrong details. Do you want to try again or visit the login page to register?")
                choice = input("Please enter 'try again' or 'visit': ").casefold()
                if choice == 'try again':
                    continue
                elif choice == 'visit':
                    print('Please, visit the login page.')
                    raise AttributeError(' Goodbye!')
                else:
                    print("Invalid input, please try again.")
        except AttributeError as a:
            print(a)
            quit()# quit the programe here
        except:
            print("Wrong input, please try again")
        

elif login == 'n':
    print("Please visit the sign in page to register")
    quit()  # quit the program

else:
    raise ValueError("Invalid input, please try again.")

import webbrowser


# Define the symptoms and illnesses as a dictionary.
SYMPTOMS = {
    'fever, headache, and chills': {
        'illness': 'malaria',
        'description': 'Malaria is a disease caused by a parasite. It is spread through the bite of an infected mosquito. The symptoms include fever, headache, and chills. Treatment usually involves medication.',
        'link': 'https://www.who.int/news-room/fact-sheets/detail/malaria'
    },
    'diarrhea, vomiting, leg cramps, thirst, and irritability': {
        'illness': 'cholera',
        'description': 'Cholera is a bacterial infection that can cause severe diarrhea and dehydration. It is spread through contaminated water or food. Treatment involves rehydration therapy and antibiotics.',
        'link': 'https://www.who.int/news-room/fact-sheets/detail/cholera'
    },
    'cough, sneezing, runny nose, sore throat, and high temperature': {
        'illness': 'covid-19',
        'description': 'COVID-19 is a respiratory illness caused by the SARS-CoV-2 virus. It is spread through respiratory droplets when an infected person talks, coughs, or sneezes. The symptoms include cough, fever, and difficulty breathing. Treatment involves supportive care and in some cases, antiviral medication.',
        'link': 'https://www.who.int/health-topics/coronavirus#tab=tab_1'
    },
    # Add more symptoms and illnesses here
}

# Ask the user to choose a symptom.
while True:
    print('Please choose a list of symptoms:')
    for i, symptom in enumerate(SYMPTOMS.keys()):
        print(f'{i+1}. {symptom}')
    try:
        choice = int(input('Enter a number: '))
        symptom = list(SYMPTOMS.keys())[choice-1]
        break
    except (ValueError, IndexError):
        print('Invalid input, please try again.')

# Prompt the user with the name of the illness and its description.
illness = SYMPTOMS[symptom]['illness']
description = SYMPTOMS[symptom]['description']
print(f'You may have {illness}.')
print(description)

# Ask the user if they want to learn more or see a doctor.
while True:
    choice = input('Do you want to learn more about your illness or see a doctor? (learn/doctor/none) ').casefold()
    if choice == 'learn':
        webbrowser.open(SYMPTOMS[symptom]['link'])
        break
    elif choice == 'doctor':
        webbrowser.open('https://www.nyarugengehospital.gov.rw/services/doctors')
        break
    elif choice == 'none':
        break
    else:
        print('Invalid input, please try again.')

# Close the program with a message.
print('Thank you for using ZIMA.')