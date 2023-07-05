from faker import Faker
import random

fake = Faker('ru_RU') # оставляем эту переменную как глобальную


def add_user_address(address):
    with open('user_address.txt', 'a') as file_address:
        file_address.write(f'{address}\n')


def add_user_email(email):
    with open('user_email.txt', 'a') as file_email:
        file_email.write(f'{email}\n')


def add_user_phone(phone):
    with open('user_phone.txt', 'a') as file_phone:
        file_phone.write(f'{phone}\n')


def add_username(username):
    with open('user_name.txt', 'a') as file_username:
        file_username.write(f'{username}\n')


def random_generate():
    for _ in range(1,21):
        first_name = f'{fake.first_name()}'
        last_name = f'{fake.last_name()}'
        age = random.randint(10,30)
        phone = f'{fake.phone_number()}'

        add_username(first_name)
        add_user_address(last_name)
        add_user_email(age)
        add_user_phone(phone)


# random_generate()


def get_user():
    user_list = []
    with open('user_name.txt', 'r') as file_name:
        for username in file_name:
            user_list.append(username.strip())


    user_address_list = []
    with open('user_address.txt', 'r') as file_address:
        for address in file_address:
            user_address_list.append(address.strip())


    user_email_list = []
    with open('user_email.txt', 'r') as file_email:
        for email in file_email:
            user_email_list.append(email.strip())


    user_phone_list = []
    with open('user_phone.txt', 'r') as file_phone:
        for phone in file_phone:
            user_phone_list.append(phone.strip())
            

    # print(user_list[1:10]) # вывели 10 первых значений
    # print(user_address_list[1:10])
    # print(user_email_list[1:10])
    # print(user_phone_list[1:10])


    # a = user_list[0]
    # b = user_address_list[0]
    # c = user_email_list[0]
    # d = user_phone_list[0]

    # print(a,b,c,d)


    for i in range(10):
        print(user_list[i %len(user_list)],
              user_address_list [i %len( user_address_list)], 
              user_email_list[i % len( user_email_list)],
              user_phone_list[i % len (user_phone_list)])

    

get_user()