with open('input_1.txt', 'r') as input_1:
    input_1 = [line.replace(' ', '').strip() for line in input_1.readlines()]


marks = [int(mark[mark.find(',')+1:]) for mark in input_1]
avg = sum(marks) / len(marks)

with open('output_1.txt', 'w') as output_1:
    output = [output_1.write(line + '\n') for line in input_1 if int(line[line.find(',')+1:]) > avg]
    output_1.close()

print(input_1)
print(avg)