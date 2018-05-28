class Problem:
    def __init__(self, contestID, index, name, tags, cnt):
        self._name = name
        self._solved_cnt = cnt
        self._tags = tags
        self._contestID = contestID
        self._index = index

    def get_url(self):
        return "http://codeforces.com/problemset/problem/{0}/{1}".format(self._contestID, self._index)

    def __str__(self):
        return "name = {0}, solved = {1} tags = {2}".format(self._name, self._solved_cnt, self._tags)

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