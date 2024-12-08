import datetime, os, re
import requests
import pytz

current_time = datetime.datetime.now(pytz.timezone('US/Eastern'))
print("Time is " + current_time.strftime("%Y-%m-%d %H:%M:%S"))
year = current_time.year
day = current_time.day

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

test_path = "day{:02d}/input_test.txt".format(day)
open(test_path, 'a').close()

code_path = "day{:02d}/main{:02d}p1.py".format(day, day)
with open(code_path, 'w+') as fp:
    fp.write("open(\"input_test.txt\").read().splitlines()")

code_path = "day{:02d}/main{:02d}p2.py".format(day, day)
with open(code_path, 'w+') as fp:
    fp.write("open(\"input_test.txt\").read().splitlines()")


