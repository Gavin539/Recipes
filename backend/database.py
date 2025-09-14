import sqlite3

DB_NAME = "recipes.db"

# Initialize the database
def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create the recipes table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            content TEXT
        )
    """)
    
    conn.commit()
    conn.close()

# Insert a new recipe
def insert_recipe(name, content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO recipes (name, content) VALUES (?, ?)", (name, content))
        conn.commit()
        print(f"Recipe '{name}' added successfully!")
    except sqlite3.IntegrityError:
        print(f"Recipe for '{name}' already exists.")

    conn.close()

# Get a recipe by name
def get_recipe_by_name(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT content FROM recipes WHERE name = ?", (name,))
    recipe = cursor.fetchone()
    
    conn.close()
    return recipe[0] if recipe else None

# Get all recipes
def get_all_recipes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, content FROM recipes")
    recipes = cursor.fetchall()
    
    conn.close()
    return recipes

# Update an existing recipe
def update_recipe(name, new_content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("UPDATE recipes SET content = ? WHERE name = ?", (new_content, name))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"Recipe '{name}' updated successfully!")
    else:
        print(f"Recipe '{name}' not found.")

    conn.close()

# Delete a recipe
def delete_recipe(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM recipes WHERE name = ?", (name,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"Recipe '{name}' deleted successfully!")
    else:
        print(f"Recipe '{name}' not found.")

    conn.close()

# Search recipes by keyword
def search_recipes(keyword):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, content FROM recipes WHERE name LIKE ? OR content LIKE ?", 
                   (f"%{keyword}%", f"%{keyword}%"))
    recipes = cursor.fetchall()
    
    conn.close()
    return recipes

# Count the number of recipes in the database
def count_recipes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM recipes")
    count = cursor.fetchone()[0]
    
    conn.close()
    return count

# Get a random recipe
def get_random_recipe():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, content FROM recipes ORDER BY RANDOM() LIMIT 1")
    recipe = cursor.fetchone()
    
    conn.close()
    return recipe if recipe else None

# Initialize DB when the script runs
initialize_db()

# Example usage
if __name__ == "__main__":
    print(f"Total recipes in database: {count_recipes()}")
    insert_recipe("Pancakes", "Flour, eggs, milk, sugar, baking powder")
    insert_recipe("Omelette", "Eggs, cheese, salt, pepper")
    print("All Recipes:", get_all_recipes())
    print("Searching for 'egg':", search_recipes("egg"))
    update_recipe("Pancakes", "Flour, eggs, milk, sugar, baking powder, vanilla extract")
    delete_recipe("Omelette")
    print("Random Recipe:", get_random_recipe())
