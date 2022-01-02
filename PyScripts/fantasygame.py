def addToInventory(inventory, addedItems):
    # your code goes here
	for i in range(len(inventory)): #Count the number of indexes
		inventory.setdefault(addedItems[i], 0) #If item not in dictionary, default it to a 0 amount
		inventory[addedItems[i]]=inventory[addedItems[i]]+1 #Add each iteration to dictionary count
	return inventory

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += inventory[k]
    print("Total number of items: " + str(item_total))

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv) #Runs function within a function