### Virtual environment
[anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ python --version
[anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ python3 -m venv venv
[anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ python3 -m venv .venv


### Environment variable
[anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ nano ~/.bashrc
source /home/anup/Job-Description/YEAR2024/MASTEK-Senior-Engineer-JAN/.venv/bin/activate

(.venv) [anup@automation-and-continuous-delivery ~]$ which python
~/Job-Description/YEAR2024/MASTEK-Senior-Engineer-JAN/.venv/bin/python


### Dependencies and Directory structure
(.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ touch requirement.txt
(.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ touch Dockerfile
(.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ touch Makefile
(.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ mkdir lib
(.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ touch lib/__init__.py
(.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ touch main.py


### Makefile 
(.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ make install
(.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ git status
(.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ make format

### requirements.txt
(.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ pip freeze | less


# CLI Fire
(.venv) (.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ sudo chmod 754 cli-fire.py
(.venv) (.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ ./cli-fire.py --help
(.venv) (.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ ./cli-fire.py
(.venv) (.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ ./cli-fire.py --length 10
(.venv) (.venv) [anup@automation-and-continuous-delivery MASTEK-Senior-Engineer-JAN]$ ./cli-fire.py --length 10 | less