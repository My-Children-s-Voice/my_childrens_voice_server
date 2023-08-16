# My Childrens Voice Server
자녀의 목소리 서버

## Development Environment

|Category| - |
| --- | --- |
|Language|python v3.11.4|
|Web Framework|Django v4.2.4|
|API|RESTful API(drf v3.14.0)|

## How to Execute

Execute the following lines to properly clone and run the project.   
config.yaml file is required.

```
$ git clone https://github.com/My-Children-s-Voice/my_childrens_voice_server.git
add config.yaml to /my_childrens_voice_server/config 
$ conda create -n ["env"] python=3.11.4
$ conda activate ["env"]
$ cd my_childrens_voice_server
$ conda install mysqlclient
$ pip install -r requirements.txt
$ python manage.py runserver