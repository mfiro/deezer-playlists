import deezer
import os

from src.helpers import get_test_playlist
from src.archive import get_catalog, save_as_json, save_as_pretty_table


def main():
    current_dir = os.path.dirname(__file__)

    # get the catalog:
    catalog_path = os.path.join(current_dir, '../data/catalog/catalog.txt')
    catalog = get_catalog(catalog_path)

    # initiate the deezer client
    client = deezer.Client()

    # get playlist info:
    for id in catalog:
        
        ## Destination paths:
        # json files location: ../data/playlists/id.json
        json_path = os.path.join(current_dir, f"../data/playlists/{id}.json")

        # pretty md pages location: ../data/playlists_pretty/id.md 
        pretty_path = os.path.join(current_dir, f"../data/playlists_pretty/{id}.md")

        ## Get playlist
        print(f"Getting the playlist {id} ...")
        playlist = client.get_playlist(id)
        playlist = playlist.as_dict()

        # remove the share key from dict. It changes constantly and causes not useful diff 
        playlist.pop('share') 
        print(f"Playlist found! name: {playlist['title']}, {playlist['nb_tracks']} Tracks")

        ## Saving to destination
        save_as_json(playlist, json_path)
        save_as_pretty_table(playlist, pretty_path)       


def dummy_main():
    """ In order to prevent real api calls"""
    
    # get the catalog:
    catalog_path = os.path.join(os.path.dirname(__file__), '../data/catalog/catalog.txt')
    catalog = get_catalog(catalog_path)

    # get some dummy data to start with
    playlist = get_test_playlist(catalog)

    # save the template
    template_path = os.path.join(os.path.dirname(__file__), f'../data/playlists_pretty/table_template.md')
    save_as_pretty_table(playlist, template_path)  
       

if __name__ == "__main__":
    dummy_mode = False

    if dummy_mode:
        dummy_main()
    else:
        main()