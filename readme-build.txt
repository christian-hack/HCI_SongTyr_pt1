Instructions to build SongTyr application:

1- Install Python3:
    1a) This can be done through the Command Line Interface (CLI):
        i) If using Ubuntu 16.10 or newer, enter the following commands:
            $ sudo apt-get update
            $ sudo apt-get install python3.9
        ii) If using another Linux distribution, Python3 should be pre-installed. If not, enter the following command:
            $ sudo dnf install python3

    OR

    1b) This can be done by downloading directly from the Python distribution website: https://www.python.org/downloads/
2- Create a project folder and a venv (Virtual environment) folder through Command Line Interface (CLI):
    2a) Using Windows:
        $ py -3 -m venv venv
    2b) Otherwise:
        $ mkdir myflaskproject
        $ cd myflaskproject
        $ python3 -m venv venv
3- Activate Virtual Environment:
    3a) Using Windows:
        > venv\Scripts\activate
    3b) Otherwise:
        $ .venv/bin/activate
4- Once evironment has been activated, install Flask within the environment with command:
    $ pip install Flask
5- Download Github repository
    5a) Access the Github repository here: https://github.com/christianhack01/HCI_SongTyr.git
    5b) Download the repository into the folder in which the virtual environment was created
6- Install required dependencies for SongTyr
    6a) Take advantage of the 'setup.py' file and streamline installation of these dependencies by entering the following command in the CLI:
        $ python3 setup.py install
7- Setup configuration for Jinja2 template engine
    7a) Create new folder within project folder named "templates"
    7b) Move 'top50.html' into the folder
8- Make slight change to songTyr.py to allow multiple Spotify user logins (optional step if this is not desired)
    8a) Find the code segment just above the first instance of '@app.route'
        ex) 
            if(path.exists("/Users/cphackelman/Desktop/Spotify_Project/.cache")):
                os.remove("/Users/cphackelman/Desktop/Spotify_Project/.cache")
    8b) Replace the existing path argument with the path to your Flask application.
        ** BE SURE TO PRESERVE '/.cache' AT END OF PATH **
        ex)
            if(path.exists("/Users/[username]/[more path]/myflaskproject/.cache")):
                os.remove("/Users/[username]/[more path]/myflaskproject/.cache")
9- Lastly, run the Flask application:
    9a) Enter the following command:
        $ flask run
    9b) A will appear in the CLI. Click the link to allow access to your Spotify account and watch the magic!

-Documentation for Installations/API can be found here:
    i) Python3: https://docs.python.org/3/
    ii) venv: https://docs.python.org/3/library/venv.html
    iii) Flask: https://flask.palletsprojects.com/en/1.1.x/
    iv) Jinja2: https://jinja.palletsprojects.com/en/2.11.x/templates/
    v) Spotify API: https://developer.spotify.com/documentation/
    vi) spotipy: https://spotipy.readthedocs.io/en/2.18.0/
        