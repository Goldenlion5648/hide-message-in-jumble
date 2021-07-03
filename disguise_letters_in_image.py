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


def diguise_multiple(filenames: List[str]):

    num_files = len(filenames)

    pos_to_num = get_pos_to_num(filenames)
    positions_needed = get_positions_needed(filenames)
    max_width, max_height = get_width_and_height(filenames)

    combos = get_combos(len(filenames), positions_needed)

    letters_used_for_each_group, available_letters = get_letters_used_for_each_group_and_available_letters(
        num_files, combos)

    output = get_output(max_width, max_height, available_letters,
                        pos_to_num, letters_used_for_each_group)
    get_answers(output, letters_used_for_each_group)


def get_positions_needed(filenames):
    positions_needed = defaultdict(set)
    for img_num, file in enumerate(filenames):
        with open(file) as f:
            a = f.read().strip().split("\n")
        for y in range(len(a)):
            for x in range(len(a[0])):
                if a[y][x] != a[0][0]:
                    positions_needed[img_num].add((y, x))
    return positions_needed


def get_width_and_height(filenames):
    max_width = 0
    max_height = 0
    for file in filenames:
        with open(file) as f:
            a = f.read().strip().split("\n")
        max_height = max(max_height, len(a))
        max_width = max(max_width, len(a[0]))
    return max_width, max_height


def get_pos_to_num(filenames):
    pos_to_num = defaultdict(set)
    for img_num, file in enumerate(filenames):
        with open(file) as f:
            a = f.read().strip().split("\n")
        for y in range(len(a)):
            for x in range(len(a[0])):
                if a[y][x] != a[0][0]:
                    pos_to_num[(y, x)].add(img_num)
    return pos_to_num


def get_combos(num_files, positions_needed):
    combos = []
    for j in range(2, num_files+1):
        combos += list(combinations(range(num_files), j))
    overlaps = {}
    for c in combos:
        cur = positions_needed[c[0]]
        # print("start", cur)
        for i in range(1, len(c)):
            cur &= positions_needed[c[i]]
        overlaps[c] = cur
    return combos


def get_letters_used_for_each_group_and_available_letters(num_files, combos):
    letters_used_for_each_group = defaultdict(list)
    num_letters_per = 7-num_files
    available_letters = set(string.ascii_letters)
    if num_files > 3:
        available_letters += set("@!#$"+string.digits)
    singles = list(range(num_files))
    pooled = reversed(singles + combos)
    # pooled = singles
    for num_group in pooled:
        chosen = (random.sample(sorted(available_letters), num_letters_per))
        letters_used_for_each_group[num_group] += chosen
        available_letters -= set(chosen)

    # for k, v_ in letters_used_for_each_group.items():
    #     print(k, "".join(v_))
    # print(pos_to_num)
    return letters_used_for_each_group, available_letters

    # exit()


def get_output(max_width, max_height, available_letters, pos_to_num, letters_used_for_each_group):
    output = [["0"]*max_width for i in range(max_height)]
    available_letters = sorted(available_letters)
    # print("remaining available_letters", len(available_letters))
    for y in range(len(output)):
        for x in range(len(output[0])):
            if (y, x) not in pos_to_num:
                output[y][x] = random.choice(available_letters)
                continue
            # cur = (pos_to_num[(y, x)])
            cur = tuple(sorted(pos_to_num[(y, x)]))
            if len(cur) == 1:
                cur = cur[0]
            output[y][x] = random.choice(sorted(letters_used_for_each_group[cur]))
    return output
    

def get_answers(output, letters_used_for_each_group, output_file: str = "multiple_output"):
    answers = defaultdict(list)
    # for i in range(num_files):
    for j, value in letters_used_for_each_group.items():
        try:
            for num in j:
                answers[num].extend(letters_used_for_each_group[j])
        except:
            answers[j].extend(value)
    for k, v in answers.items():
        print(k, ":", "".join(v))


    with open(f"{output_file}.txt", 'w') as f:
        for line in output:
            print(*line, sep='', file=f)
