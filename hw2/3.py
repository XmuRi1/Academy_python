with open('input1_3.txt', 'r') as input1:
    input1 = [line.strip() for line in input1.readlines()]

with open('input2_3.txt', 'r') as input2:
    input2 = [line.strip() for line in input2.readlines()]

input3 = input1 + input2
with open('output_3.txt', 'w') as output_1:
    output = [output_1.write(line + '\n') for line in sorted(input3)]

print(sorted(input3))