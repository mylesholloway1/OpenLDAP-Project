# OpenLDAP-Project
Repository of notes for the OpenLDAP Project

# Other useful links
* [Copy a file to EC2](medium.com/srcecde/copy-file-directory-to-from-ec2-using-scp-secure-copy-685c46636399)

## Apache Directory Studio
* In order to get Apache to properly run, I had to [download and install OpenJDK](https://adoptopenjdk.net/)

## MobaxTerm
* There aren't any explicit instructions on what to do with MobaxTerm. I started to use it as a terminal to connect to EC2.

## Setting up EC2

* Followed [This youtube video](https://www.youtube.com/watch?v=rIi8Pd5Uvbc)
* On the project they are using RedHat Enteprise Linux when they set up environments

### Selecting RedHat OS & Security settings
* Select RedHat Enterprise


![select redhat](img/five.png)

![select redhat](img/six.png)

![select redhat](img/seven.png)

* Add inbound rules to Security group


![Select Edit](img/two.png)

### Security for OpenLDAP
![configure inbound rule](img/three.png)

### Security for Ansible
![configure inbound rule](img/eight.png)



## Installing OpenLDAP to EC2 Instance

### On RHEL7
* Following [install & config. instructions](https://cyberithub.com/best-steps-to-install-and-configure-openldap-server-on-rhel-centos-7-8/)
* [Needed documentation](https://digitalocean.com/community/tutorials/how-to-change-account-passwords-on-an-openldap-server) for knowing and changing the root password and user


## Installing Ansible to EC2 Instance

### On RHEL7
* Following [install & config. instructions](https://developers.redhat.com/blog/2016/08/15/install-ansible-on-rhel#)

## Connecting Ansible Server to OpenLDAP
* [ansible Documentation](https://docs.ansible.com/ansible/latest/getting_started/index.html)
* I ultimatley followed [this video](https://youtube.com/watch?v=EGWyN6DMI1g) becuase at times the ansible doc is very vauge on steps
