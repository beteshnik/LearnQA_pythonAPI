import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# 1) создавал задачу
response_without_params = requests.get(url, verify=False)
json_without_params = response_without_params.json()
params = {"token": json_without_params["token"]}
secs = json_without_params["seconds"]

# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
response_not_complete = requests.get(url, params=params, verify=False)
json_not_complete = response_not_complete.json()
status_not_complete = json_not_complete["status"]
status_not_complete_expected = "Job is NOT ready"
status_not_complete_is_correct = status_not_complete == status_not_complete_expected
print(f"Отображается корректный статус {status_not_complete_expected}?: {status_not_complete_is_correct}")

# 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
if status_not_complete_is_correct:
    print(f"Ждём {secs} секунд")
time.sleep(secs)

# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова,
response_complete = requests.get(url, params=params, verify=False)
json_complete = response_complete.json()
status_complete = json_complete["status"]
status_complete_expected = "Job is ready"

# убеждался в правильности поля status
status_complete_is_correct = status_complete == status_complete_expected
print(f"Отображается корректный статус {status_complete_expected}?: {status_complete_is_correct}")

# и наличии поля result
try:
    result = json_complete["result"]
    print(f"Присутствует поле result: {result}")
except KeyError:
    print("Отутствует поле result")
