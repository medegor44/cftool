import requests as rq
import sys
import json
from problem import Problem


def html_print(problems, file):
    file.write("<!DOCTYPE html>")
    file.write("<html>\n")
    file.write("  <head>\n")
    file.write("    <meta charset=\"utf-8\">")
    file.write("  </head>\n")

    file.write("  <table border='1'>\n")

    for p in problems:
        file.write("    <tr>\n")

        file.write("      <td>\n")
        file.write("<a href={0}>{1}</a>\n".format(p.get_url(), p.name))
        file.write("      </td>\n")

        file.write("    </tr>\n")

    file.write("  </table>\n")

    file.write("</html>")


t = sys.argv[1:]

for i in range(len(t)):
    t[i] = t[i].replace('_', ' ')

tags = set(t)

try:
    response = rq.get('http://codeforces.com/api/problemset.problems?locale=ru').json()

    problems = []
    for kv, stat in zip(response['result']['problems'], response['result']['problemStatistics']):
        if tags.issubset(kv['tags']):
            problems.append(Problem(kv['contestId'], kv['index'], kv['name'], kv['tags'], stat['solvedCount']))

    problems.sort(key=lambda x: x.solved_cnt, reverse=True)

    html_print(problems, open("index.html", "w"))
except IOError:
    print("Can't connect to Codeforces. Wait a bit or check your Internet connection.")
except json.JSONDecodeError:
    print("Codeforces does't respond.")


