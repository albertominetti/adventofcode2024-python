import re

inputs_part, logic_part = open("input.txt").read().split("\n\n")

inputs = {}
for l in inputs_part.splitlines():
    i, val = l.split(": ")
    inputs[i] = int(val)

logic = ([tuple(re.findall("AND|OR|XOR|[a-z0-9]+", l)) for l in logic_part.splitlines()])

deps = {}
formulas = {}
for l in logic:
    a, op, b, res = l
    deps.setdefault(a, []).append(res)
    deps.setdefault(b, []).append(res)
    formulas[res] = (a, op, b)

to = []
def find_to(el):
    if el in to: return
    for dep in deps.get(el, []):
        find_to(dep)
    to.insert(0, el)


for el in deps:
    find_to(el)

print(f"Topological order: {to}")

for res in to:
    if res in inputs: continue
    a, op, b = formulas[res]
    a_val = inputs[a]
    b_val = inputs[b]
    val = a_val and b_val if op == "AND" else a_val or b_val if op == "OR" else a_val ^ b_val
    inputs[res] = val

print(inputs)
ans = {k: v for k, v in inputs.items() if k.startswith("z")}
ans = dict(reversed(sorted(ans.items())))

print(int("".join(str(x) for x in ans.values()), 2)) # 60714423975686