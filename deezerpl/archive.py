import json
from deezerpl.pretty_playlist import make_pretty_md


def read_catalog(catalog_path):
    """ get the catalog (list of playlists to get) """
    with open(catalog_path, 'r') as f:
        playlist_ids = f.read().splitlines()
    return playlist_ids


def save_as_json(playlist, save_path):
    print("Saving track list ...")
    with open(save_path, 'w') as f:
        json.dump(playlist, f, indent=4)
    print(f"Tracks' information saved to {save_path}")


def save_as_pretty_table(playlist, save_path):
    # get page content
    page_content = make_pretty_md(playlist)

    # Write to the md file
    with open(save_path, 'w') as f:
        f.write(page_content)

    print(f"{save_path} updated")
