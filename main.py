
import time, re
x = []
v = 0
while True:
    try:
        b = int(input("1-Регистрация 2-Авторизация"))
        if b == 1:
            i = input("Login")
            if len(i) < 5:
                time.sleep(2)
                print("Введите не мение 5 букв ")
                continue

         #       x.append({"Login":i})
            p = input("Pasword")
            if len(p) < 4:
                time.sleep(2)
                print("Пинкод слишком короткий")
                continue

          #      x.append({"Pasword":p})
            j = input("Email")
            if not re.match(r"[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+", j):
                time.sleep(2)
                print('Email error')
                continue
            else:
                x.append({"Login":i,"Pasword":p,"Email":j})
                print("Вы успешно зарегестрировались")
        if b == 2:
            d = input("Login")
            for h in x:
               # print(h['Login'])
                if h["Login"] == d:
                    print("Login is good")
                else:
                    print("Eror Login")
                    continue
                dd = input("Pasword")
                if h["Pasword"] == dd:
                    print("Пароль верный")
                    time.sleep(2)
                    print("Вы успешно авторизировались")
                else:
                    print("Ошибка")
                    continue
    except:
        print('Error')
