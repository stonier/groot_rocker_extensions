# Groot Rocker Extensions

Extensions for [groot_rocker](https://github.com/stonier/groot_rocker).

* **bind**: mount a host dir at a specified location inside the container
* **development_environment**: system dependencies and env variables for development
* **git**: transfer the user's git configuration across to the container
* **named_prompt**: a coloured <user>@<container-name> prompt
* **nvidia**: enable nvidia
* **ssh**: install ssh dependencies, transfer the ssh agent into the container
* **user**: replicate the script's user in the image (useful for avoiding permission problems)
* **work_directory**: specify the starting directory on entry into the container

## Examples

**Development Workspace**

A customised image/container for your development workspace (`foo`):

```
$ groot-rocker-workspace --name foo --bind /mnt/mervin/workspaces/foo:/mnt/foo --work-directory /mnt/foo ubuntu:18.04
```

This will create both a named image (`workspace:foo`) and container (`foo`). The named image
is useful merely for image management. The named container is very useful for subsequent interactions
with the container. Note that the same command if executed again would fail since the container is persisting. To enter the container again:

```
$ docker container ls -a
CONTAINER ID IMAGE     COMMAND             CREATED    STATUS     NAMES
4db981f214b5 devel:foo "/bin/bash --login -i" 2 mins ago Exited (0) foo

$ docker container start -i foo
```

Launch a different development environment - `bar`:

```
$ groot-rocker-workspace --name bar --bind /mnt/mervin/workspaces/bar:/mnt/bar --work-directory /mnt/foo ubuntu:18.04
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


The `groot-rocker-sandbox` is actually, merely a convenience wrapper around the underlying `groot-rocker` command. Fully expanded:

```
$ groot-rocker \
  --development-environment \
  --user \
  --git \
  --ssh \
  --persistent \
  --image-name devel:foo \
  --container-name foo \
  --named-prompt \
  --bind /mnt/mervin/workspaces/foo:/mnt/foo \
  --work-directory /mnt/foo \
  ubuntu:18.04 \
  "/bin/bash --login -i"
```


**Nvidia Benchmark**

Be sure to install [nvidia-docker 2](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker).

A benchmarking test:

```
$ groot-rocker \
  --nvidia \
  --user \
  --image-name groot:glmark2 \
  ubuntu:18.04 \
  "glmark2"
```

**Nvidia Workspace**

An nvidia enabled workspace - simply add `--nvidia` to the argument list for a development workspace:

```
$ groot-rocker-workspace \
  --name foo \
  --bind /mnt/mervin/workspaces/foo:/mnt/foo \
  --work-directory \
  --nvidia
  /mnt/foo \
  ubuntu:18.04
```

Once inside, test the nvidia performace with `glmark2`.
