#!/bin/bash

set -e

script_dir="$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)"

usage() {
    echo "Usage: ./run.sh [OPTIONS] CHANNEL_NAME"
    echo "Options:"
    echo "  -h, help"
    echo "  -b, build docker image"
    echo "  --post POST_CHANNEL_NAME, post image to POST_CHANNEL_NAME"
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
            flag="post"; param_post_channel="$2"; shift 2
            ;;
        *)
            if [[ ! -z "$1" ]] && [[ ! "$1" =~ ^-+ ]]; then
                param+=( "$1" ); shift 1
            fi
            ;;
    esac
done

token="${param[0]}"
channel="#${param[1]}"
post_channel=""

if [ $with_build -eq 1 ]; then
  docker build -t 'matsuchara/slackloud:latest' "$script_dir"
fi

if [ "$flag" = "post" ]; then
  post_channel="#$param_post_channel"
fi

# for rm container whether script succeeded or failed
set +e

docker run -i -t --rm -v "${script_dir}/src:/app/src" -v "${script_dir}/dic:/app/dic" -v "${script_dir}/result:/app/result" matsuchara/slackloud:latest "$token" "$channel" "$post_channel"
