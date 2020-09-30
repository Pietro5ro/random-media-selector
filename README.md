# random-media-selector
A Python script to select a random media file, open it with a selected player, and make sure the same file isn't selected later again.

I wrote this script so I could play random episodes from my M\*A\*S\*H collection (so the default file extensions are for common video formats and the default player path is the default path for VLC) but the script is basically for opening the files you want with the program you want, so you can use it for whatever.

## usage
* [Optional] Change the global variables in the code to adapt to your situation.
  * You can also directly change the (config) .ini file after the first run, delete the scanned_episodes file and run the script again.
* Place the script in the same folder where your media files are.
* Run it. It will create the config file as well as the file with listed scanned media.
  * It will only put down the media files with the same extension as in the config file (or for the first time running, the default file extensions that are listed in the code).
* Run it again. This time it will pick a random episode from the scanned episodes and open it with the media player whose path is in the config file.
