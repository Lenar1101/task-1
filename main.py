def process_recipe(lines, index):
    name = lines[index]
    count = int(lines[index + 1])
    ingredients = []
    for i in range(index + 2, index + count + 2):
        _name, _quantity, _measure = lines[i].split(' | ')
        ingredients.append({
            'ingredient_name': _name,
            'quantity': int(_quantity),
            'measure': _measure,
        })
    return {name: ingredients}, index + count + 2

def read_receipts(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        lines[i] = line.rstrip('\n')
    receipts = {}
    index = 0
    while index <= len(lines):
        receipt, index = process_recipe(lines, index)
        index += 1
        receipts.update(receipt)
    return receipts

file_path = 'C:\\Users\\lenar\\AppData\\Roaming\\JetBrains\\PyCharmCE2022.2\\scratches\\scratch_1.txt'

receipts = read_receipts(file_path)
print(receipts)

# ======================================
# #2
# ======================================
def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        receipt = receipts[dish]
        for item in receipt:
            if item['ingredient_name'] in ingredients:
                ingredients[item['ingredient_name']]['quantity'] += item['quantity'] * person_count
            else:
                ingredients[item['ingredient_name']] = {
                    "measure": item['measure'],
                    "quantity": item['quantity'] * person_count,
                }
    return ingredients

