
m = int(input())
products = []

for i in range(m):
    product = input()
    products.append(product)

n = int(input())

for i in range(n):
    recipe = input().split()
    name = recipe[0]
    ingredients = recipe[1:]

    can_cook = True

    for ingredient in ingredients:
        if ingredient not in products:
            can_cook = False

    if can_cook:
        print(name)
