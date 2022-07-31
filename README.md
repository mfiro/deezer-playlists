# Disclaimer
DEEZER is a registered trademark of Deezer. This project is not associated with Deezer in any way.


## deezer-playlists
A journal of Deezer's playlists to always have the history available. Updating Daily. Inspired by [spotify-playlist-archive](https://github.com/mackorone/spotify-playlist-archive) and [git-scraping](https://simonwillison.net/2020/Oct/9/git-scraping/).

### How this project works?
This project uses github actions to call deezer's API everyday to get new changes of desired playlists. List of playlists that are monitored are saved in [the catalog file](data/catalog/catalog.txt).

### In which format data is saved?
At the moment in two format:
1) **JSON** including all meta data received from Deezer's api. [Example](data/playlists/1111143121.json).
2) **Tables** using Github markdown (and a few lines html). This format is prettier but have less metadata for sure. [Example](data/playlists_pretty/table_template.md) 


### Can I also add my favorite playlists to this project? 
I would love to have your playlists. You only need to add your playlist's id to the catalog file [here](data/catalog/catalog.txt) and make a pull requests.

You can also find playlist's id from the url. Example:
deezer.com/us/playlist/**1913763402**
