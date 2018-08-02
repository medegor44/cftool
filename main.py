import requests as rq
import sys
import webbrowser
import json
import os
from problem import Problem, Verdict

# prints list of problems into simple html table
def html_print(problems, file):
    file.write("<!DOCTYPE html>")
    file.write("<html>\n")
    file.write("  <head>\n")
    if not os.name == "nt":
        file.write("    <meta charset=\"utf-8\">")
    else:
        file.write("    <meta charset=\"windows-1251\">")
    file.write("  </head>\n")

    file.write("  <table border='1'>\n")

    for p in problems:
        color = 'white'
        if p.verdict == Verdict.AC:
            color = '#ADFF2F'
        elif p.verdict == Verdict.FAIL:
            color = '#FA8072'

        file.write("    <tr>\n")

        file.write("      <td bgcolor={0}>\n".format(color))
        file.write("        <a href={0}?locale={1}>{2}</a>\n".format(p.get_url(), lang, p.name))
        file.write("      </td>\n")

        file.write("    </tr>\n")

    file.write("  </table>\n")

    file.write("</html>")

    file.close()


# gets problems with some tags from Codeforces
def get_problems(lang, tags):
    api_problems_request = "http://codeforces.com/api/problemset.problems?lang={0}&tags={1}".format(lang,
                                                                                                    ';'.join(tags))
    problems_response = rq.get(api_problems_request).json()

    problems = []
    for kv, stat in zip(problems_response['result']['problems'], problems_response['result']['problemStatistics']):
        problems.append(Problem(kv['contestId'], kv['index'], kv['name'], kv['tags'], stat['solvedCount']))

    return problems


# checks which problems were solved
def check_solved(lang, user, problems):
    verdicts = {}
    for p in problems:
        verdicts[p.get_id()] = p.verdict

    api_user_stat_request = "http://codeforces.com/api/user.status?lang={0}&handle={1}&from=1".format(lang, user)
    response = rq.get(api_user_stat_request).json()

    for submission in response['result']:
        if not 'contestId' in submission['problem']:
            continue

        id = str(submission['problem']['contestId']) + submission['problem']['index']
        verdict = submission['verdict']

        verd = Verdict.FAIL

        if verdict == "OK":
            verd = Verdict.AC

        if id in verdicts:
            old_verdict = verdicts[id]
            verdicts[id] = verd if old_verdict != Verdict.AC else old_verdict

    for problem in problems:
        id = problem.get_id()
        if id in verdicts:
            problem.verdict = verdicts[id]


def setup():
    print('Enter your cf handle')
    handle = input()
    print('Select language (en/ru)')
    lang = input()

    if str.lower(lang) not in ('ru', 'en'):
        lang = 'en'

    json.dump({'lang' : lang, 'user' : handle}, open('settings.json', 'w'))


def read_settings():
    try:
        file = open('settings.json', 'r')
        settings = json.load(file)

        return {'user' : settings['user'], 'lang' : settings['lang']}
    except IOError:
        return {'user' : 'N/A', 'lang' : 'en'}


try:
    if '-s' in sys.argv:
        setup()
        exit(0)

    info = read_settings()
    user = info['user']
    lang = info['lang']

    t = sys.argv[1:]

    for i in range(len(t)):
        t[i] = t[i].replace('_', ' ')

    tags = set(t)

    problems = get_problems(lang, tags)
    check_solved(lang, user, problems)

    problems.sort(key=lambda x: x.solved_cnt, reverse=True)

    html_print(problems, open("index.html", "w"))
    webbrowser.open("file://" + os.path.realpath("index.html"))

except KeyError:
    print("Please, check your cf handle or use '-s' to setup cftool")
except IOError:
    print("Can't connect to Codeforces. Wait a bit or check your Internet connection.")
except json.JSONDecodeError:
    print("Codeforces does't respond.")


