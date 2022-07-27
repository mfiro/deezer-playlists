from helpers import seconds2hms, create_url_markdown


def list2prettyrow(l):
    # convert everything to str
    l = [str(i) for i in l]
    pretty = ' | '.join(['', *l,''])
    pretty = pretty.strip() # delete both leading and trailing spaces
    pretty += '\n'
    return pretty 


def make_pretty_md(playlist: dict) -> str:
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
    