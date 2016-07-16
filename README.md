# slackloud

- slack history api
- wordcloud

![example](https://github.com/matsu-chara/slackloud/blob/master/example/example.png?raw=true "example")

## USAGE

```
#1 get your slack token
# https://api.slack.com/web#authentication

#2 pull image
docker pull matsuchara/slackloud

#3 copy run.sh & write your token
cp _run.sh run.sh
vim run.sh

#4 generate image and post to slack! ( `-b` means "with docker build". `-h` show help.)
./run.sh "#CHANNEL"
```

## linting

```
hadolint Dockerfile
pylint src
```

