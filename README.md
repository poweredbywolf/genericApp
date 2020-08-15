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



# genericApp
python3 -m venv env

This is a


Install Dependencies
----------------------
pip install -r requirements.txt




###Resources
1. Flask by Example - Gareth Dwyer