# Groot Rocker Extensions

Extensions for [groot_rocker](https://github.com/stonier/groot_rocker).

## Examples

## Development Sandbox

Build a basic development image - this will expedite image/container spin-up for
individual workspace sandboxes. Here, this image will be named `groot:devel`:

```
$ groot-rocker \
  --development-environment \
  --tag groot:devel \
  ubuntu:18.04 \
  "echo 'Bless your noggin with a tickle from his most noodly appendages.'"
```

```
$ groot-rocker \
  --user \
  --persistent \
  --named-prompt \
  --tag groot:foo \
  --name foo \
  --bind /mnt/mervin/workspaces/foo:/mnt/foo \
  --work-directory /mnt/foo \
  groot:devel \
  "/bin/bash --login -i"
```

This will enter and leave both a named container around for development. `groot-docker-enter` won't work on a subsequent execution since the container is persisting. Inspect and re-enter via:

```
$ docker container ls -a
CONTAINER ID IMAGE        COMMAND             CREATED    STATUS     NAMES
4db981f214b5 groot:foo "/bin/bash --login -i" 2 mins ago Exited (0) foo

$ docker container start -i foo
```

Re-use the development image to launch a different development environment (bar):

```
$ groot-rocker \
  --user \
  --persistent \
  --named-prompt \
  --tag groot:bar \
  --name bar \
  --bind /mnt/mervin/workspaces/foo:/mnt/bar \
  --work-directory /mnt/bar \
  groot:devel \
  "/bin/bash --login -i"
```
