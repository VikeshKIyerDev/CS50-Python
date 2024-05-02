import project

def test_save_recipes():
    # Test saving recipes to a file
    recipes = [{'name': 'Test Recipe', 'ingredients': ['Ingredient1', 'Ingredient2'], 'instructions': 'Test instructions', 'notes': 'Test notes'}]
    project.save_recipes(recipes)
    loaded_recipes = project.load_recipes()
    assert recipes == loaded_recipes

def test_delete_recipe():
    # Test deleting a recipe
    # Assuming there's a recipe named 'Test Recipe' added previously
    project.delete_recipe('Test Recipe')
    loaded_recipes = project.load_recipes()
    assert len(loaded_recipes) == 0


def test_add_recipe():
    # Test adding a recipe
    # Assuming user inputs 'Test Recipe', 'Ingredient1, Ingredient2', 'Test instructions', 'Test notes'
    project.add_recipe({'name': 'Test Recipe', 'ingredients': ['Ingredient1, Ingredient2'], 'instructions': 'Test instructions', 'notes': 'Test notes'})
    loaded_recipes = project.load_recipes()
    assert (len(loaded_recipes) == 1) and (loaded_recipes[0]['name'] == 'Test Recipe')


def test_search_recipe():
    # Test case for searching recipes
    project.add_recipe({'name': "Spaghetti Bolognese", 'ingredients': ["spaghetti", "minced beef", "tomato sauce"], 'instructions': "Cook spaghetti, brown beef, add sauce.", 'notes': "Top with grated cheese."})
    project.add_recipe({'name': "Chocolate Cake", 'ingredients': ["flour", "sugar", "cocoa powder"], 'instructions': "Mix dry ingredients, add wet ingredients, bake.", 'notes': "Let cool before frosting."})
    found_recipes=project.search_recipe("spaghetti")
    assert len(found_recipes) > 0
    assert "Spaghetti Bolognese" in (found_recipes[i]['name'] for i in range(len(found_recipes)))
    assert "Chocolate Cake" not in (found_recipes[i]['name'] for i in range(len(found_recipes)))


if __name__ == '__main__':
    test_save_recipes()
    test_delete_recipe()
    test_add_recipe()
    test_search_recipe()