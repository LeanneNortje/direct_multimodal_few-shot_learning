#!/bin/bash

#_________________________________________________________________________________________________
#
# Author: Leanne Nortje
# Year: 2019
# Email: nortjeleanne@gmail.com
#_________________________________________________________________________________________________

docker run -v "$(pwd)":/home -u $(id -u):$(id -g) --rm -it cpu_docker_image 