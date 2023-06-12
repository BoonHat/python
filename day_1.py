def elf_inventory (input_txt):
    for numb in elf:
        inventory = numb.split('\n')
        sum_kcal = sum(int(count) for count in inventory)
        list_for_kcal.append(sum_kcal)
    list_for_kcal.sort(reverse=True)
    return list_for_kcal

filename = "day_1.txt"

with open (filename,'r') as file:
    input_txt = file.read()

elf = input_txt.split('\n\n')
list_for_kcal = []

highest_kcal = elf_inventory(input_txt)
print(highest_kcal [0])
print(highest_kcal[:3])

top3_total_kcal = sum(int (count) for count in highest_kcal[:3])
print(top3_total_kcal)