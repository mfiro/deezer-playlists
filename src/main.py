import deezer
import json
import os

def get_catalog():
    """ get the catalog (list of playlists to get) """
    catalog_path = os.path.join(os.path.dirname(__file__), '../data/catalog/catalog.txt')
    with open(catalog_path, 'r') as f:
        catalog = f.read().splitlines()
    return catalog


def get_tracks_dict(playlist):
    return playlist.as_dict()['tracks']


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
        print(f"Playlist found! name: {playlist.title}, {playlist.nb_tracks} Tracks")

        # get tracks' information, artist, titles ...
        print(f"Getting tracks' information in raw json/dict format ...")
        tracks = get_tracks_dict(playlist)

        # saving to json file
        print(f"Saving track list ...")
        save_path = os.path.join(os.path.dirname(__file__), f'../data/playlists/{id}.json')
        with open(save_path,'w') as f:
            json.dump(tracks, f, indent=4)
        print(f"Tracks' information saved to {save_path}")


if __name__ == "__main__":
    main()