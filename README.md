# Опиание
Cftool -- программа для создания тематической выборки задач с сайта [Codeforces](codeforces.com).

# Работа
Для работы необходим Python 3 или выше и установленная библиотека requests. При запуске необходимо указать теги задач 
которые следует выбрать с сайта. Первым в списке параметров указывается хендл на 
Codeforces, затем список тегов задач. Например:

    python3 main.py strings hashing

Чтобы настроить свой язык и хедл на Codeforces следует воспользоваться параметром `-s`:
    
    python3 main.py -s

# Теги задач 
    *special
    2-sat
    binary_search
    bitmasks
    brute_force
    chinese_remainder_theorem
    combinatorics
    constructive_algorithms
    data_structures
    dfs_and_similar
    divide_and_conquer
    dp
    dsu
    expression_parsing
    fft
    flows
    games
    geometry
    graph_matchings
    graphs
    greedy
    hashing
    implementation
    math
    matrices
    meet-in-the-middle
    number_theory
    probabilities
    schedules
    shortest_paths
    sortings
    string_suffix_structures
    strings
    ternary_search
    trees
    two_pointers