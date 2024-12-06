import datetime, os, re
import requests

year = datetime.datetime.now().year
day = datetime.datetime.now().day

for day in range(1,6):
    input_path = "day{:02d}/input.txt".format(day)
    with open("cookies.txt", "r") as file:
        for line in file:
            match = re.search(r'session=([a-f0-9]+)$', line)
            if match:
                session_value = match.group(1)
                break

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"cookie": f"session={session_value}",
               "User-Agent": "github.com/albertominetti/adventofcode2024-python"}

    r = requests.get(url, headers=headers)
    content = r.text
    os.makedirs(os.path.dirname(input_path), exist_ok=True)
    with open(input_path, 'w+') as fp:
        fp.write(content)

    code_path = "day{:02d}/main.py".format(day)
    with open(code_path, 'w+') as fp:
        fp.write("")

    test_path = "day{:02d}/input_test.txt".format(day)
    open(test_path, 'a').close()

