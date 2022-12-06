"""
source: https://adventofcode.com/2022/day/5
--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, 
but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, 
the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. 
Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. 
In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?




    [H]         [D]     [P]        
[W] [B]         [C] [Z] [D]        
[T] [J]     [T] [J] [D] [J]        
[H] [Z]     [H] [H] [W] [S]     [M]
[P] [F] [R] [P] [Z] [F] [W]     [F]
[J] [V] [T] [N] [F] [G] [Z] [S] [S]
[C] [R] [P] [S] [V] [M] [V] [D] [Z]
[F] [G] [H] [Z] [N] [P] [M] [N] [D]
 1   2   3   4   5   6   7   8   9 

"""

filePath = 'data.txt'
unitTestData = 'testData.txt'


f = open(filePath, 'r')
crates = []
#getting indices for crates
t1 = "[F] [G] [H] [Z] [N] [P] [M] [N] [D]"
cnt = 0
crateIndex = []
for l in t1:
   cnt += 1
   if l.isalpha() == True:
        crateIndex.append(cnt-1)
print(f'crate index = {crateIndex}')

movingInstructions = []

for line in f:
    if '[' in line:
        tempList = []
        whitspaceCount = 0
        for char in line:
           if whitspaceCount == 4 or whitspaceCount == 5:
                tempList.append('0')
                whitspaceCount = 0
           elif whitspaceCount == 9 or whitspaceCount == 8:
                tempList.append('0')
                tempList.append('0')
                whitspaceCount = 0
           else:
                if (line.index(char) in crateIndex) and (char.isalpha() == True):
                        tempList.append(char)
                        whitspaceCount = 0
                elif  char ==' ':
                        whitspaceCount += 1
        if len(tempList) == 8:
           tempList.append('0')
           whitspaceCount = 0
        crates.append(tempList)
    else:
        movingInstructions.append(line.strip())
print(f"crate = {crates}")
print(f"instruction = {movingInstructions}")


def parse_stack_text(stacktext):
    stacks = [""]*10
    for line in stacktext[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != " ": stacks[i+1] += box
    return stacks
    
input_data = open("data.txt").read()
stackt, instructions = [part.split("\n") for part in input_data.split("\n\n")]
stacks = parse_stack_text(stackt)

p1, p2 = stacks[:], stacks[:]
for line in instructions:
    _, n, _, src, _, dest = line.split()
    n = int(n); src = int(src); dest = int(dest)

    p1[src], p1[dest] = p1[src][n:],  p1[src][:n][::-1] + p1[dest]
    p2[src], p2[dest] = p2[src][n:],  p2[src][:n]       + p2[dest]

print("Part 1:", "".join(s[0] for s in p1 if s))
print("Part 2:", "".join(s[0] for s in p2 if s))