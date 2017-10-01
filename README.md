# Software-developer-internship-script
This script will interact with a cyber physical system, download its data and manipulate its values.
# Watchman

The watchman framework allows easy creation of invariants in Python.

## Installation

```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install redis-server # if you don't have redis
$ sudo pip install requirements.txt

```


## How to run the program

```bash

$ python main.py # starts the invariant checker, logs on the screen.

$ python main.py -d # starts the daemon. so choose one of the above commands

$ cd argus

$ python app.py # Starts the web server

```

If you are running the argus web server simply visit http://localhost:5000 to look at the status of the PLCs.
