# OpenLDAP-Project
Repository of notes for the OpenLDAP Project

## Apache Directory Studio
* In order to get Apache to properly run, I had to [download and install OpenJDK](https://adoptopenjdk.net/)

## MobaxTerm
* There aren't any explicit instructions on what to do with MobaxTerm. I started to use it as a terminal to connect to EC2.

## Setting up EC2

* Followed [this youtube video](https://www.youtube.com/watch?v=rIi8Pd5Uvbc)
* Andrew provided that on the project they are using RedHat Enteprise Linux when they set up environments

### Selecting RedHat OS & Security settings
* Select RedHat Enterprise


![select redhat](img/one.png)

* Add inbound rules to Security group


![Select Edit](img/two.png)
![configure inbound rule](img/three.png)

## Installing OpenLDAP to EC2 instance

### RHEL7
Following [install & config. instructions](cyberithub.com/best-steps-to-install-and-configure-openldap-server-on-rhel-centos-7-8/)
[Needed documentation](digitalocean.com/community/tutorials/how-to-change-account-passwords-on-an-openldap-server) for knowing and changing the root password and user


