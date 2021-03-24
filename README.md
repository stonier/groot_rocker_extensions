# Groot Rocker Extensions

Extensions for [groot_rocker](https://github.com/stonier/groot_rocker).

## Examples

## Development Sandbox

Map user and a workspace into the container. Make it persistent, so the development environment
can be further modified as needed.

```
$ groot-rocker \
  --user \
  --name=workspace \
  --persistent \
  --named-prompt \
  --tag groot:foo \
  --work-directory /mnt/foo \
  --bind /mnt/mervin/workspaces/foo:/mnt/foo \
  -- \
  ubuntu:18.04 \
  "/bin/bash --login -i"
```

This will enter and leave a container around for development. `groot-docker-enter` won't work
on a subsequent execution since the container is persisting. Inspect and re-enter via:

```
$ docker container ls -a
CONTAINER ID IMAGE        COMMAND                CREATED       STATUS     NAMES
4db981f214b5 groot:foo "/bin/bash --login -i" 2 mins ago Exited (0) workspace

$ docker container start -i workspace
```