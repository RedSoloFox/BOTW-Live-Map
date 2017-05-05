#!/usr/bin/env bash
# I am using Windows 10 Bash for this
echo "Starting Tile Generation"
python2 gdal2tiles-multiprocess.py -l -p raster -z 0-5 -w none "BotW-Map-FULL.png" "../webserver/static/img/tiles/"
echo "Tiles Created"