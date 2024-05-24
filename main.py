from scraper.app import App
from consolemenu import *
from consolemenu.items import *

def run():
    try:
        app = App()
        
        menu = ConsoleMenu("YokAtlas Web Scraper", "This is a scraper for bachelor's degree programs in Turkey.")
        menu.append_item(FunctionItem("Bachelor's Degree Programs", app.get_bachelor_programs, should_exit=True))
        menu.show()
    except KeyboardInterrupt:
        print()
        print("🔨 Aborted: User Interrupt.")

if __name__ == "__main__":
    run()