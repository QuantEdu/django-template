# Deploy

## Initial setup for Ubuntu

1. Create non-root user:
```
adduser quant (pass:quantzone)
```

2. Give root priveleges
```
usermod -aG sudo quant
```

3. Login as user @quant
```angular2html
su - quant
```

TODO: [add nopassword authentication](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04)

## Install docker

[Docker.com](https://docs.docker.com/install/linux/docker-ce/ubuntu/#supported-storage-drivers)
```angular2html
sudo usermod -a -G docker $USER
```
then logout and login

## Install docker-compose
[Docs](https://docs.docker.com/compose/django/#connect-the-database)

## Grant priveleges to opt dir
```angular2html
sudo chmod 777 /opt  
```