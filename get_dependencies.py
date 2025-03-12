import requests
from bs4 import BeautifulSoup

def get_mod_dependencies(mod_id):
    """Scrapes Nexus Mods webpage to get dependencies for a given mod ID."""
    url = f"https://www.nexusmods.com/stardewvalley/mods/{mod_id}"

    # Set headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # get entire html content
        soup = BeautifulSoup(response.text, "html.parser")

        # filter down to dependencies/requirements table
        dependencies_table = None
        for table in soup.find_all("table"):
            if "Mod name" in table.get_text():
                dependencies_table = table
                break

        # Extract dependency mod IDs
        dependency_ids = []
        if dependencies_table:
            for row in dependencies_table.find_all("tr"):
                cols = row.find_all("td")
                if len(cols) >= 2:  # Ensure it's a valid row
                    mod_link_tag = cols[0].find("a", href=True)
                    mod_link = mod_link_tag["href"] if mod_link_tag else ""

                    # Extract mod ID from the URL
                    if "/stardewvalley/mods/" in mod_link:
                        mod_id_new = mod_link.split("/")[-1]  # Get last part of the URL (mod ID)
                        if mod_id_new.isdigit():  # Ensure valid ID
                            dependency_ids.append(mod_id_new)

        return dependency_ids  # Only return the mod IDs
    
    else:
        print("Error fetching mod webpage:", response.status_code)
        return []



def get_all_dependencies(mod_id):
    """Recursively get all dependencies for a given mod ID."""
    to_check = [mod_id]  # List of mod IDs to check
    c = 0
    while c < len(to_check):
        dependencies = get_mod_dependencies(to_check[c])
        for mod_id in dependencies:
            if mod_id not in to_check and mod_id != '2400':  # Exclude SMAPI
                to_check.append(mod_id)
        c += 1

    return to_check








