# slackloud

- slack history api
- wordcloud

![example](example/example.png "example")

## USAGE

```
#1 get your slack token
# https://api.slack.com/web#authentication

#2 build image
docker build -t slackloud:latest .

#3 run container
docker run -i -t --name slackloud "YOUR_SLACK_TOKEN" "#CHANNEL"

#3 (b) you can also use
cp _run.sh run.sh
vim run.sh
./run.sh "#CHANNEL"
```

## linting

```
hadolint Dockerfile
pylint src
```

