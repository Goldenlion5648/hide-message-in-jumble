import random
import string
from typing import List
from collections import defaultdict
from itertools import combinations


def disguise(filename, password):
    with open(f"{filename}_as_data.txt") as f:
        a = f.read().split("\n")

    a = list(map(list, a))
    # blacklist = "evergreen"
    blacklist = list(set(password))
    allowed = list(set(string.ascii_lowercase) - set(blacklist))
    for i, line in enumerate(a):
        for j, letter in enumerate(line):
            if a[i][j] == "1":
                a[i][j] = random.choice(allowed)
            else:
                a[i][j] = random.choice(blacklist)
        a[i] = "".join(a[i])

    with open(f"{filename}_jumbled.txt", 'w') as f:
        print("\n".join(a), file=f)


def diguise_multiple(filenames: List[str], message: List[str], output_file="multiple_output", num_letters_per=3):
    positions_needed = defaultdict(set)
    pos_to_num = defaultdict(set)
    num_files = len(filenames)
    max_width = 0
    max_height = 0
    for img_num, file in enumerate(filenames):
        with open(file) as f:
            a = f.read().strip().split("\n")
        max_height = max(max_height, len(a))
        max_width = max(max_width, len(a[0]))
        # print(a)
        for y in range(len(a)):
            for x in range(len(a[0])):
                if a[y][x] != a[0][0]:
                    positions_needed[img_num].add((y, x))
                    pos_to_num[(y, x)].add(img_num)
    combos = []
    # print(positions_needed)
    # print(len(pos_to_num))
    # exit()
    # print(num_files)
    for j in range(2, num_files+1):
        combos += list(combinations(range(num_files), j))
    overlaps = dict()
    for c in combos:
        cur = positions_needed[c[0]]
        # print("start", cur)
        for i in range(1, len(c)):
            cur &= positions_needed[c[i]]
        overlaps[c] = cur
    # [print(overlaps, "\n") for i in overlaps]
    singles = list(range(num_files))
    # print(combos + singles)
    # print(combos)
    letters_used_for_each_group = defaultdict(list)
    available_letters = set(string.ascii_letters)
    if num_files > 3:
        available_letters += set("@!#$"+string.digits)
    pooled = reversed(singles + combos)
    # pooled = singles
    for num_group in pooled:
        chosen = (random.sample(sorted(available_letters), num_letters_per))
        letters_used_for_each_group[num_group] += chosen
        available_letters -= set(chosen)

    for k in letters_used_for_each_group:
        print(k, "".join(letters_used_for_each_group[k]))
    # print(pos_to_num)

    # exit()
    output = [["0"]*max_width for i in range(max_height)]
    available_letters = sorted(available_letters)
    print("remaining available_letters", len(available_letters))
    times_used = defaultdict(int)
    for y in range(len(output)):
        for x in range(len(output[0])):
            if (y, x) not in pos_to_num:
                output[y][x] = random.choice(available_letters)
                continue
            cur = (pos_to_num[(y, x)])
            cur = tuple(sorted(cur))
            if len(cur) == 1:
                cur = cur[0]
            # options = [letters_used_for_each[z] for z in pos_to_num[(y, x)]]
            # times_used[tuple(sorted(pos_to_num[(y, x)]))] += 1
            output[y][x] = random.choice(sorted(letters_used_for_each_group[cur]))
            # output[y][x] = random.choice(options)
    answers = defaultdict(list)
    # for i in range(num_files):
    for j in letters_used_for_each_group:
        try:
            for num in j:
                answers[num].extend(letters_used_for_each_group[j])
        except:
            answers[j].extend(letters_used_for_each_group[j])
    for k, v in answers.items():
        print(k, ":", "".join(v))

    # for k, v in times_used.items():
    #     print(k, ":", v)
    print("times_used", len(times_used))
    # print("letters_used_for_each", len(letters_used_for_each))
    # print("punc", len(string.punctuation))
    with open(f"{output_file}.txt", 'w') as f:
        for line in output:
            print(*line, sep='', file=f)
