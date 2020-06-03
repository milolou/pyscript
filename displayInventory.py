# inventoryOfPlayer = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    totalNum = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalNum = totalNum + v
    print('Total number of items: ' + ' ' + str(totalNum))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] = inventory[i] + 1
        else:
            inventory.setdefault(i, 1)
    return inventory
        
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
