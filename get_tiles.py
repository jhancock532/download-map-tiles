import os
import requests
import shutil

##########################################
# Requires configuration before running! #
##########################################

minZoom = 1
maxZoom = 3

minZoomMinX = 0
minZoomMaxX = 2
minZoomMinY = 0
minZoomMaxY = 2

tile_folder_name = "tiles"

def generate_image_url(zoom_level, x_tile_number, y_tile_number):
    # Change the tile server URL here
    image_url = "https://osm-demo-a.wheregroup.com/tiles/1.0.0/osm/webmercator/" + str(zoom_level) + "/" + str(x_tile_number) + "/" + str(y_tile_number) + ".png"
    return image_url

##########################################
#   The following code is usable as is   #
##########################################

def download_image(image_url, file_path):
    """Downloads an image from the given URL and saves it to the specified file path."""

    response = requests.get(image_url, stream=True)

    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            response.raw.decode_content = True # Handle compressed images
            shutil.copyfileobj(response.raw, f)
    else:
        print("Failed to download image. Status code:", response.status_code)

def create_folder(folder_path):
    """Creates a folder at the specified path if it doesn't already exist."""

    try:
        os.mkdir(folder_path)
    except FileExistsError:
        print(f"Folder {folder_path} already exists.")

def calculate_total_tiles():
    """Calculates the total number of tiles to download."""

    total = 0
    for zoom_level in range(minZoom, maxZoom):
        multiplier = 2 ** (zoom_level - minZoom)
        min_x_tile = minZoomMinX * multiplier
        max_x_tile = minZoomMaxX * multiplier
        min_y_tile = minZoomMinY * multiplier
        max_y_tile = minZoomMaxY * multiplier
        total += (max_x_tile - min_x_tile) * (max_y_tile - min_y_tile)
    return total


num_total_tiles = calculate_total_tiles()

print("Total tiles to download:", num_total_tiles)

downloaded_tiles = 0

create_folder(tile_folder_name)

for zoom_level in range(minZoom, maxZoom):
    zoom_folder = tile_folder_name + "/" + str(zoom_level)

    create_folder(zoom_folder)

    multiplier = 2 ** (zoom_level - minZoom)

    min_x_tile = minZoomMinX * multiplier
    max_x_tile = minZoomMaxX * multiplier
    min_y_tile = minZoomMinY * multiplier
    max_y_tile = minZoomMaxY * multiplier

    print(min_x_tile, max_x_tile, min_y_tile, max_y_tile)

    for x_tile_number in range(min_x_tile, max_x_tile):
        x_folder = zoom_folder + "/" + str(x_tile_number)

        create_folder(x_folder)

        for y_tile_number in range(min_y_tile, max_y_tile):
            y_folder = x_folder + "/" + str(y_tile_number)

            file_path = y_folder + ".png"
            image_url = generate_image_url(zoom_level, x_tile_number, y_tile_number)

            download_image(image_url, file_path)
            downloaded_tiles += 1
            print("Downloaded tile ", str(downloaded_tiles), " of ", str(num_total_tiles))

  