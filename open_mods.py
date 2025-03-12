import webbrowser

def open_mod_links(all_dependencies):
    """Opens a list of Nexus Mods pages in web browser."""
    base_url = "https://www.nexusmods.com/stardewvalley/mods/"
    
    for mod_id in all_dependencies:
        mod_url = base_url + str(mod_id)
        print(f"Opening: {mod_url}")
        webbrowser.open(mod_url)  

