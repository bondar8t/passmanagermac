import os
import sys  # МАРК УОЛБЕРГ ГОВНЯШКА

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("----что ты хочешь сделать?----")
    print("1 - Добавить новый пароль")
    print("2 - Посмотреть свои пароли")
    print("3 - Удалить пароль")
    deistv = int(input("Введите число действия: "))
    if deistv == 1:
        os.system("cls" if os.name == "nt" else "clear")
        print("Введи сервис: ")
        namepassword = input()
        print("Введи пароль: ")
        password = input()

        file = open("passwords.txt", "a", encoding="utf-8")
        file.write(f"{namepassword}:{password}\n")
        file.close()
        print("Сохранён пароль: ", namepassword, "--", password)
        print("Выйти:")
        print("1-Меню")
        deistv2 = input()
        if deistv2 == 1:
            continue
        if deistv2 == 2:
            sys.exit()

    if deistv == 2:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n--- Твои сохраненные чупапы ---")
        file = open("passwords.txt", "r", encoding="utf-8")
        for line in file:
            line = line.strip()
            name, pwd = line.split(":")
            print(f"Сервис: {name} | Пароль : {pwd}")
        file.close()

        print("Выйти:")
        print("1-Меню")
        deistv2 = input()
        if deistv2 == 1:
            continue
        if deistv2 == 2:
            sys.exit()

    if deistv == 3:
        os.system("cls" if os.name == "nt" else "clear")
        file = open("passwords.txt", "r", encoding="utf-8")
        for line in file:
            line = line.strip()
            name, pwd = line.split(":")
            print(f"Сервис: {name} | Пароль : {pwd}")
        passdelet = input("Введи сервис для удаления: ").strip()
        file = open("passwords.txt", "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        new_lines = []
        for line in lines:
            if line.strip():
                service, pwd = line.strip().split(":", 1)
                if service != passdelet:
                    new_lines.append(line)
        file = open("passwords.txt", "w", encoding="utf-8")
        file.writelines(new_lines)
        file.close()
        print(f"ЧУПАПИ! Пароль для говняшки {passdelet} удалён!")
        print("Выйти:")
        print("1-Меню")
        deistv2 = input()
        if deistv2 == 1:
            continue
        if deistv2 == 2:
            sys.exit()
