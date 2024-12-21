import re
from collections import deque
from functools import cmp_to_key

num_keypad = [list(s) for s in ["789", "456", "123", " 0A"]]
num_keypad_pos = {}
for r, row in enumerate(num_keypad):
    for c, k in enumerate(row):
        num_keypad_pos[k] = (r, c)


def numpad_moves(from_letter: chr, to_letter: chr):
    if from_letter == '7' and to_letter == 'A': return ['>', '>', 'v', 'v', 'v', 'A']
    if from_letter == '7' and to_letter == '0': return ['>', '>', 'v', 'v', 'A']
    if from_letter == '4' and to_letter == 'A': return ['>', '>', 'v', 'v', 'A']
    if from_letter == '4' and to_letter == '0': return ['>', '>', 'v', 'A']
    if from_letter == '1' and to_letter == 'A': return ['>', '>', 'v', 'A']
    if from_letter == '1' and to_letter == '0': return ['>', 'v', 'A']

    if to_letter == '7' and from_letter == 'A': return ['^', '^', '^', '<', '<', 'A']
    if to_letter == '7' and from_letter == '0': return ['^', '^', '^', '<', 'A']
    if to_letter == '4' and from_letter == 'A': return ['^', '^', '<', '<', 'A']
    if to_letter == '4' and from_letter == '0': return ['^', '^', '<', 'A']
    if to_letter == '1' and from_letter == 'A': return ['^', '<', '<', 'A']
    if to_letter == '1' and from_letter == '0': return ['^', '<', 'A']

    v_moves_count = num_keypad_pos[from_letter][0] - num_keypad_pos[to_letter][0]
    h_moves_count = num_keypad_pos[from_letter][1] - num_keypad_pos[to_letter][1]

    v_moves = abs(v_moves_count) * ['^' if v_moves_count > 0 else 'v']
    h_moves = abs(h_moves_count) * ['<' if h_moves_count > 0 else '>']
    SORT_ORDER = {'<': 0, '^': 1, 'v': 2, '>': 3}
    return sorted(v_moves + h_moves, key=lambda val: SORT_ORDER[val]) + ['A']


print(numpad_moves('A', '7'))

dir_keypad = [list(s) for s in [" ^A", "<v>"]]
dir_keypad_pos = {}
for r, row in enumerate(dir_keypad):
    for c, k in enumerate(row):
        dir_keypad_pos[k] = (r, c)


def dirpad_moves(from_letter: chr, to_letter: chr):
    if from_letter == '<' and to_letter == 'A': return ['>', '>', '^', 'A']
    if from_letter == '<' and to_letter == '^': return ['>', '^', 'A']
    if from_letter == 'A' and to_letter == '<': return ['v', '<', '<', 'A']
    if from_letter == '^' and to_letter == '<': return ['v', '<', 'A']

    v_moves_count = dir_keypad_pos[from_letter][0] - dir_keypad_pos[to_letter][0]
    h_moves_count = dir_keypad_pos[from_letter][1] - dir_keypad_pos[to_letter][1]

    v_moves = abs(v_moves_count) * ['^' if v_moves_count > 0 else 'v']
    h_moves = abs(h_moves_count) * ['<' if h_moves_count > 0 else '>']
    SORT_ORDER = {'<': 0, '^': 1, 'v': 2, '>': 3}
    return sorted(v_moves + h_moves, key=lambda val: SORT_ORDER[val]) + ['A']


codes = open("input_test.txt").read().splitlines()

complexity = 0
for code in codes:
    print(f"Code: {code}")
    prev = 'A'
    moves = []
    for c in code:
        moves += numpad_moves(prev, c)
        prev = c
    print("".join(moves))

    prev = 'A'
    moves2 = []
    for c in moves:
        moves2 += dirpad_moves(prev, c)
        prev = c
    print("".join(moves2))

    prev = 'A'
    moves3 = []
    for c in moves2:
        moves3 += dirpad_moves(prev, c)
        prev = c
    print("".join(moves3))
    print(
        f"Code complexity: {len(moves3)} * {int(re.sub(r'\D', '', code))} = {len(moves3) * int(re.sub(r'\D', '', code))}")
    complexity += len(moves3) * int(re.sub(r'\D', '', code))

print(complexity)  # test 126384
int(re.sub(r'\D', '', "029A"))  # 215374
