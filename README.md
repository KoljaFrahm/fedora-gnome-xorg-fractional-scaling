# fedora-gnome-xorg-fractional-scaling

Xorg fractional scaling on Fedora Linux 41 and GNOME 47, patches taken from https://github.com/puxplaying/mutter-x11-scaling and https://github.com/puxplaying/gnome-control-center-x11-scaling

![After installation screenshot](https://user-images.githubusercontent.com/58503327/202655092-7eff9828-589e-4d81-a061-d97ef68d19b9.png)

## How to install

- Download `mutter-x11-scaling-{version}.src.rpm` and `gnome-control-center-{version}.src.rpm` from Releases page
  (for me the following steps first didn't work because I was in a conda environment, so be sure to use conda deactivate before)

```
# dnf in -y rpm-build
$ rpm -Uvh ./mutter-x11-scaling-{version}.src.rpm ./gnome-control-center-{version}.src.rpm
$ cd ~/rpmbuild/SPECS
# dnf builddep mutter.spec
$ rpmbuild --clean -ba mutter.spec
# dnf builddep gnome-control-center.spec
$ rpmbuild --clean -ba gnome-control-center.spec
$ cd ~/rpmbuild/RPMS/
# dnf install ./noarch/mutter-x11-scaling-common-{version}.rpm ./x86_64/mutter-x11-scaling-{version}.rpm --allowerasing
# rpm --force -iv ./noarch/gnome-control-center-filesystem-{version}.noarch.rpm ./x86_64/gnome-control-center-{version}.x86_64.rpm
# echo "exclude=gnome-control-center-filesystem gnome-control-center" >> /etc/dnf/dnf.conf
```

## or installing with `mock` (not tested with Fedora 40/41)

- Download `mutter-43.0-4.fc37.src.rpm` and `gnome-control-center-43.0-2.fc37.src.rpm` from Releases page

```
$ mock -r fedora-37-x86_64 ./mutter-43.0-4.fc37.src.rpm
$ cp -v /var/lib/mock/results/*.rpm .
$ mock -r fedora-37-x86_64 ./gnome-control-center-43.0-2.fc37.src.rpm
$ cp -v /var/lib/mock/results/*.rpm .
# rpm --force -iv ./x86_64/mutter-43.0-4.fc37.x86_64.rpm ./noarch/gnome-control-center-filesystem-43.0-2.fc37.noarch.rpm ./x86_64/gnome-control-center-43.0-2.fc37.x86_64.rpm
# echo "exclude=mutter gnome-control-center-filesystem gnome-control-center" >> /etc/dnf/dnf.conf
```

## Using prebuilt binaries

- Download `mutter-x11-scaling-common-{version}.noarch.rpm`, `mutter-x11-scaling-{version}.x86_64.rpm`, `gnome-control-center-filesystem-{version}.noarch.rpm` and `gnome-control-center-{version}.x86_64.rpm` from Releases page

```
# dnf install ./noarch/mutter-x11-scaling-common-{version}.rpm ./x86_64/mutter-x11-scaling-{version}.rpm --allowerasing
# rpm --force -iv ./noarch/gnome-control-center-filesystem-{version}.noarch.rpm ./x86_64/gnome-control-center-{version}.x86_64.rpm
# echo "exclude=gnome-control-center-filesystem gnome-control-center" >> /etc/dnf/dnf.conf
```

## How to reinstall the original mutter

```
# dnf install mutter mutter-common --allowerasing
```

## How to update repository

- Update mutter spec and patches from https://src.fedoraproject.org/rpms/mutter for the right Gnome version
- Update gnome-control-center spec and patches from https://src.fedoraproject.org/rpms/gnome-control-center for the right Gnome version
- Download correct tar.xz from https://download.gnome.org/sources/gnome-control-center/ and https://download.gnome.org/sources/mutter/
- Update scaling patches from
  - https://salsa.debian.org/gnome-team/mutter/-/tree/ubuntu/latest/debian/patches/ubuntu?ref_type=heads
  - https://salsa.debian.org/gnome-team/mutter/-/tree/ubuntu/latest/debian/patches/debian?ref_type=heads
  - https://salsa.debian.org/gnome-team/gnome-control-center/-/tree/ubuntu/latest/debian/patches/ubuntu?ref_type=heads
- Clean the folder ~/rpmbuild
- Go to the SPECS folder of this git and do
  `rpmbuild -bs <mutter/gcc>.spec`
