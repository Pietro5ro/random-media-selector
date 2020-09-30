from os import scandir, stat, curdir
from os.path import isdir, isfile, splitext, exists
from typing import List
from random import randint
from subprocess import call
from configparser import ConfigParser


FOLDER_LOCATION = curdir + "\\"
CONFIG_FILE = FOLDER_LOCATION + "cfg.ini"
SCAN_FILE = FOLDER_LOCATION + "scanned_episodes.csv"
FILE_EXT = [".mkv", ".mp4", ".wmv", ".avi"]
VIDEO_PLAYER_PATH = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"


def should_config() -> bool:
    return (not exists(CONFIG_FILE)) or stat(CONFIG_FILE).st_size == 0


def should_scan() -> bool:
    return (not exists(SCAN_FILE)) or stat(SCAN_FILE).st_size == 0


def is_episode(path: str) -> bool:
    return isfile(path) and splitext(path)[1] in FILE_EXT


def config() -> None:
    config_object = ConfigParser()
    config_object["CFGINFO"] = {
        "folder": FOLDER_LOCATION,
        "scan_file": SCAN_FILE,
        "file_ext": "|".join(FILE_EXT),
        "mediaplayer_path": VIDEO_PLAYER_PATH,
    }

    with open(CONFIG_FILE, 'w') as cfg:
        config_object.write(cfg)


def load_config() -> None:
    global FOLDER_LOCATION
    global SCAN_FILE
    global FILE_EXT
    global VIDEO_PLAYER_PATH

    config_object = ConfigParser()
    config_object.read(CONFIG_FILE)
    config_info = config_object["CFGINFO"]

    FOLDER_LOCATION = config_info["folder"]
    SCAN_FILE = config_info["scan_file"]
    FILE_EXT = config_info["file_ext"].split("|")
    VIDEO_PLAYER_PATH = config_info["mediaplayer_path"]


def scan(cur_location: str, entries: List[str]):
    with scandir(cur_location) as filders:
        for filder in filders:
            if isdir(filder):
                scan(filder.path + "\\", entries)
            if isfile(filder) and is_episode(filder.path):
                entries.append(filder.path + "\n")


def select_random():
    with open(SCAN_FILE, 'r') as cfg:
        episodes = cfg.readlines()
        episode_index = randint(0, len(episodes) - 1)
        episode_path = episodes.pop(episode_index)
        print(episode_path)

    with open(SCAN_FILE, 'w') as cfg:
        cfg.writelines(episodes)
    call([VIDEO_PLAYER_PATH, episode_path.strip("\n")])


if __name__ == '__main__':
    if should_config():
        config()
    else:
        load_config()

    if should_scan():
        entries = []
        with open(SCAN_FILE, 'w') as cfg:
            scan(FOLDER_LOCATION, entries)
            cfg.writelines(entries)
    else:
        select_random()
