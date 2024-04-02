## Container commands

### Simple container run with some flags

```shell
docker container run hello-world
```
Talk about output from above!

```shell
docker container run --name cool_container -p 8080:80 -d nginx
```
 - --name must but be unique
 - -p ports ext/int int can depend on image 
 - -d detached mode good
 - -it opens up a terminal to interact with container
 - --rm remove container when done (different from docker container rm)

#### Quiz Answers

1. docker container run -p 8080:80 -d nginx
2. docker container run -it --name test alpine sh
3. docker container run --name greet_me --rm ubuntu echo hello world


docker container ls  (optional -a flag)
(review output table)

docker container stop   (can have multiple container in list no commas just spaces) (no wildcards *)

docker container start (only restarts and existing container, run is like a create/start combo)

docker container rm  (-f flag forces)

docker container prune (remove all)

docker container exec  (with -it flag) to execute a command on an running container

 - find or create a nginx container
 - docker container exec -it nginx sh


docker container inspect [container name]


## Networking

docker network ls

only custom bridge networks allows for DNS resolution! (not the default, "super awesome" per Rose)

docker network create --driver bridge my_network

### Network Demo

 - use network created above

docker container run -d --name c1 --network my_network nginx:alpine
docker container run -d --name c2 --network my_network nginx:alpine
(use nginx:alpine for ping already installed)

 - create two more images, without specifying a network

docker container run -d --name c3 nginx:alpine
docker container run -d --name c4 nginx:alpine

use docker container inspect to show networks and IP addresses

 - access the shell on one of our two networked containers
docker container exec -it c1 ash
 - ping a container that is not on the network
ping -c 2 c3
 - ping a container that is on the network
ping -c 2 c2


docker container exec -it c3 ash
ping -c 2 c1
ping -c 2 c4



## Bind Mounts & Volumes

docker container run -v ...
docker container run --mount ...

for bind mounts
--mount type=bind,source=/absolute/path,target=/absolute/path/in/container

for volumes
--mount type=volume,source=name_of_volume,target=/absolute/path/in/container



### Bind Mounts

 - create a folder called app in your current directory, and make an empty index.html file inside 

- docker container inspect to find out where bind mounts go on nginx

docker container run -d 
--mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html 
-p 8080:80 nginx:alpine

apk add nano

### Volumes

docker pull postgres
docker image inspect postgres
 - inspect the image to find out what the path to the volume should be and what port we want to expose

 - run the container with a volume named "postgres-data" that corresponds to the path where a postgres container stores its data (/var/lib/postgresql/data)

docker container run -p 5431:5432 \
-e POSTGRES_PASSWORD=password \
--name postgres5431 -d \
--mount type=volume,source=postgres-data,target=/var/lib/postgresql/data postgres

- now use the psql command line tool to connect to the postgres instance running in our container

psql -p 5431 -h localhost -U postgres


