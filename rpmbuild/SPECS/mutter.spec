%global glib_version 2.75.1
%global gtk3_version 3.19.8
%global gtk4_version 4.0.0
%global gsettings_desktop_schemas_version 47~beta
%global libinput_version 1.19.0
%global pipewire_version 0.3.33
%global lcms2_version 2.6
%global colord_version 1.4.5
%global libei_version 1.0.901
%global mutter_api_version 15
%global mutter_name mutter

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:          mutter-x11-scaling
Version:       47.5
Release:       %autorelease
Summary:       Window and compositing manager based on Clutter

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://www.gnome.org
Source0:       http://download.gnome.org/sources/%{mutter_name}/47/%{mutter_name}-%{tarball_version}.tar.xz

# Work-around for OpenJDK's compliance test
Patch:         0001-window-actor-Special-case-shaped-Java-windows.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1936991
Patch:         mutter-42.alpha-disable-tegra.patch

# https://pagure.io/fedora-workstation/issue/79
Patch:         0001-place-Always-center-initial-setup-fedora-welcome.patch

# https://pagure.io/fedora-workstation/issue/357
Patch:         0001-gschema-Enable-fractional-scaling-experimental-featu.patch

# Add scaling support using randr under x11 and dynamic triple buffering support
Patch:	       x11-Add-support-for-fractional-scaling-using-Randr.patch
Patch:         Support-Dynamic-triple-double-buffering.patch

BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.41.0
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xtst)
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGLES-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pam-devel
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: pkgconfig(libpipewire-0.3) >= %{pipewire_version}
BuildRequires: pkgconfig(sysprof-capture-4)
BuildRequires: sysprof-devel
BuildRequires: pkgconfig(libsystemd)
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: desktop-file-utils
BuildRequires: cvt
# Bootstrap requirements
BuildRequires: gettext-devel git-core
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= %{gsettings_desktop_schemas_version}
BuildRequires: pkgconfig(gnome-settings-daemon)
BuildRequires: meson
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(wayland-eglstream)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(lcms2) >= %{lcms2_version}
BuildRequires: pkgconfig(colord) >= %{colord_version}
BuildRequires: pkgconfig(libei-1.0) >= %{libei_version}
BuildRequires: pkgconfig(libeis-1.0) >= %{libei_version}

BuildRequires: pkgconfig(libinput) >= %{libinput_version}
BuildRequires: pkgconfig(xwayland)

BuildRequires: python3-dbusmock

Requires: control-center-filesystem
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gnome-settings-daemon
Requires: gtk4%{?_isa} >= %{gtk4_version}
Requires: libinput%{?_isa} >= %{libinput_version}
Requires: pipewire%{_isa} >= %{pipewire_version}
Requires: startup-notification
Requires: dbus

# Provides mutter libraries
Provides: %{mutter_name}%{?_isa} = %{version}-%{release}
Obsoletes: %{mutter_name} < %{version}-%{release}
Conflicts: %{mutter_name}

# Need common
Requires: %{name}-common = %{version}-%{release}

Recommends: mesa-dri-drivers%{?_isa}

Provides: firstboot(windowmanager) = mutter

# Cogl and Clutter were forked at these versions, but have diverged
# significantly since then.
Provides: bundled(cogl) = 1.22.0
Provides: bundled(clutter) = 1.26.0

Conflicts: mutter < 45~beta.1-2

# Make sure dnf updates gnome-shell together with this package; otherwise we
# might end up with broken gnome-shell installations due to mutter ABI changes.
Conflicts: gnome-shell < 45~rc

%description
Mutter is a window and compositing manager that displays and manages
your desktop via OpenGL. Mutter combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

While Mutter can be used stand-alone, it is primarily intended to be
used as the display core of a larger system such as GNOME Shell. For
this reason, Mutter is very extensible via plugins, which are used both
to add fancy visual effects and to rework the window management
behaviors to meet the needs of the environment.

%package common
Summary: Common files used by %{mutter_name} and forks of %{mutter_name}
BuildArch: noarch
Conflicts: mutter < 45~beta.1-2
# Provides mutter-common libraries
Provides: %{mutter_name}-common = %{version}-%{release}
Obsoletes: %{mutter_name}-common < %{version}-%{release}
Conflicts: %{mutter_name}-common

%description common
Common files used by Mutter and soft forks of Mutter

%package devel
Summary: Development package for %{mutter_name}
Requires: %{mutter_name}%{?_isa} = %{version}-%{release}
# for EGL/eglmesaext.h that's included from public cogl-egl-defines.h header
Requires: mesa-libEGL-devel

%description devel
Header files and libraries for developing Mutter plugins. Also includes
utilities for testing Metacity/Mutter themes.

%package  tests
Summary:  Tests for the %{mutter_name} package
Requires: %{mutter_name}-devel%{?_isa} = %{version}-%{release}
Requires: %{mutter_name}%{?_isa} = %{version}-%{release}
Requires: gtk3%{?_isa} >= %{gtk3_version}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%autosetup -S git -n %{mutter_name}-%{tarball_version}

%build
%meson -Degl_device=true -Dwayland_eglstream=true
%meson_build

%install
%meson_install

%find_lang %{mutter_name}

%files -f %{mutter_name}.lang
%license COPYING
%doc NEWS
%{_bindir}/mutter
%{_libdir}/lib*.so.*
%{_libdir}/mutter-%{mutter_api_version}/
%{_libexecdir}/mutter-restart-helper
%{_libexecdir}/mutter-x11-frames
%{_mandir}/man1/mutter.1*

%files common
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.x11.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-*.xml
%{_udevrulesdir}/61-mutter.rules

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%files tests
%{_libexecdir}/installed-tests/mutter-%{mutter_api_version}
%{_datadir}/installed-tests/mutter-%{mutter_api_version}
%{_datadir}/mutter-%{mutter_api_version}/tests

%changelog
%autochangelog
