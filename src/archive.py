import os
import json
from pretty_playlist import make_pretty_md


def get_catalog():
    """ get the catalog (list of playlists to get) """
    catalog_path = os.path.join(os.path.dirname(__file__), '../data/catalog/catalog.txt')
    with open(catalog_path, 'r') as f:
        catalog = f.read().splitlines()
    return catalog


def save_as_json(playlist):
    print(f"Saving track list ...")
    save_path = os.path.join(os.path.dirname(__file__), f"../data/playlists/{playlist['id']}.json")
    with open(save_path,'w') as f:
        json.dump(playlist, f, indent=4)
    print(f"Tracks' information saved to {save_path}")


def save_as_pretty_table(playlist):

    current_dir = os.path.dirname(__file__)
    save_path = os.path.join(current_dir, f"../data/playlists_pretty/{playlist['id']}.md")

    # get page content
    page_content = make_pretty_md(playlist)

    # Write to the md file
    with open(save_path, 'w') as f:
        f.write(page_content)
    
    print(f"{save_path} updated")
