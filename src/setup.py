from context_menu import menus
import modules

ch=int(input("Press 1 to install and 2 to uninstall\n"))
if ch == 1:
    cm = menus.ContextMenu("Easyry", type="FILES")
    cm.add_items([
                menus.ContextCommand("📁 Move To Folder", python=modules.moveToFolder),
                menus.ContextCommand("📄 Copy Path To Clipboard", python=modules.copyPath),
                menus.ContextCommand("📄 Copy Name To Clipboard", python=modules.copyName)
            ])
    cm.compile()
    print("Easyry Installed!")

elif ch == 2:
    menus.removeMenu("Easyry", "FILES")
    print("Easyry Uninstalled!")
