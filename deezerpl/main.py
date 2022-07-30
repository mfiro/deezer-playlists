import os
import deezer

from deezerpl.archive import read_catalog, save_as_json, save_as_pretty_table
from deezerpl.helpers import get_test_playlist


def main():
    data_dir = './data'

    # get the catalog:
    catalog_path = os.path.join(data_dir, 'catalog/catalog.txt')
    playlist_ids = read_catalog(catalog_path)

    # initiate the deezer client
    client = deezer.Client()

    # get playlist info:
    for playlist_id in playlist_ids:

        # Destination paths:
        # json files location: ../data/playlists/id.json
        json_path = os.path.join(data_dir, f"playlists/{playlist_id}.json")

        # pretty md pages location: ../data/playlists_pretty/id.md
        pretty_path = os.path.join(data_dir,
                                   f"playlists_pretty/{playlist_id}.md")

        # Get playlist
        print(f"Getting the playlist {playlist_id} ...")
        playlist = client.get_playlist(playlist_id)
        playlist = playlist.as_dict()

        # share link changes constantly and doesn't have useful info
        playlist.pop('share')
        print(f"{playlist['title']}, {playlist['nb_tracks']} Tracks")

        # Saving to destination
        save_as_json(playlist, json_path)
        save_as_pretty_table(playlist, pretty_path)


def dummy_main():
    """In order to prevent real api calls"""
    # get the catalog:
    data_dir = './data/'
    catalog_path = os.path.join(data_dir, 'test/catalog.txt')
    playlist_ids = read_catalog(catalog_path)

    # get some dummy data to start with
    playlist = get_test_playlist(playlist_ids, data_dir)

    # save the template
    template_path = os.path.join(data_dir,
                                 'playlists_pretty/table_template.md')
    save_as_pretty_table(playlist, template_path)


if __name__ == "__main__":
    dummy_mode = False

    if dummy_mode:
        dummy_main()
    else:
        main()
