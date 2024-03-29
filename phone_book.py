def show_menu():
    print('1. Распечатать справочник '
        '2. Найти телефон по фамилии '
        '3. Изменить номер телефона '
        '4. Удалить запись '
        '5. Найти абонента по номеру телефона '
        '6. Добавить абонента в справочник '
        '7. Закончить работу ', sep = '\n')
    choice=int(input())
    return choice

def find_by_lastname(phone_book,last_name):
    for i in range(len(phone_book)):
        nowPhone = phone_book[i]
        if (last_name == nowPhone['Фамилия']):
            return "Телефон: " + nowPhone['Телефон']
    return "Такой фамилии нет или фамилия написана неправильно (запись устойчива к регистру)"

def change_number(phone_book,last_name,new_number):
    for i in phone_book:
        nowPhone = i
        if (last_name == nowPhone['Фамилия']):
            nowPhone['Телефон'] = new_number
            return nowPhone
    return "Такой фамилии нет или фамилия написана неправильно (запись устойчива к регистру)"

def delete_by_lastname(phone_book,lastname):
    for i in range(len(phone_book)):
        nowPhone = phone_book[i]
        if (lastname == nowPhone['Фамилия']):
            phone_book.pop(i)
            return "Успешно удалено"
    return "Такой фамилии нет или фамилия написана неправильно (запись устойчива к регистру)"
    
def find_by_number(phone_book,number):
    for i in range(len(phone_book)):
        nowPhone = phone_book[i]
        if (number == nowPhone['Телефон']):
            return nowPhone
    return "Такого телефона нет"

def read_txt(filename):

    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r', encoding='utf-8') as phb:

        for line in phb:
            if (len(line) > 1):
                line = line.replace("\t", "").replace("\n", " ")
                record = dict(zip(fields, line.split(',')))        
                record['Фамилия'] = record['Фамилия'].replace(" ", "") 
                record['Имя'] = record['Имя'].replace(" ", "")
                record['Телефон'] = record['Телефон'].replace(" ", "")
                phone_book.append(record)

    return phone_book

def add_user(phone_book,user_data):
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    line = user_data.replace("\t", "").replace("\n", " ")
    record = dict(zip(fields, line.split(',')))               
    phone_book.append(record)

    return phone_book

def write_txt(filename , phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')


def work_with_phonebook():
    choice=show_menu()
    phone_book = read_txt('phone_book.txt')
    
    while (choice!=7):
        if choice==1:
            for i in range(len(phone_book)):
                print(i + 1, f" {phone_book[i]}")
            print()
        elif choice==2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book,last_name))
            print()
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new number ')
            print(change_number(phone_book,last_name,new_number))
            print()
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
            print()
        elif choice==5:
            number = input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            phone_book = add_user(phone_book,user_data)
            write_txt('phone_book.txt',phone_book)
        choice=show_menu()

work_with_phonebook()