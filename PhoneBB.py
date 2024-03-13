def work_with_phonebook():

    choice=show_menu()

    phone_book=read_txt('phonebook.txt')

    while (choice!=8):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
	    	
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)
        elif choice == 7:
            NumberLine = int(input("Номер строки "))
            with open('phonebook.txt', 'r') as phonebook:
                line = phonebook.readlines()

                element = line[NumberLine]
            with open('NewFile.txt', 'a') as file2:
                file2.write(element)

        choice=show_menu()


def show_menu():
    print("\n Выберите команду:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонент по фамилии\n"
          "3. найти абонент по номеру\n"
          "4.  Добавить абонент в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу\n"
          "7. Найти номер по строке")
    choice = int(input())
    return choice



def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:

           record = dict(zip(fields, line.split(',')))
	     
    phone_book.append(record)	

    return phone_book

def write_txt(filename , phone_book):

    with open('phonebook.txt','w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')

work_with_phonebook()
