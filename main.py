from open_mods import open_mod_links
from get_dependencies import get_all_dependencies

mod_id = input("Enter Mod ID: ")  # Example: 3753 for Stardew Valley Expanded
all_dependencies = get_all_dependencies(mod_id)
print("All dependencies:", all_dependencies)
open_mod_links(all_dependencies)

