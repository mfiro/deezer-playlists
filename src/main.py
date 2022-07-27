import deezer
import json
import os

from helpers import get_test_playlist
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


def main():
    # get the catalog:
    catalog = get_catalog()

    # initated the deezer client
    client = deezer.Client()

    # get playlist tracks and artists:
    for id in catalog:

        # get playlist
        print(f"Getting the playlist {id} ...")
        playlist = client.get_playlist(id)
        playlist = playlist.as_dict()

        # remove the share key from dict. It changes constantly and causes not useful diff 
        playlist.pop('share') 
        print(f"Playlist found! name: {playlist['title']}, {playlist['nb_tracks']} Tracks")

        # saving to playlist as json file. Dest: ../data/playlists/id.json
        save_as_json(playlist)

        # saving as a pretty table. ../data/playlists_pretty/id.md
        save_as_pretty_table(playlist)       


def dummy_main():
    """ In order to prevent real api calls"""
    
    # get the catalog:
    catalog = get_catalog()

    # get some dummy data to start with
    playlist = get_test_playlist(catalog)

    # get pretty content
    page_content = make_pretty_md(playlist)

    template_path = os.path.join(os.path.dirname(__file__), f'../data/playlists_pretty/table_template.md')

    with open(template_path, 'w') as f:
        f.write(page_content)
    
    print(f"{template_path} updated")
       

if __name__ == "__main__":
    dummy_mode = False

    if dummy_mode:
        dummy_main()
    else:
        main()