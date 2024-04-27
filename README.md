# NASA Solar Dynamics Observatory Data Downloader

This repository contains a little Python script to help you download NASA Solar Dynamics Observatory images of the sun.

More details about the SDO [on their website](https://sdo.gsfc.nasa.gov/).

## Instructions

- First, you need Python installed. I recommend Python 3.12.

- Then, you have to install the required dependencies:

```
python3 -m pip install -r requirements.txt
```

- Set the following environment variables: Go into the script, and set the `path` value to a directory where you want
  the images to be saved.

| Environment variables | Possible values                                                               | Note                                                 | Default value |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------|---------------|
| `SDO_RESOLUTION`      | 4096,2048,1024,512                                                            | One value possible                                   | 4096          |
| `SDO_CHANNELS`        | 0094,0131,0171,0193,0211,0304,0335,1600,1700,HMIB,HMII,HMID,HMIBC,HMIIF,HMIIC | Multiple values possible, separated by a comma       | 0094,0193     |
| `SDO_IMAGE_DIRECTORY` | ./sdo_images/ or /home/user/sdo_images or D:\\sdo_images\                     | Path, can be relative or absolute                    | sdo_images/   |
| `SDO_START_DATE`      | Any date                                                                      | Date in the YYYY-MM-DD format. Included in the range | 2023-01-13    |
| `SDO_END_DATE`        | Any date after SDO_START_DATE                                                 | Date in the YYYY-MM-DD format. Included in the range | 2023-01-14    |

Finally, run the script. Here's an example:  
`SDO_RESOLUTION=4096 SDO_CHANNELS=0094,0193 SDO_IMAGE_DIRECTORY=sdo_images/ SDO_START_DATE=2023-01-13 SDO_END_DATE=2023-01-14 python3 main.py`    

You don't have to set all the environment variables, as they have default values, e.g:  
`python3 main.py`  => Will yield the same result as above.  

/!\ Make sure you have enough space disk before running the script. There are **a lot** of **heavy** images.

Also, as there are a lot of images, it might take a long time to download a large range of images. Image download is not
parallelized in order not to overwhelm the servers. It takes approximately 5 minutes to download a full day of image, for one resolution and one channel.

## Image credit

Courtesy of NASA/SDO and the AIA, EVE, and HMI science teams.
![20230101_000629_4096_0193.jpg](sdo_images%2F20230101_000629_4096_0193.jpg)
