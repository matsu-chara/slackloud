# slackloud

- slack history api
- wordcloud

![example](example/example.png "example")

## USAGE

```
#1 get your slack token
# https://api.slack.com/web#authentication

#2 copy run.sh & write your token
cp _run.sh run.sh
vim run.sh

#3 generate image and post to slack! ( `-b` means "with docker build". `-h` show help.)
./run.sh "#CHANNEL"
```

## linting

```
hadolint Dockerfile
pylint src
```

