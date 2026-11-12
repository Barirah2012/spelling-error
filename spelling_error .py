MENU = [
    "pizza", "pasta", "burger", "fries", "tacos",
    "sushi", "ramen", "biryani", "paneer tikka",
    "butter chicken", "masala dosa", "idli",
    "samosa", "pav bhaji", "momos", "noodles",
    "fried rice", "sandwich", "salad", "pancakes",
    "waffles", "brownie", "cake", "coke", "coffee",
    "tea", "mango lassi", "ice cream", "milkshake",
    "nachos","nuts","freanch fries","fries","nuggets","chikken tikkah","drump sticks"
    ]
def edit_distance(word1,word2):
    count = abs(len(word1) - len(word2))
    for i in range (min(len(word1),len(word2))):
        if word1[i] != word2[i]:
                count+=1
        return count
    
def suggest(query):
    best_food=""
    smallest_distance =len(query) +100
    #smallest_distance = 999 means we are setting the starting smallest distance to a very large number.
    # We want to find the food name with the smallest spelling difference.
    for food in MENU:
        distance = edit_distance(query,food)
        if distance<smallest_distance:
            smallest_distance=distance
            best_food = food
            if smallest_distance<=max(1,len(query)//4):
                return best_food


# Main program
print("===== DID YOU MEAN? FOOD SEARCH =====")
while True:
    query = input("\n Enter food name OR type quit to stop : ").lower().strip()
    if query == "quit":
        print("Thank you!")
        break
    if query in MENU:
        print("showing result for:",query)
    else:
        result = suggest(query)
        if result:
            print("did u mean:",result)
        else:
            print("no dishes found!!!!!")

