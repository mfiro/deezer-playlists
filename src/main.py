import deezer
import json
import os

from helpers import get_test_playlist, list2prettyrow, seconds2hms, create_url_markdown


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


def get_pretty_content(playlist: dict) -> str:
    #### Create page content
    ## ---------- Playlist information ------------
    page_content = "## Playlist Information \n"

    # create a vertical table
    page_content += "<table>" # beginning of table html
    page_content += f"<tr><th align ='left'>Title</th><td align ='left'>{playlist['title']}</td></tr>"
    page_content += f"<tr><th align ='left'>Description</th><td align ='left'>{playlist['description']}</td></tr>"
    page_content += f"<tr><th align ='left'>No. Tracks</th><td align ='left'>{playlist['nb_tracks']}</td></tr>"
    page_content += f"<tr><th align ='left'>Duration</th><td align ='left'>{seconds2hms(playlist['duration'])}</td></tr>"
    page_content += f"<tr><th align ='left'>No. Fans</th><td align ='left'>{playlist['fans']}</td></tr>"
    page_content += f"<tr><th align ='left'>Link</th><td align ='left'>{playlist['link']}</td></tr>"
    page_content += "</table>" # end of html table
    page_content += "\n\n"
    #page_content += f"Playlist title : {playlist['title']} \n\n"

    # ----------- Tracklist -----------------------
    page_content += "## Tracklist \n"
    column_names = ['No.', 'Song', 'Artist', 'Album', 'Time']

    page_content += list2prettyrow(column_names)
    page_content += list2prettyrow(['---']*len(column_names))

    for idx, track in enumerate(playlist['tracks'], 1):
        page_content += list2prettyrow(
            [
            idx,
            create_url_markdown(track['link'], track['title']),
            create_url_markdown(track['artist']['link'], track['artist']['name']),
            track['album']['title'],
            seconds2hms(track['duration'])
            ],)
    return page_content


def save_as_pretty_table(playlist):

    current_dir = os.path.dirname(__file__)
    save_path = os.path.join(current_dir, f"../data/playlists_pretty/{playlist['id']}.md")

    # get page content
    page_content = get_pretty_content(playlist)

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
    page_content = get_pretty_content(playlist)

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