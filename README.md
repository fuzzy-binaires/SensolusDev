# SensolusDev
Dev for Constant-SpectralDesires-Sensolus, Bruxelles, Dec 2021

## Description

The script will download a list of previously create geo-zones and will randomly assing geozones to phrases in the **text corpus**.
For every geozone change event of each device under ``device_serials.txt`` the text will be modfied and printed out into a thermal
printer thus creating a interactive text intervention.


## Installation

Please make sure to install requirements using pip3.

```bash
pip3 install -r requirements
```

1 - add the device serial number of the tracking devices under ``device_serials.txt``. One serial number per line

2 - Feel free to modify the ``noun_list.txt`` and ``verb_list.txt`` with a custom list of words to replace.

3 - start the script by running:
```bash
$ python3 main.py
```

## Custom queries

By default, the script queries for geo-zone events starting from today's date.
It is also possible to specify a custom geo-zone query date in the past by using the ``--start_date`` command line argument, for example:

```bash
$ python3 main.py --start_date 2021-03-24
```

or modify the frequency at which you can query for new data (in seconds, default is 60):

```bash
$ python3 main.py --refresh_period 120
```

and you can put one right after the other one

```bash
$ python3 main.py --start_date 2021-03-24 --refresh_period 120
```


## Auto Startup and ShutDown scripts

Startup Script for automatically launching the python script when powered on:
```bash
/home/pi/.config/autostart/clock.desktop
```

Auto-shutdown script: A cronJob that triggers at 22:00 every day:
Edit this file:
```bash
sudo crontab -e
```
at the end of it, modify/add this line:
```bash
22 00 * * * /usr/sbin/shutdown -h now
```
