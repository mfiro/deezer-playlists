import deezer
import json
import os

from helpers import get_dummy_tracks, list2prettyrow, seconds2hms
# TODO: Add pretty tables


def get_catalog():
    """ get the catalog (list of playlists to get) """
    catalog_path = os.path.join(os.path.dirname(__file__), '../data/catalog/catalog.txt')
    with open(catalog_path, 'r') as f:
        catalog = f.read().splitlines()
    return catalog


def get_tracks_dict(playlist):
    return playlist.as_dict()['tracks']


def save_as_json(id, tracks):
    print(f"Saving track list ...")
    save_path = os.path.join(os.path.dirname(__file__), f'../data/playlists/{id}.json')
    with open(save_path,'w') as f:
        json.dump(tracks, f, indent=4)
    print(f"Tracks' information saved to {save_path}")


def get_pretty_content(playlist_title: str, tracks: dict) -> str:
    #### Create page content
    # Header (before table)
    page_content = f"Playlist title : {playlist_title} \n\n"

    # table content
    column_names = ['No.', 'Song', 'Artist', 'Album', 'Time']

    page_content += list2prettyrow(column_names)
    page_content += list2prettyrow(['---']*len(column_names))

    for idx, track in enumerate(tracks, 1):
        page_content += list2prettyrow([idx,
            track['title'],
            track['artist']['name'],
            track['album']['title'],
            seconds2hms(track['duration'])],)
    return page_content


def save_as_pretty_table(playlist, tracks):

    current_dir = os.path.dirname(__file__)
    save_path = os.path.join(current_dir, f'../data/playlists_pretty/{playlist.id}.md')

    # get page content
    page_content = get_pretty_content(playlist.title, tracks)

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
        print(f"Playlist found! name: {playlist.title}, {playlist.nb_tracks} Tracks")

        # get tracks' information, artist, titles ...
        print(f"Getting tracks' information in raw json/dict format ...")
        tracks = get_tracks_dict(playlist)

        # saving to json file. Dest: ../data/playlists/id.json
        save_as_json(id, tracks)

        # saving as a pretty table. ../data/playlists_pretty/id.md
        save_as_pretty_table(playlist, tracks)       


def dummy_main():
    """ In order to prevent real api calls"""
    
    # get the catalog:
    catalog = get_catalog()

    # get some dummy data to start with
    tracks = get_dummy_tracks(catalog)

    # get pretty content
    page_content = get_pretty_content('Top Germany', tracks)

    template_path = os.path.join(os.path.dirname(__file__), f'../data/playlists_pretty/table_template.md')

    with open(template_path, 'w') as f:
        f.write(page_content)
    
    print(f"{template_path} updated")
       

if __name__ == "__main__":
    dummy_mode = True

    if dummy_mode:
        dummy_main()
    else:
        main()