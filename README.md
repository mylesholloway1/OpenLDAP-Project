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

* Following [install instructions](https://www.herongyang.com/Linux/LDAP-Install-OpenLDAP-Server-on-CentOS-8.html)
* During Step 4. Change the OpenLDAP version from openldap-2.4.9.tgz to the desired version (the version mentioned in the e-mail)

### Errors
* while configuring, if cannot locate cc(1) run ```sudo yum install gcc```
* while configuring, if cannot locate libtool run ```yum install libtool-ltdl-devel```


```sudo yum install cyrus-sasl-devel make libtool autoconf libtool-ltdl-devel openssl-devel libdb-devel tar gcc perl perl-devel wget vim

sudo useradd -r -M -d /var/lib/openldap -u 55 -s /usr/sbin/nologin ldap

```



