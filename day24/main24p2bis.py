import re
from collections import Counter

inputs_part, logic_part = open("input.txt").read().split("\n\n")

inputs = {}
for l in inputs_part.splitlines():
    i, val = l.split(": ")
    inputs[i] = int(val)

logic = ([tuple(re.findall("AND|OR|XOR|[a-z0-9]+", l)) for l in logic_part.splitlines()])


def calc_wire_val(wire_id):
    ans = {k: v for k, v in inputs.items() if k.startswith(wire_id)}
    ans = dict(reversed(sorted(ans.items())))
    if not ans: return None
    return int("".join(str(x) for x in ans.values()), 2)


expected_z = calc_wire_val("x") + calc_wire_val("y")

print(f"Expected Z: {expected_z}")  # 60439554459366

deps = {}
formulas = {}
for l in logic:
    a, op, b, res = l
    deps.setdefault(a, []).append(res)
    deps.setdefault(b, []).append(res)
    formulas[res] = (a, op, b)


def depth_deps(elem):
    elems = [elem]
    if not elem in formulas: return [elem]
    a, op, b = formulas[elem]
    elems.extend(["="])
    elems.extend([op])
    elems.extend(["("])
    elems.extend(depth_deps(a))
    elems.extend(depth_deps(b))
    elems.extend([")"])
    return elems

def calc_formulas_and_ops_count():
    ops_count = {}
    full_formulas = {}
    for fk in formulas.keys():
        depth = depth_deps(fk)
        op_count = Counter([op for op in depth if op in ["AND", "OR", "XOR"]])
        ops_count[fk] = op_count
        full_formulas[fk] = depth
    return ops_count, full_formulas

ops_count, full_formulas = calc_formulas_and_ops_count()

swaps = []
wrong_z = set()
middles = set()
for i in range(0, 45 + 1):
    i_with_pad = str(i).rjust(2, '0')
    z = 'z' + i_with_pad
    x = 'x' + i_with_pad
    y = 'y' + i_with_pad

    depth = depth_deps(z)

    op_count = Counter([op for op in depth if op in ["AND", "OR", "XOR"]])
    print(f"z: {z} has {op_count}")
    if i > 3:
        exp_AND = 2 * i - 1
        exp_OR = i - 1
        exp_XOR = i + 1
        print(f"z: {z} should have {exp_AND} ANDs and {exp_OR} ORs and {exp_XOR} XORs")
        if op_count["AND"] != exp_AND or op_count["OR"] != exp_OR or op_count["XOR"] != exp_XOR:
            print(f" ... but it has {op_count["AND"]} ANDs and {op_count["OR"]} ORs and {op_count["XOR"]} XORs")
            the_corrects = [k for k, c in ops_count.items()
                           if c["AND"] == exp_AND and c["OR"] == exp_OR or c["XOR"] == exp_XOR]


            print(f"Options are: {the_corrects}")

            print(f"It should contain {middles}")
            the_correct = [c for c in the_corrects
                           if middles < set(full_formulas[c])
                           and formulas[c][1] == "XOR" and not c.startswith("z")][0]
            print(f"Should swap {the_correct} with {z}? Let's find out!")
            formulas[z], formulas[the_correct] = formulas[the_correct], formulas[z]
            swaps += [the_correct, z]
            wrong_z.add(z)

            ops_count, full_formulas = calc_formulas_and_ops_count()

    middles = middles.union(set(depth_deps(z)) - set([z]))


print(swaps)

# manually checked data :-(
swaps.append("pmd")
swaps.append("cgh")

print(",".join(sorted(swaps))) #cgh,frt,pmd,sps,tst,z05,z11,z23

for k,f in sorted(full_formulas.items()):
    if not k.startswith("z"): continue
    print(k, "-->", f)



def calc_topological_order(deps):
    to = []

    def find_to(el):
        if el in to: return
        for dep in deps.get(el, []):
            find_to(dep)
        to.insert(0, el)

    for el in deps:
        find_to(el)
    return to


def calculate_z(formulas, to):
    print(f"formulas: {formulas}, to: {to}")
    values = inputs.copy()
    for res in to:
        if res in values: continue
        a, op, b = formulas[res]
        if not a in values or not b in values: return None  # easy way to check loops
        a_val = values[a]
        b_val = values[b]
        val = a_val and b_val if op == "AND" else a_val or b_val if op == "OR" else a_val ^ b_val
        values[res] = val
    return calc_wire_val("z")


def has_cycle(deps):
    visited = set()
    stack = []

    def cycle_detection(node):
        if node in stack: return True
        if node in visited: return False

        visited.add(node)
        stack.append(node)

        for neighbor in deps.get(node, []):
            if cycle_detection(neighbor):
                return True
        stack.pop()
        return False

    for vertex in deps:
        if vertex not in visited:
            if cycle_detection(vertex):
                return True

    return False


def find_swaps(formulas, deps, swaps):
    print(f"formulas: {formulas}")
    to = calc_topological_order(deps)
    print(f"to: {to}, swaps: {swaps}")
    if calculate_z(formulas, to) == expected_z: return swaps
    if len(swaps) == 8: return None

    if len(swaps) < 8:
        for a in to:
            if not a in formulas: continue
            for b in to:
                if a == b: continue
                if not b in formulas: continue
                print(f"swapping {a} and {b}")
                new_swaps = swaps + [a, b]

                new_deps = deps.copy()
                new_deps[a], new_deps[b] = new_deps.get(b, []), new_deps.get(a, [])

                new_formulas = formulas.copy()
                new_formulas[a], new_formulas[b] = new_formulas[b], new_formulas[a]

                if has_cycle(new_deps): continue

                print(f"new formulas: {new_formulas}, new to: {new_deps}, new swaps: {new_swaps}")
                if find_swaps(new_formulas, new_deps, new_swaps) == expected_z: return swaps


swaps = find_swaps(formulas, deps, [])
print(",".join(sorted(swaps)))
