# Specific to this app
API keys are by default kept in the home directory in a file called api.json
If you choose to keep the keys in a differenct path or file you must edit keys.py


# General Principles

# Generic APP

* This is a generic flask app which I have used for education purposes. Below is some of the major resources
which deserve credit based on the amount of content uses. *

As a result I have tried to put as much comments as possible. From Git (local, remote repositores) to the extras not covered on most books such as little niggles with deployment etc.

## GIT (local)
### Git Config

### Git Add

### Git Push


### Git Pull

## GIT HUB



# GOOGLE
## Compute ENgines - Virtual Machines (VM)

## GCLOUD
1. Install Cloud SDK
2. Authorize cloud SDK on your behalf to access your project and acquire an auth token
3. `gcloud init` [Initial Setup](https://cloud.google.com/compute/docs/gcloud-compute)
4. 


## Useful Commands
$ gcloud compute instances list


SSH into your VM Instance:

gcloud compute ssh 
gcloud compute ssh --zone "europe-west3-c" "my-project" --project "my-instance"


**Instance File Directory**
automatically taken to home:  ~
This is a fairl empty place. 
$ ls -a
.  ..  .bash_history  .bash_logout  .bashrc  .cache  .cloud-locale-test.skip  .nano  .profile  .ssh  .wget-hsts  readme.md

> I want to begin SSHing into place like a remote repository etc


### Generate a new Key in Gcloud
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

follow prompts
Start SSH Agent:
$ eval "$(ssh-agent -s)"
> Agent pid 59566

Add your SSH private key to the ssh-agent. 
$ ssh-add ~/.ssh/id_rsa 
>> Identity added: /home/name_of_home/.ssh/id_rsa (/home/name_of_home/.ssh/id_rsa)

$ sudo apt-get install xclip
Downloads and installs xclip. If you don't have `apt-get`, you might need to use another installer (like `yum`)

$ xclip -sel clip < ~/.ssh/id_rsa.pub
Copies the contents of the id_rsa.pub file to your clipboard
or just cat the file

** Add this to your github SSH keys **
[Github SSH](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)


## SERVER 
We are going to run Apache 
[Ubuntu Resource](https://ubuntu.com/tutorials/install-and-configure-apache#3-creating-your-own-website)
You Apache2 resource can be found and configured in this path:
/etc/apache2/sites-enabled/000-default.conf

# genericApp
python3 -m venv env

This is a


Install Dependencies
----------------------
pip install -r requirements.txt


# The Application Itself

## Working with Files and the Operating system
[working with files and OS](https://realpython.com/working-with-files-in-python/)
[OS module](https://docs.python.org/3/library/os.html)
[open file - simplest](https://docs.python.org/3/library/functions.html#open)


> import os



## Requests TO flask 
[request to flask ](https://flask.palletsprojects.com/en/0.12.x/reqcontext/)


## HTTP/S Requests FROM flask
As per the system of all Networks their is a request response

Reuests are handled by pythons **urllib.request** 
[urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)

The response object is handled by **http.client**
[http.client](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse)


###Resources
1. Flask by Example - Gareth Dwyer