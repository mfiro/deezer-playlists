import deezer
import os

from src.helpers import get_test_playlist
from src.archive import read_catalog, save_as_json, save_as_pretty_table

# TODO: rename get_catalog to read_catalog

def main():
    data_dir = './data'

    # get the catalog:
    catalog_path = os.path.join(data_dir, 'catalog/catalog.txt')
    playlist_ids = read_catalog(catalog_path)

    # initiate the deezer client
    client = deezer.Client()

    # get playlist info:
    for id in playlist_ids:
        
        ## Destination paths:
        # json files location: ../data/playlists/id.json
        json_path = os.path.join(data_dir, f"playlists/{id}.json")

        # pretty md pages location: ../data/playlists_pretty/id.md 
        pretty_path = os.path.join(data_dir, f"playlists_pretty/{id}.md")

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
    data_dir = './data/'
    catalog_path = os.path.join(data_dir, 'test/catalog.txt')
    playlist_ids = read_catalog(catalog_path)

    # get some dummy data to start with
    playlist = get_test_playlist(playlist_ids, data_dir)

    # save the template
    template_path = os.path.join(data_dir, f'playlists_pretty/table_template.md')
    save_as_pretty_table(playlist, template_path)  
       

if __name__ == "__main__":
    dummy_mode = True

    if dummy_mode:
        dummy_main()
    else:
        main()