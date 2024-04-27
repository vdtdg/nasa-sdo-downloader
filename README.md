# NASA Solar Dynamics Observatory Data Downloader
This repository contains a little Python script to help you download NASA Solar Dynamics Observatory images of the sun.

More details about the SDO [on their website](https://sdo.gsfc.nasa.gov/).

## Instructions

- First, you need Python installed. I recommend Python 3.12.

- Then, you have to install the required dependencies:
```
python3 -m pip install -r requirements.txt
```
- Go into the script, and set the `path` value to a directory where you want the images to be saved.

- Finally, modify the values `start_date`, `end_date`, `resolution`, `channels`, at your will.

For reference:

| Parameter    | Possible values                                                               |
|--------------|-------------------------------------------------------------------------------|
| `resolution` | 4096 2048 1024 512                                                            |
| `channels`   | 0094 0131 0171 0193 0211 0304 0335 1600 1700 HMIB HMII HMID HMIBC HMIIF HMIIC |


/!\ Make sure you have enough space disk before running the script. There are **a lot** of **heavy** images.

## Image credit 
Courtesy of NASA/SDO and the AIA, EVE, and HMI science teams.
![20230101_000629_4096_0193.jpg](sdo_images%2F20230101_000629_4096_0193.jpg)
