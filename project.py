import json

def load_recipes():
    global recipes
    try:
        with open('recipes.json', 'r') as file:
            recipes = json.load(file)
    except FileNotFoundError:
        recipes = []
    return recipes

def save_recipes(recipes):
    with open('recipes.json', 'w') as file:
        json.dump(recipes, file, indent=4)

def add_recipe(recipe):
    recipes.append(recipe)
    save_recipes(recipes)
    print("Recipe added successfully!")

def view_recipes():
    recipes = load_recipes()
    if recipes:
        for i, recipe in enumerate(recipes, 1):
            print(f"{i}. {recipe['name']}")
            print("   Ingredients:", ', '.join(recipe['ingredients']))
            print("   Instructions:", recipe['instructions'])
            print("   Notes:", recipe['notes'])
    else:
        print("No recipes found.")

def search_recipe(query: str):
    recipes = load_recipes()
    found_recipes = []
    for recipe in recipes:
        if query.lower() in recipe['name'].lower() or query.lower() in [ing.lower() for ing in recipe['ingredients']]:
            found_recipes.append(recipe)
    if found_recipes:
        for i, recipe in enumerate(found_recipes, 1):
            print(f"{i}. {recipe['name']}")
            print("   Ingredients:", ', '.join(recipe['ingredients']))
            print("   Instructions:", recipe['instructions'])
            print("   Notes:", recipe['notes'])
    else:
        print("No matching recipes found.")
    return found_recipes

def delete_recipe(name):
    recipes = load_recipes()
    for i, recipe in enumerate(recipes):
        if recipe['name'].lower() == name.lower():
            del recipes[i]
            save_recipes(recipes)
            print("Recipe deleted successfully!")
            return
    print("Recipe not found.")

def main():
    print("Welcome to Recipe Organizer!")
    while True:
        print("\n1. Add Recipe\n2. View Recipes\n3. Search Recipe\n4. Delete Recipe\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            recipes = load_recipes()
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = input("Enter cooking instructions: ")
            notes = input("Enter any additional notes: ")
            recipe = {'name': name, 'ingredients': ingredients, 'instructions': instructions, 'notes': notes}
            add_recipe(recipe)
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            query = input("Enter recipe name or ingredient to search: ")
            search_recipe(query)
        elif choice == '4':
            name = input("Enter the name of the recipe to delete: ")
            delete_recipe(name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()