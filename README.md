# slackloud

- slack history api
- wordcloud

![example](https://github.com/matsu-chara/slackloud/blob/master/example/example.png?raw=true "example")

## USAGE

```bash
#1 get your slack token
# https://api.slack.com/web#authentication

#2 pull image
docker pull matsuchara/slackloud

#3 prepare run.sh
cat << EOF > run.sh
#!/bin/bash
./_run.sh "YOUR_TOKEN" "\$@"
EOF

#4 generate image ( `./run.sh -h` show help.)
./run.sh "CHANNEL"

#5 your wordcloud is here!
open result/wordcloud.png
```

## linting

```bash
hadolint Dockerfile
pylint src
```

