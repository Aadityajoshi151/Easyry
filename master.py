from context_menu import menus
import modules

ch=int(input("Press 1 to add and 2 to remove"))
if ch == 1:
    cm = menus.ContextMenu('Easyry', type='FILES')
    cm2 = menus.ContextMenu('Some Function')
    cm.add_items([
                cm2,
                menus.ContextCommand('Func1', python=modules.func1)
            ])
    cm.compile()
    print("Menu Added")

elif ch == 2:
    menus.removeMenu('Easyry', 'FILES')
    print("Menu Removed")
