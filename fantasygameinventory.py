#Fantasy Game Inventory
#Display:
#Inventory:
             #12 arrow
             #42 gold coin
             #1 rope
             #6 torch
             #1 dagger
             #Total number of items: 62

#inventory.py


stuff = {'rope': 1, 'torch': 6,'gold coin': 42,'dagger':1,'arrow':12}

def displayInventory(inventory):
    print('Inventory:')
    total_items = 0
    for k, v in inventory.items():
        print(str(v) +' '+ k)
        total_items = total_items + v
    print('Total number of items:' + str(total_items))

displayInventory(stuff)



#addinventory.py




def addToInventory(inventory, addedItems):
    # your code goes here
    for i in range(len(addedItems)):        #dumps list to dictionary
        inventory.setdefault(addedItems[i], 0)   #adds new keys to inv(default to zero)
        inventory[addedItems[i]] = inventory[addedItems[i]] + 1 #adds to totals value by on, if it appears in dragon loot
    return inventory
   

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
