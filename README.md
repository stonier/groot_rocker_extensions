# Groot Rocker Extensions

Extensions for [groot_rocker](https://github.com/stonier/groot_rocker).

## Examples

### Development Sandbox

Build a basic development image - this will expedite image/container spin-up for
individual workspace sandboxes. Here, this image will be named `groot:devel`:

```
$ groot-rocker \
  --development-environment \
  --tag groot:devel \
  ubuntu:18.04 \
  "echo 'Bless your noggin with a tickle from his most noodly appendages.'"
```

Now launch a customised image/container for your workspace:

```
$ groot-rocker \
  --user \
  --ssh \
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
  --ssh \
  --persistent \
  --named-prompt \
  --tag groot:bar \
  --name bar \
  --bind /mnt/mervin/workspaces/foo:/mnt/bar \
  --work-directory /mnt/bar \
  groot:devel \
  "/bin/bash --login -i"
```

Ping between the two containers across the docker bridge:

```
# Foo
$ docker container start -i foo
$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.2  netmask 255.255.0.0  broadcast 172.17.255.255

# Bar
$ docker container start -i bar
$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.3  netmask 255.255.0.0  broadcast 172.17.255.255
$ ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
64 bytes from 172.17.0.2: icmp_seq=1 ttl=64 time=0.047 ms
$ ssh `whoami`@192.168.1.4  # replace this ip with your host's ip
```
