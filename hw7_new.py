cook_book = {}
with open('recipes.txt', encoding='utf-8') as file_work:
    food_list = [line.strip() for line in file_work]
    #print(lst)
    for string_number, string_content in enumerate(food_list): #The enumerate() method adds counter to an iterable and returns it (the enumerate object).
        #print(string_number)
        if string_content.isdigit(): #The isdigit() method returns True if all characters in a string are digits. If not, it returns False.
            cook_book[food_list[string_number - 1]] = []
            #print(cook_book)
            for ingredients in food_list[string_number + 1:string_number + int(string_content) + 1]:
                #print(ingredients)
                ingredient_name = ingredients.split('|')[0]
                quantity = int(ingredients.split('|')[1])
                measure = ingredients.split('|')[2]
                cook_book[food_list[string_number - 1]].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
print(cook_book)

