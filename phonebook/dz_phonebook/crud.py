import csv
import os.path
import string
import logger as lg


db_file_name = ''
db = []
global_id = 0  # id для добавления пользователей


def init_data_base(file_name='base_phone.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if(row[0] != 'ID'):
                    db.append(row)
                    if(int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(name='', surname='', number='', email=''):
    global global_id
    global db
    global db_file_name
    if(name == ''):
        print("ALARM NO NAME SPECIFIED!!!!!1111")
        return
    if(surname == ''):
        print("ALARM NO SURNAME SPECIFIED!!!!!")
        return
    if(number == ''):
        print("ALARM NO TELEPHONE NUMBER SPECIFIED!!!!")
        return
    if(email == ''):
        print("ALARM NO EMAIL SPECIFIED!!!!!")
        return

    for row in db:
        if(row[1] == name.title() and row[2] == surname.title() and row[3] == number and row[4] == email.lower()):
            print("already exist")
            return

    global_id += 1
    new_row = [str(global_id), name.title(),
               surname.title(), number, email.lower()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


# поиск (если нужно выгрузить все: result = retrive())
def retrive(id='', name='', surname='', number='', email=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if(name != '' and row[1] != name.title()):
            continue
        if(surname != '' and row[2] != surname.title()):
            continue
        if(number != '' and row[3] != number):
            continue
        if(email != '' and row[3] != email.lower()):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Контакты не найдены'
    else:
        return result


def update(id='', new_name='', new_surname='', new_number='', new_email=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for update')
        return
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            if(row[0] == id):
                if(new_name != ''):
                    row[1] = new_name.title()

                if(new_surname != ''):
                    row[2] = new_surname.title()

                if(new_number != ''):
                    row[3] = new_number

                if(new_email != ''):
                    row[3] = new_email.lower()

            writer.writerow(row)


def export(id='', new_name='', new_surname='', new_number='', new_email=''):
    global global_id
    global db
    global db_file_name
   
    export_file = open(input('Введите путь к файлу из которого импортировать: '), 'r')
    i = 0
    with open('base_phone.csv', 'a') as csvF:
        writer = csv.writer(csvF)

        while i < 1000:
            href = export_file.readline('***').rstrip()
            writer.writerow([href])
            i = i + 1


def delete(id=''):
    global global_id
    global db
    global db_file_name
    if(id == ''):
        print('specify id for delete')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)


def write_file_txt():
    file_in= open("base_phone.csv",'r')
    file_out = open("base_phone.txt",'w')
    file_out.write(file_in.read().replace('\n', '***').replace('\r', '|||'))


def get_token():
    file = open('token.txt', 'r')
    for i in file:
        token = i
    file.close()
    return token




