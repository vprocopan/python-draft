# Demonstrate and distinguish Python data structures:
# list, tuple, set, and dict

def demo_data_structures():
    print("=== 1️⃣ LIST ===")
    # A list is ordered, mutable, and allows duplicates
    fruits = ["apple", "banana", "cherry", "apple"]
    print("Original list:", fruits)
    fruits.append("orange")
    fruits[1] = "kiwi"
    print("Modified list:", fruits)
    print("Access element [2]:", fruits[2])
    print("Count of 'apple':", fruits.count("apple"))
    print("Type:", type(fruits), "\n")

    print("=== 2️⃣ TUPLE ===")
    # A tuple is ordered, immutable, and allows duplicates
    colors = ("red", "green", "blue", "green")
    print("Tuple:", colors)
    print("Access element [1]:", colors[1])
    # colors[1] = "yellow"  # ❌ This would cause an error (immutable)
    print("Count of 'green':", colors.count("green"))
    print("Type:", type(colors), "\n")

    print("=== 3️⃣ SET ===")
    # A set is unordered, mutable, and contains unique elements
    numbers = {1, 2, 3, 3, 4}
    print("Original set (duplicates removed):", numbers)
    numbers.add(5)
    numbers.discard(2)
    print("Modified set:", numbers)
    print("Check if 3 in set:", 3 in numbers)
    print("Type:", type(numbers), "\n")

    print("=== 4️⃣ DICTIONARY ===")
    # A dictionary stores key-value pairs
    person = {"name": "Vitalie", "role": "DevOps", "country": "Moldova"}
    print("Dictionary:", person)
    person["role"] = "SRE"
    person["email"] = "vprocopan@example.com"
    print("Modified dictionary:", person)
    print("Keys:", list(person.keys()))
    print("Values:", list(person.values()))
    print("Access by key ['name']:", person["name"])
    print("Type:", type(person), "\n")

if __name__ == "__main__":
    demo_data_structures()