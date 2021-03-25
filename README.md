# Groot Rocker Extensions

Extensions for [groot_rocker](https://github.com/stonier/groot_rocker).

## Examples

### Development Sandbox

A customised image/container for your workspace - `foo`:

```
$ groot-rocker \
  --development-environment \
  --user \
  --ssh \
  --persistent \
  --named-prompt \
  --tag groot:foo \
  --name foo \
  --bind /mnt/mervin/workspaces/foo:/mnt/foo \
  --work-directory /mnt/foo \
  ubuntu:18.04 \
  "/bin/bash --login -i"
```

This will create both a named image (`groot:foo`) and container (`foo`). The named image
is useful merely for image management. The named container is very useful for subsequent interactions
with the container. Note that the same command if executed again would fail since the container is persisting. To enter the container again:

```
$ docker container ls -a
CONTAINER ID IMAGE     COMMAND             CREATED    STATUS     NAMES
4db981f214b5 groot:foo "/bin/bash --login -i" 2 mins ago Exited (0) foo

$ docker container start -i foo
```

Launch a different development environment - `bar`:

```
$ groot-rocker \
  --development-environment \
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

### Nvidia Examples

Be sure to install [nvidia-docker 2](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker).

A benchmarking test:

```
$ groot-rocker \
  --nvidia \
  --user \
  --tag groot:glmark2 \
  ubuntu:18.04 \
  "glmark2"
```


An nvidia enabled sandbox - simply add `--nvidia` to the argument list for your usual sandbox:

```
$ groot-rocker \
  --development-environment \
  --nvidia \
  --user \
  --ssh \
  --persistent \
  --named-prompt \
  --tag groot:foo \
  --name foo \
  --bind /mnt/mervin/workspaces/foo:/mnt/foo \
  --work-directory /mnt/foo \
  ubuntu:18.04 \
  "/bin/bash --login -i"
```

Once inside, test the nvidia performace with `glmark2`.
