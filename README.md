# download-map-tiles

A template repository for downloading map tiles.

Requires Python.

## Instructions

Configure `get_tiles.py` with the tile values you'd like to download from the server.

Make sure to update the URL in `generate_image_url()` for where you'd like to download the tiles from.

N.B. Check the license & permitted usage before downloading tiles. This script downloads roughly 3 tiles a second so typically avoids most API request limits.

Create a new virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

Install the project dependency

```bash
pip install requests
```

Run the script

```bash
python get_tiles.py
```

If the script crashes, see what tile number it crashed on. Add an if statement to skip downloading tiles less than that number when you run the script again.
