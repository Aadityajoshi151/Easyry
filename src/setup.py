from context_menu import menus
import modules

print("Press 1 to install Easyry")
print("Press 2 to uninstall Easyry")
ch=int(input())
if ch == 1:
    cm = menus.ContextMenu("Easyry", type="FILES")
    cm.add_items([
                menus.ContextCommand("📁 Move To Folder", python=modules.moveToFolder),
                menus.ContextCommand("📄 Copy Path To Clipboard", python=modules.copyPath),
                menus.ContextCommand("📄 Copy Name To Clipboard", python=modules.copyName),
                menus.ContextCommand("📛 Rename With Random String", python=modules.renameRandom),
                menus.ContextCommand("⏰ Rename With Timestamp",python=modules.renameTimestamp),
                menus.ContextCommand("⏰ Append Timestamp", python=modules.appendTimestamp),
                menus.ContextCommand("☠️ Corrupt File (Dangerous)", python=modules.corruptFile),
                menus.ContextCommand("🗐 Duplicate File", python=modules.duplicateFile)
            ])
    cm.compile()
    print("Easyry Installed!")

elif ch == 2:
    menus.removeMenu("Easyry", "FILES")
    print("Easyry Uninstalled!")
else:
    print("Wrong choice")
