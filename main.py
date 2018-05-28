import requests as rq
import sys
from problem import Problem

tags = set(sys.argv[1:])

response = rq.get('http://codeforces.com/api/problemset.problems').json()

problems = []
for kv, stat in zip(response['result']['problems'], response['result']['problemStatistics']):
    if (tags.issubset(kv['tags'])):
        problems.append(Problem(kv['contestId'], kv['index'], kv['name'], kv['tags'], stat['solvedCount']))

problems.sort(key=lambda x: x.solved_cnt, reverse=True)


for p in problems:
    print(p)
