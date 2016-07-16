#!/bin/bash

set -eu

TOKEN=""

usage() {
    echo "Usage: ./run.sh [OPTIONS] FILE"
    echo "Options:"
    echo "  -h, help"
    echo "  -b, build docker image"
    echo "  --post CHANNEL_NAME, post to CHANNEL_NAME"
    echo "  --cp, no post. cp image to host."
    exit 1
}

flag=""
with_build=0
for OPT in "$@"
do
    case "$OPT" in
        '-h' )
            usage; exit 1
            ;;
        '-b' )
            with_build=1; shift 1
            ;;
        '--post' )
            if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
                echo "option requires an argument -- $1" 1>&2
                exit 1
            fi
            flag="post"; post_channel="$2"; shift 2
            ;;
        '--cp' )
            flag="cp"; shift 1
            ;;
        *)
            if [[ ! -z "$1" ]] && [[ ! "$1" =~ ^-+ ]]; then
                param+=( "$1" ); shift 1
            fi
            ;;
    esac
done

if [ $with_build -eq 1 ]; then
  docker build -t matsuchara/slackloud:latest .
fi

if [ "$flag" = "post" ]; then
  docker run -i -t --rm matsuchara/slackloud "$TOKEN" "#${param[0]}" "#$post_channel"
elif [ "$flag" = "cp" ]; then
  docker run -i -t matsuchara/slackloud "$TOKEN" "#${param[0]}" "no"
  docker cp "$(docker ps -lq):/app/wordcloud.png" .
  docker rm "$(docker ps -lq)" > /dev/null
else
  docker run -i -t --rm matsuchara/slackloud "$TOKEN" "#${param[0]}" "#${param[0]}"
fi
