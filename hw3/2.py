with open('input.txt', 'r') as input_txt:
    sales_dict = dict(eval(input_txt.read()))

print(sales_dict)
new_dict = {}

for el1 in sales_dict.values():
    for el2 in dict(el1).items():
        if el2[0] not in new_dict:
            new_dict[el2[0]] = el2[1]
        else:
            new_dict[el2[0]] += el2[1]
print(new_dict)

with open('output.txt', 'w') as output_txt:
    for el in new_dict.items():
        output_txt.write(f'{el[0]}:{el[1]} \n')
    output_txt.close()