#!/bin/bash

set -eu

###
# ex1: post wordcloud image about #general to #general
# docker run -i -t --rm slackloud "TOKEN" "#general"
#
# ex2: post wordcloud image about #general to #my_channel
# docker run -i -t --rm slackloud "TOKEN" "#general" "#my_channel"
#
# ex3: 'no' means 'no post image to slack'.
# docker run -i -t slackloud "TOKEN" "#general" "no"
# docker cp "$(docker ps -lq)":/app/wordcloud".png .
# docker rm "$(docker ps -lq)" > /dev/null
###

### if you changed the source, turn this on.
# docker build -t slackloud:latest .

docker run -i -t --rm slackloud "TOKEN" "$1"

