from enum import Enum


class Verdict(Enum):
    NA = -1
    FAIL = 0
    AC = 1


class Problem:
    def __init__(self, contestID, index, name, tags, cnt, verdict=Verdict.NA):
        self._name = name
        self._solved_cnt = cnt
        self._tags = tags
        self._contestID = contestID
        self._index = index
        self._verdict = verdict

    def get_id(self):
        return str(self.contestID) + self.index

    def get_url(self):
        return "http://codeforces.com/problemset/problem/{0}/{1}".format(self._contestID, self._index)

    def __str__(self):
        return "name = {0}, solved = {1} tags = {2}".format(self._name, self._solved_cnt, self._tags)

    @property
    def verdict(self):
        return self._verdict

    @verdict.setter
    def verdict(self, v):
        self._verdict = v

    @property
    def contestID(self):
        return self._contestID

    @property
    def index(self):
        return self._index

    @property
    def name(self):
        return self._name

    @property
    def tags(self):
        return self._tags

    @property
    def solved_cnt(self):
        return self._solved_cnt

    @solved_cnt.setter
    def solved_cnt(self, cnt):
        self._solved_cnt = cnt