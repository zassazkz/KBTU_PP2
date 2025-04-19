import psycopg2

def connect():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="T96k58O72",
        host="localhost",
        port="5432"

    )

def insert_or_update_user():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("Успешно добавлено или обновлено.")
    cur.close()
    conn.close()

def search_by_pattern():
    pattern = input("Введите шаблон (часть имени или номера): ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    if rows:
        print("Результаты поиска:")
        for row in rows:
            print(row)
    else:
        print("Ничего не найдено.")
    cur.close()
    conn.close()

def delete_user():
    name = input("Имя (нажмите Enter, если не удаляете по имени): ") or None
    phone = input("Телефон (нажмите Enter, если не удаляете по номеру): ") or None
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s, %s)", (name, phone))
    conn.commit()
    print("Успешно удалено.")
    cur.close()
    conn.close()

def show_all_users():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_all_users()")
    rows = cur.fetchall()
    if rows:
        print("Все записи:")
        for row in rows:
            print(row)
    else:
        print("Таблица пуста.")
    cur.close()
    conn.close()

def menu():
    while True:
        print("""
           PHONEBOOK MENU №2   
        1 - Добавить или обновить
        2 - Поиск по шаблону
        3 - Удалить по имени/номеру
        4 - Показать все записи
        0 - Выйти
        """)
        choice = input("Выберите действие: ")
        if choice == "1":
            insert_or_update_user()
        elif choice == "2":
            search_by_pattern()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            show_all_users()
        elif choice == "0":
            print("До встречи!")
            break
        else:
            print("Неверный ввод. Попробуйте ещё раз.")

if __name__ == "__main__":
    menu()