# $Id$
# This spec file is part of Los Angeles GNU/Linux and distributed 
# under the terms of the GNU General Public License version 2
# Copyright (c) 2005 by Los Angeles GNU/Linux Team
# Homepage: http://los-angeles.berlios.de/

# vim: set ft=spec: -*- mode: rpm-spec; -*-

# TODO: Double-making build to support 3DFX Glide (tm). // sectoid
# TODO: clean up Group information. // icesik
# TODO: #define BuildHtmlManPages	NO !!!! // icesik
# TODO: add /sbin/ldconfig to all packages that is need this! // icesik
# TODO: PreReq: chkfontpath // icesik
# TODO: clean up spec! // icesik
# TODO: // icesik
####### ld.so.conf.d support
#######%__mkdir_p %buildroot%_sysconfdir/ld.so.conf.d
#######echo "%_x11libdir" > %buildroot%_sysconfdir/ld.so.conf.d/X11R6.conf

%define maintainer	Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru>
%define name		xorg
%define ver		6.8.2
%define rel		los1.1
%define _iconsdir	/usr/X11R6/lib/X11/icons/
%define _x11fontsdir	/usr/X11R6/lib/X11/fonts/

Summary:	Part of the X.Org implementation of the X Window System
Name:		%{name}
Version:	%{ver}
Release:	%{rel}
Packager:	%{maintainer}
License:	X/MIT and other
Group:		X11
Source0:	X11R%{version}-src.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
If you want to install the X Window System (TM) on
your machine, you'll need to install X.Org.

The X Window System provides the base technology
for developing graphical user interfaces. Simply stated,
X draws the elements of the GUI on the user's screen and
builds methods for sending user interactions back to the
application. X also supports remote application deployment-running an
application on another computer while viewing the input/output
on your machine.  X is a powerful environment which supports
many different applications, such as games, programming tools,
graphics programs, text editors, etc.  X.Org is the version of
X which runs on Linux, as well as other platforms.

This package contains the basic fonts, programs and documentation
for an X workstation.  However, this package doesn't provide the
program which you will need to drive your video hardware.  To
control your video card, you'll need the particular X server
package which corresponds to your computer's video card.

In addition to installing this package, you will need to install
the X.Org package which corresponds to your video card, the
Xconfigurator package and the xorg-libs package. You may also
need to install one of the X.Org fonts packages.

And finally, if you are going to develop applications that run as
X clients, you will also need to install xorg-devel.

%package server
Summary: The X server from release of X.Org
Group: System/X11
#PreReq: xorg-server-control
Requires: %{name}-server-common = %{version}-%{release}

%description server
xorg-x11-server is the new generation of X server from X.Org.

%package libs
Summary: Shared libraries needed by the X Window System version 11 release 6
Group: System/Libraries
Requires: %{name}-locales = %{version}-%{release}

%description libs
This package contains the shared libraries that most X programs
need to run properly. These shared libraries are in a separate package in
order to reduce the disk space needed to run X applications on a machine
without an X server (i.e, over a network).

%package xapps
Group: System/X11
Summary: Graphical application for Xorg
Requires: %{name}-utils = %{version}-%{release}

%description xapps
Graphical application for Xorg.

%package xauth
Summary: X authority file utility
Group: System/X11
Requires: %{name}-libs = %{version}-%{release}

%description xauth
The xauth program is used to edit and display the authorization information
used in connecting to the X server.

%package xdm
Summary: X Display Manager
Group: System/X11
Requires: %{name}-libs = %{version}-%{release}

%description xdm
Xdm  manages a collection of X displays, which may be on the local host
or remote servers.  The design of xdm was guided by the needs of X ter-
minals  as well as The Open Group standard XDMCP, the X Display Manager
Control Protocol.  Xdm provides services similar to those  provided  by
init, getty and login on character terminals: prompting for login name
and password, authenticating the user, and running a "session".

%package rstart
Summary: A sample implementation of a Remote Start client for the X Window System
Group: System/X11
Requires: %{name}-server = %{version}-%{release}
Requires: %{name}-font-utils = %{version}-%{release}

%description rstart
Rstart  is  a simple implementation of a Remote Start client as defined
in "A Flexible Remote Execution Protocol Based on ssh".  It uses ssh as
its underlying remote execution mechanism.

%package xfs
Group: System/Servers
Summary: Font server for X.Org
#PreReq: shadow-utils
Requires: %{name}-libs = %{version}-%{release}
Requires: %{name}-server-common = %{version}-%{release}

%description xfs
This is a font server for X.Org.  You can serve fonts to other X servers
remotely with this package, and the remote system will be able to use all
fonts installed on the font server, even if they are not installed on the
remote computer.

%package -n twm
Group: System/X11
Summary: Tab Window Manager for the X Window System
Requires: %{name}-server = %{version}-%{release}

%description -n twm
Twm is a window manager for the X Window System. It provides titlebars,
shaped windows, several forms of icon management, user-defined macro
functions, click-to-type and pointer-driven keyboard focus, and
user-specified key and pointer button bindings.

%package locales
Summary: This package contains set of X.Org locales
Group: System/Internationalization

%description locales
This package contains set of X.Org locales.

%package drv-v4l
Summary: video4linux driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-v4l
v4l  is  an  Xorg  driver  for video4linux cards.  It provides a Xvideo
extention port for video overlay.  Just add the driver  to  the  module
list  within  the  module section of your xorg.conf file if you want to
use it.  There are no config options.

%package drv-input
Summary: input drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-input
input drivers for X Window System

%package drv-glint
Summary: GLINT/Permedia video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-glint
glint  is  an Xorg driver for 3Dlabs & Texas Instruments GLINT/Permedia
based video cards. The driver is rather fully accelerated, and provides
support  for  the  following  framebuffer  depths:  8, 15 (may give bad
results with FBDev support), 16, 24 (32 bpp  recommended,  24  bpp  has
problems), 30, and an 8+24 overlay mode.

%package drv-tdfx
Summary: 3Dfx video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-tdfx
tdfx is an Xorg driver for 3Dfx video cards.

%package drv-savage
Summary: S3 Savage video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-savage
savage  is  an  Xorg  driver for the S3 Savage family video accelerator
chips.  2D, 3D, and Xv acceleration is supported on  all  chips  except
the  Savage2000  (2D only).  Dualhead operation is supported on MX, IX,
and SuperSavage chips.

%package drv-ati
Summary: ATI video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-ati
ati is an Xorg drivers for ATI video cards.

%package drv-nvidia
Summary: NVIDIA video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-nvidia
nvidia is an Xorg driver for NVIDIA video cards. The driver supports 2D
acceleration and provides support for the following framebuffer depths:
8,  15, 16 (except Riva128) and 24.  All visual types are supported for
depth 8, TrueColor and DirectColor visuals are supported for the  other
depths  with the exception of the Riva128 which only supports TrueColor
in the higher depths.

%package drv-i128
Summary: Number 9 I128 video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-i128
i128  is  an  Xorg driver for Number 9 I128 video cards.  The driver is
accelerated and provides support for all versions of the I128 chip fam-
ily,  including the SGI flatpanel configuration.  Multi-head configura-
tions are supported.

%package drv-sis
Summary: SiS video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-sis
sis  is  an  Xorg  driver for SiS (Silicon Integrated Systems) video
chips. The driver is accelerated, and provides support for  colordepths
of 8, 16 and 24 bpp.  XVideo, Render and other extensions are supported
as well.

%package drv-apm
Summary: Alliance ProMotion video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-apm
apm is an Xorg driver for Alliance ProMotion video cards. The driver is
accelerated  for  supported  hardware/depth  combination.  It  supports
framebuffer  depths of 8, 15, 16, 24 and 32 bits. For 6420, 6422, AT24,
AT3D and AT25, all depths are fully accelerated except 24 bpp for which
only screen to screen copy and rectangle filling is accelerated.

%package drv-chips
Summary: Chips and Technologies video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-chips
chips  is  an  Xorg driver for Chips and Technologies video processors.
The majority of the Chips and Technologies chipsets  are  supported  by
this  driver.  In  general  the  limitation on the capabilities of this
driver are determined by the chipset on which it is run.  Where  possi-
ble,  this driver provides full acceleration and supports the following
depths: 1, 4, 8, 15, 16, 24 and on the latest chipsets an 8+16  overlay
mode.  All  visual  types  are  supported for depth 1, 4 and 8 and both
TrueColor and DirectColor visuals are supported where possible.  Multi-
head configurations are supported on PCI or AGP buses.

%package drv-cyrix
Summary: Cyrix video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-cyrix
cyrix  is  an  Xorg  driver  for  the Cyrix MediaGX (now Natsemi Geode)
series of processors when using the built in video.

%package drv-i740
Summary: Intel i740 video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-i740
i740 is an Xorg driver for Intel i740 video cards.

%package drv-i8xx
Summary: Intel 8xx integrated graphics chipsets drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-i8xx
i810  is  an  Xorg  driver for Intel integrated graphics chipsets.  The
driver supports depths 8, 15, 16 and 24.  All  visual  types  are  sup-
ported  in  depth  8.  For the i810/i815 other depths support the True-
Color and DirectColor visuals.  For the 830M and later, only the  True-
Color  visual  is supported for depths greater than 8.  The driver sup-
ports hardware accelerated 3D via the Direct  Rendering  Infrastructure
(DRI),  but only in depth 16 for the i810/i815 and depths 16 and 24 for
the 830M and later.

i810 supports the i810, i810-DC100, i810e,  i815,  830M,  845G,  852GM,
855GM, 865G and 915G chipsets.

%package drv-newport
Summary: Newport video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-newport
newport  is  an  Xorg  driver  for the SGI Indy's and Indigo2's newport
video cards.

%package drv-rendition
Summary: Rendition video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-rendition
rendition  is  an  Xorg  driver for Rendition/Micron based video cards.
The driver supports following framebuffer depths: 8, 15  (Verite  V1000
only),  16  and  24. Acceleration and multi-head configurations are not
supported yet, but are work in progress.

%package drv-s3virge
Summary: S3 ViRGE video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-s3virge
s3virge  is  an  Xorg  driver  for S3 based video cards.  The driver is
fully accelerated, and provides support for the  following  framebuffer
depths: 8, 15, 16, and 24.  All visual types are supported for depth 8,
and TrueColor visuals are supported for the other depths.  XVideo hard-
ware up scaling is supported in depth 16 and 24 on the DX, GX, GX2, MX,
MX+, and Trio3D/2X.  Doublescan modes are supported and tested in depth
8 and 16 on DX, but disable XVideo.  Doublescan modes on other chipsets
are untested.

%package drv-ark
Summary: ARK Logic video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-ark
ark is an Xorg drivers for ARK Logic video cards.

%package drv-imstt
Summary: Integrated Micro Solutions Twin Turbo 128 video driver for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-imstt
imstt  is  an Xorg driver for Integrated Micro Solutions Twin Turbo 128
video chips.
       
%package drv-cirrus
Summary: Cirrus Logic video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-cirrus
cirrus  is  an Xorg driver for Cirrus Logic video chips.

%package drv-mga
Summary: Matrox video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-mga
mga  is  an  Xorg  driver  for Matrox video cards.  The driver is fully
accelerated, and provides support for the following framebuffer depths:
8,  15,  16,  24,  and an 8+24 overlay mode.  All visual types are sup-
ported for depth 8, and both TrueColor and DirectColor visuals are sup-
ported  for  the  other  depths except 8+24 mode which supports Pseudo-
Color, GrayScale and TrueColor.   Multi-card  configurations  are  sup-
ported.   XVideo  is  supported  on G200 and newer systems, with either
TexturedVideo or video overlay.  The second head of dual-head cards  is
supported  for  the G450 and G550.  Support for the second head on G400
cards requires a binary-only "mga_hal" module that  is  available  from
Matrox  <http://www.matrox.com>, and may be on the CD supplied with the
card.  That module also provides various other enhancements, and may be
necessary  to  use  the  DVI  (digital)  output  on the G550 (and other
cards).

%package drv-via
Summary: VIA video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-via
via is an Xorg driver for VIA video chipsets.

The via driver supports the VIA CLE266 (CLE3122, CLE3022) chipset video
and the VIA KM400/K8M800 VT3204/5/7204/5 video, including 2D  accelera-
tion  and  the Xv video overlay extensions. Flat panel, TV and VGA out-
puts are supported.

%package drv-neomagic
Summary: Neomagic video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-neomagic
neomagic  is an Xorg driver for the Neomagic graphics chipsets found in
many laptop computers.

%package drv-nsc
Summary: Nsc video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-nsc
nsc  is an Xorg driver for National Semiconductors GEODE processor fam-
ily.  It uses the DURANGO kit provided by National Semiconductor.   The
driver  is  accelerated,  and provides support for the following frame-
buffer depths: 8, 16 and 24.

%package drv-s3
Summary: S3 video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-s3
s3 is an Xorg driver for S3 video chipsets.

%package drv-siliconmotion
Summary: Silicon Motion video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-siliconmotion
siliconmotion  is  an Xorg driver for Silicon Motion based video cards.
The driver is fully accelerated, and provides support for the following
framebuffer  depths: 8, 16, and 24.  All visual types are supported for
depth 8, and TrueColor visuals are supported for the other depths.

%package drv-tga
Summary: DEC TGA video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-tga
tga is an Xorg driver for DEC TGA video chipsets.

%package drv-trident
Summary: Trident video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-trident
trident  is  an  Xorg  driver  for  Trident video cards.  The driver is
accelerated, and provides support for the following framebuffer depths:
1,  4, 8, 15, 16, and 24. Multi-head configurations are supported.  The
XvImage extension is supported on TGUI96xx and greater cards.

%package drv-tseng
Summary: Tseng Labs video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-tseng
tseng  is  an  Xorg  driver  for Tseng Labs video cards.

%package drv-vmware
Summary: VMware SVGA video drivers for X Window System
Group: System/X11
PreReq: %{name}-server = %{version}-%{release}

%description drv-vmware
vmware is an Xorg driver for VMware virtual video cards.


%package server-common
Summary: The X server common files
Group: System/X11
Requires: %{name}-xauth = %{version}-%{release}
Requires: %{name}-misc-fonts = %{version}-%{release}
Requires: xinitrc >= 2.4.4
#Requires: app-defaults >= 0.2.6

%description server-common
xorg-x11-server-common is common files for X.Org.

%package -n xinitrc
Summary: xinitrc
Group: System/X11

%description -n xinitrc
xinitrc

%package utils
Summary: Utilities for the X Window System version 11 release 6
Group: X11
Requires: %{name}-libs = %{version}-%{release}
Requires: %{name}-font-utils = %{version}-%{release}
Requires: %{name}-xauth = %{version}-%{release}
#Requires: xterm
#Requires: cpp

%description utils
Some useful utilities for the X Window System version 11 release 6.

Install xorg-utils if you are going to work with X.Org.

%package font-utils
Summary: Font utilities required for installing fonts
Group: System/X11
Requires: %{name}-libs = %{version}-%{release}

%description font-utils
Includes mkfontdir, and other font related utilities which are required when
installing font packages.

%package Xprt
Summary: The X print service
Group: System/X11
Requires: %{name}-server-common = %{version}-%{release}

%description Xprt
Xprint is a very flexible, extensible, scaleable,  client/server  print
system  based on ISO 10175 (and some other specs) and the X11 rendering
protocol.  Using Xprint  an  application  can  search,  query  and  use
devices like printers, FAX machines or create documents in formats like
PDF.  In particular, an application can seek a printer, query supported
attributes  (like paper size, trays, fonts etc.), configure the printer
device to match its needs and print on it like on any  other  X  device
reusing parts of the code which is used for the video card Xserver.

%package Xvfb
Summary: A virtual framebuffer X Windows System server for X.Org
Group: System/X11
Requires: %{name}-server-common = %{version}-%{release}

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X Windows System server
that is capable of running on machines with no display hardware and no
physical input devices.  Xvfb emulates a dumb framebuffer using virtual
memory.  Xvfb doesn't open any devices, but behaves otherwise as an X
display.  Xvfb is normally used for testing servers.  Using Xvfb, the mfb
or cfb code for any depth can be exercised without using real hardware
that supports the desired depths.  Xvfb has also been used to test X
clients against unusual depths and screen configurations, to do batch
processing with Xvfb as a background rendering engine, to do load testing,
to help with porting an X server to a new platform, and to provide an
unobtrusive way of running applications which really don't need an X
server but insist on having one.

If you need to test your X server or your X clients, you may want to
install Xvfb for that purpose.

%package Xnest
Summary: A nested X.Org server
Group: System/X11
Requires: %{name}-server-common = %{version}-%{release}

%description Xnest
Xnest is an X Window System server which runs in an X window.
Xnest is a 'nested' window server, actually a client of the
real X server, which manages windows and graphics requests
for Xnest, while Xnest manages the windows and graphics
requests for its own clients.

You will need to install Xnest if you require an X server which
will run as a client of your real X server (perhaps for
testing purposes).

%package Xdmx
Summary: Multi-head X server
Group: System/X11
Requires: %{name}-server = %{version}-%{release}

%description Xdmx
Xdmx  is  a proxy X server that uses one or more other X servers as its
display devices.  It provides multi-head X functionality  for  displays
that  might  be  located  on  different  machines.  Xdmx functions as a
front-end X server that acts as a proxy to a set of back-end X servers.
All  of  the  visible  rendering  is  passed to the back-end X servers.
Clients connect to the Xdmx front-end, and  everything  appears  as  it
would  in  a  regular multi-head configuration.  If Xinerama is enabled
(e.g., with +xinerama on the command line), the clients  see  a  single
large screen.
      
Xdmx communicates to the back-end X servers using the standard X11 pro-
tocol, and standard and/or commonly available X server extensions.

%package sdk
Summary: SDK for X server driver module development
Group: Development/C

%description sdk
The SDK package provides the developmental files which are necessary for
developing X server driver modules, and for compiling driver modules
outside of the standard X11 source code tree.  Developers writing video
drivers, input drivers, or other X modules should install this package.

%package dev
Summary: Include files, development libraries and manual pages for xorg-x11
Group: Development/C
Requires: %{name}-libs = %{version}-%{release}
#Requires: %{name}-mesaGL = %{version}-%{release}
Requires: %{name}-font-utils = %{version}-%{release}
#Requires: %{name}-bitmaps = %{version}-%{release}
#Requires: glibc-dev
#Requires: cpp

%description dev
This package includes the libraries, header files and documentation
you'll need to develop programs which run in X clients. xorg-x11 includes
the base Xlib library as well as the Xt and Xaw widget sets.

For guidance on programming with these libraries, O'Reilly & Associates
produces a series on X programming which you might find useful.

Install this package if you are going to develop programs which
will run as X clients.

%package static-dev
Summary: X11R6 development static libraries
Group: System/Libraries
Requires: xorg-dev = %{version}-%{release}

%description static-dev
This package contains X.Org static libraries needed to
build statically linked programs.

%package fonts
Summary: some missing fonts
Group: System/Fonts/X11 bitmap

%description fonts
fonts

%package cyrillic
Summary: cyrillic fonts
Group: System/Fonts/X11 bitmap

%description cyrillic
cyrillic fonts

%package misc-fonts
Summary: Misc fonts required by the X Window System
Group: System/Fonts/X11 bitmap
#PreReq: chkfontpath
PreReq: %{name}-font-utils

%description misc-fonts
This package provides the misc fonts that are required by the X Window System.

%package type1-fonts
Summary: Type1 fonts required by the X Window System
Group: System/Fonts/X11 bitmap
#PreReq: chkfontpath
PreReq: %{name}-font-utils

%description type1-fonts
This package provides the type1 fonts that are required by the X Window System.

%package 75dpi-fonts
Summary: A set of 75 dpi resolution fonts for the X Window System
Group: System/Fonts/X11 bitmap
#PreReq: chkfontpath
PreReq: %{name}-font-utils

%description 75dpi-fonts
xorg-x11-75dpi-fonts contains the 75 dpi fonts used
on most X Window Systems. If you're going to use the
X Window System, you should install this package, unless
you have a monitor which can support 100 dpi resolution.
In that case, you may prefer the 100dpi fonts available in
the xorg-x11-100dpi-fonts package.

You may also need to install other X.Org font packages.

To install the X Window System, you will need to install
the xorg-x11 package, the xorg-x11 package corresponding to 
your video card, the Xconfigurator package and the
xorg-x11-libs package.

Finally, if you are going to develop applications that run
as X clients, you will also need to install the
xorg-x11-devel package.

%package 75dpi-fonts-unicode
Summary: A set of 75 dpi resolution unicode fonts for the X Window System
Group: System/Fonts/X11 bitmap
#PreReq: chkfontpath
PreReq: %{name}-font-utils

%description 75dpi-fonts-unicode
See 75dpi-fonts

%package 100dpi-fonts-unicode
Summary: A set of 100 dpi resolution unicode fonts for the X Window System
Group: System/Fonts/X11 bitmap
#PreReq: chkfontpath
PreReq: %{name}-font-utils

%description 100dpi-fonts-unicode
See 100dpi-fonts

%package 100dpi-fonts
Summary: X Window System 100dpi fonts
Group: System/Fonts/X11 bitmap
#PreReq: chkfontpath
PreReq: %{name}-font-utils

%description 100dpi-fonts
If you're going to use the X Window System and you have a
high resolution monitor capable of 100 dpi, you should install
xorg-x11-100dpi-fonts. This package contains a set of
100 dpi fonts used on most Linux systems.

If you are installing the X Window System, you will also
need to install the xorg-x11 package, the xorg-x11
package corresponding to your video card, the
Xconfigurator package and the xorg-x11-libs package.
If you need to display certain fonts, you may also need
to install other xorg-x11 fonts packages.

And finally, if you are going to develop applications that
run as X clients, you will also need to install the
xorg-x11-devel package.

%package ttf-fonts
Summary: TrueType fonts provided by the X Window System
Group: System/Fonts/True type
#PreReq: chkfontpath
#PreReq: freetype
PreReq: %{name}-font-utils

%description ttf-fonts
A collection of truetype fonts which are part of the core X Window System
distribution.

##%package speedo-fonts
##Summary: TrueType fonts provided by the X Window System
##Group: System/Fonts/X11 bitmap
##PreReq: chkfontpath, %{name}-font-utils

##%description speedo-fonts
##A collection of Speedo fonts which are part of the core X Window System
##distribution.

%package libGL
Summary: libGL from xorg
Group: System/X11

%description libGL
libGL striped from xorg

%prep
%setup -q -n xc

%build
sed -i -e "s@^#include <linux/config.h>@/* & */@" `grep -lr linux/config.h *`
cat > %{_builddir}/xc/config/cf/host.def << EOF
#define HasFreetype2            YES
#define HasFontconfig           YES
#define HasExpat                YES
#define HasLibpng               YES
#define HasZlib                 YES

#define XFree86CustomVersion	"Los Angeles GNU/Linux build: %{version}-%{release}"

#define BuilderString		"Build Host: evil.los-angeles.org.ua\n"

#define BootstrapCFlags		$RPM_OPT_FLAGS -pipe

#define DefaultGcc2i386Opt	$RPM_OPT_FLAGS -fno-strength-reduce GccAliasingArgs -pipe
#define DefaultGcc2x86_64Opt	$RPM_OPT_FLAGS -fno-strength-reduce GccAliasingArgs -pipe
#define DefaultGcc2AxpOpt	$RPM_OPT_FLAGS -Wa,-m21164a GccAliasingArgs -pipe
#define DefaultGcc2PpcOpt	$RPM_OPT_FLAGS GccAliasingArgs -pipe

#define BuildXterm		NO

#define InstallXdmConfig	NO
#define InstallFSConfig		NO

#undef  DefaultUserPath
#define DefaultUserPath		/usr/local/bin:/bin:/usr/bin
#undef  DefaultSystemPath
#define DefaultSystemPath	/usr/local/sbin:/sbin:/usr/sbin:/bin:/usr/bin

#define AdmDir			/var/log
#define LbxproxyDir		/etc/X11/lbxproxy
#define ProxyManagerDir		/etc/X11/proxymngr
#define ServerConfigDir		/etc/X11/xserver
#define XdmDir			/etc/X11/xdm
#define XConfigDir		/etc/X11
#define XinitDir		/etc/X11/xinit
#define EtcX11Directory		/etc/X11
#define XAppLoadDir		/etc/X11/app-defaults
#define XPrintDir		/etc/X11/xprint

#define XOrgNameString		Los Angeles GNU/Linux X.Org Maintainer Team
#define XOrgWebSupportAddress	http://bugs.los-angeles.org.ua
#define BuilderEMailAddr	"Sectoid_GGV@mail.ru"
#define LinuxDistName		"Los Angeles GNU/Linux"

#define DriverManDir		/usr/X11R6/man/man4
#define DriverManSuffix		4x /* use just one tab or cpp will die */
#define MiscManDir		/usr/X11R6/man/man7
#define MiscManSuffix		7x /* use just one tab or cpp will die */
EOF

%{__make} World %{_smp_mflags}

%install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install
%{__make} DESTDIR=${RPM_BUILD_ROOT} install.man
%{__make} DESTDIR=${RPM_BUILD_ROOT} install.sdk

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/xc

%files
%defattr(-,root,root)
%{_x11libdir}/X11/etc/Xinstall.sh
%{_x11libdir}/X11/etc/sun.termcap
%{_x11libdir}/X11/etc/sun.terminfo

%files utils
%defattr(-,root,root)
%{_sysconfdir}/X11/xkb/
%{_x11bindir}/lbxproxy
%{_x11bindir}/proxymngr
%{_x11bindir}/xfindproxy
%{_x11bindir}/xfwp
%{_x11bindir}/lndir
%{_x11bindir}/luit
%{_x11bindir}/mkdirhier
%{_x11bindir}/appres
%{_x11bindir}/cleanlinks
%{_x11bindir}/dpsexec
%{_x11bindir}/dpsinfo
%{_x11bindir}/gtf
%{_x11bindir}/iceauth
%{_x11bindir}/showrgb
%{_x11bindir}/smproxy
%{_x11bindir}/x11perf
%{_x11bindir}/x11perfcomp
%{_x11bindir}/Xmark
%{_x11bindir}/xcutsel
%{_x11bindir}/xcmsdb
%{_x11bindir}/sessreg
%{_x11bindir}/xdpyinfo
%attr(0755,root,root) %{_x11bindir}/dga
%{_x11bindir}/xhost
%{_x11bindir}/xinit
%{_x11bindir}/setxkbmap
%{_x11bindir}/xkbcomp
%{_x11bindir}/xkbevd
%{_x11bindir}/xkbprint
%{_x11bindir}/xkbvleds
%{_x11bindir}/xkbwatch
%{_x11bindir}/xkbbell
%{_x11bindir}/xlsatoms
%{_x11bindir}/xlsclients
%{_x11bindir}/xlsfonts
%{_x11bindir}/xmessage
%{_x11bindir}/xmodmap
%{_x11bindir}/xprop
%{_x11bindir}/xrdb
%{_x11bindir}/xset
%{_x11bindir}/xrefresh
%{_x11bindir}/xsetmode
%{_x11bindir}/xsetpointer
%{_x11bindir}/xsetroot
%{_x11bindir}/xstdcmap
%{_x11bindir}/xev
%{_x11bindir}/xwd
%{_x11bindir}/xwininfo
%{_x11bindir}/xwud
%{_x11bindir}/xorgconfig
%{_x11bindir}/ico
%{_x11bindir}/listres
%{_x11bindir}/mkhtmlindex
%{_x11bindir}/oclock
%{_x11bindir}/pcitweak
%{_x11bindir}/pswrap
%{_x11bindir}/revpath
%{_x11bindir}/rman
%{_x11bindir}/showfont
%{_x11bindir}/xgamma
%{_x11bindir}/xvinfo
%{_x11bindir}/xrandr
%{_x11bindir}/inb
%{_x11bindir}/inl
%{_x11bindir}/inw
%{_x11bindir}/ioport
%{_x11bindir}/makepsres
%{_x11bindir}/makestrs
%{_x11bindir}/mmapr
%{_x11bindir}/mmapw
%{_x11bindir}/outb
%{_x11bindir}/outl
%{_x11bindir}/outw
%{_x11bindir}/xtrapchar
%{_x11bindir}/xtrapin
%{_x11bindir}/xtrapinfo
%{_x11bindir}/xtrapout
%{_x11bindir}/xtrapproto
%{_x11bindir}/xtrapreset
%{_x11bindir}/xtrapstats
%{_x11bindir}/cxpm
%{_x11bindir}/sxpm
%{_x11bindir}/getconfig
%{_x11bindir}/getconfig.pl
%{_x11mandir}/man1/getconfig.1x*
%{_x11mandir}/man1/cxpm.1x*
%{_x11mandir}/man1/sxpm.1x*
%{_x11mandir}/man1/xrandr.1x*
%{_x11mandir}/man1/xvinfo.1x*
%{_x11mandir}/man1/xgamma.1x*
%{_x11mandir}/man1/showfont.1x*
%{_x11mandir}/man1/rman.1x*
%{_x11mandir}/man1/revpath.1x*
%{_x11mandir}/man1/pswrap.1x*
%{_x11mandir}/man1/pcitweak.1x*
%{_x11mandir}/man1/oclock.1x*
%{_x11mandir}/man1/listres.1x*
%{_x11mandir}/man1/luit.1x*
%{_x11mandir}/man1/ico.1x*
%{_x11mandir}/man1/Xmark.1x*
%{_x11mandir}/man1/dpsexec.1x*
%{_x11mandir}/man1/dpsinfo.1x*
%{_x11mandir}/man1/lbxproxy.1x*
%{_x11mandir}/man1/proxymngr.1x*
%{_x11mandir}/man1/xfindproxy.1x*
%{_x11mandir}/man1/xfwp.1x*
%{_x11mandir}/man1/lndir.1x*
%{_x11mandir}/man1/makestrs.1x*
%{_x11mandir}/man1/mkdirhier.1x*
%{_x11mandir}/man1/appres.1x*
%{_x11mandir}/man1/iceauth.1x*
%{_x11mandir}/man1/showrgb.1x*
%{_x11mandir}/man1/smproxy.1x*
%{_x11mandir}/man1/x11perf.1x*
%{_x11mandir}/man1/x11perfcomp.1x*
%{_x11mandir}/man1/xcutsel.1x*
%{_x11mandir}/man1/xcmsdb.1x*
%{_x11mandir}/man1/sessreg.1x*
%{_x11mandir}/man1/xdpyinfo.1x*
%{_x11mandir}/man1/xev.1x*
%{_x11mandir}/man1/dga.1x*
%{_x11mandir}/man1/xhost.1x*
%{_x11mandir}/man1/xinit.1x*
%{_x11mandir}/man1/startx.1x*
%{_x11mandir}/man1/setxkbmap.1x*
%{_x11mandir}/man1/xkbcomp.1x*
%{_x11mandir}/man1/xkbevd.1x*
%{_x11mandir}/man1/xkbprint.1x*
%{_x11mandir}/man1/xlsatoms.1x*
%{_x11mandir}/man1/xlsclients.1x*
%{_x11mandir}/man1/xlsfonts.1x*
%{_x11mandir}/man1/xmessage.1x*
%{_x11mandir}/man1/xmodmap.1x*
%{_x11mandir}/man1/xprop.1x*
%{_x11mandir}/man1/xrdb.1x*
%{_x11mandir}/man1/xrefresh.1x*
%{_x11mandir}/man1/xset.1x*
%{_x11mandir}/man1/xsetmode.1x*
%{_x11mandir}/man1/xsetpointer.1x*
%{_x11mandir}/man1/xsetroot.1x*
%{_x11mandir}/man1/xstdcmap.1x*
%{_x11mandir}/man1/xwd.1x*
%{_x11mandir}/man1/xwininfo.1x*
%{_x11mandir}/man1/xwud.1x*
%{_x11mandir}/man1/Xserver.1x*
%{_x11mandir}/man1/Xorg.1x*
%{_x11mandir}/man1/cleanlinks.1x*
%{_x11mandir}/man1/gtf.1x*
%{_x11mandir}/man1/makepsres.1x*
%{_x11mandir}/man1/mkhtmlindex.1x*
%{_x11mandir}/man1/xtrap.1x*
%{_x11mandir}/man1/xtrapchar.1x*
%{_x11mandir}/man1/xtrapin.1x*
%{_x11mandir}/man1/xtrapinfo.1x*
%{_x11mandir}/man1/xtrapout.1x*
%{_x11mandir}/man1/xtrapproto.1x*
%{_x11mandir}/man1/xtrapreset.1x*
%{_x11mandir}/man1/xtrapstats.1x*
%{_x11mandir}/man1/xorgconfig.1x*
%{_x11mandir}/man1/dumpkeymap.1x*
%{_x11mandir}/man5/xorg.conf.5x*
%{_x11mandir}/man5/getconfig.5x*
%dir %{_x11libdir}/X11/etc
%{_x11libdir}/X11/etc/xmodmap.std
%{_x11libdir}/X11/x11perfcomp
%{_x11libdir}/X11/lbxproxy
%{_x11libdir}/X11/proxymngr
%{_x11libdir}/X11/getconfig
%dir %{_sysconfdir}/X11/lbxproxy
%dir %{_sysconfdir}/X11/proxymngr
%config(noreplace) %{_sysconfdir}/X11/lbxproxy/*
%config(noreplace) %{_sysconfdir}/X11/proxymngr/*

%files sdk
%defattr(-,root,root)
%{_x11libdir}/Server/

%files dev
%defattr(-,root,root)
%{_x11includedir}/*
%exclude %{_x11includedir}/X11/bitmaps
%exclude %{_x11includedir}/X11/pixmaps
%{_x11mandir}/man3/*
%exclude %{_x11mandir}/man3/DMX*
%{_x11libdir}/X11/config
%{_x11bindir}/imake
%{_x11bindir}/makedepend
%{_x11bindir}/gccmakedep
%{_x11bindir}/ccmakedep
%{_x11bindir}/xmkmf
%{_x11bindir}/makeg
%{_x11bindir}/mergelib
%{_x11bindir}/xcursorgen
%{_x11bindir}/*-config
%{_x11mandir}/man1/makeg.1x*
%{_x11mandir}/man1/imake.1x*
%{_x11mandir}/man1/makedepend.1x*
%{_x11mandir}/man1/xmkmf.1x*
%{_x11mandir}/man1/xcursorgen.1x*
%{_x11mandir}/man1/mergelib.1x*
%{_x11mandir}/man1/ccmakedep.1x*
%{_x11mandir}/man1/gccmakedep.1x*
%{_x11mandir}/man7/XStandards.7x*
%{_x11libdir}/*.so
%exclude %{_x11libdir}/libI810XvMC.so
%{_x11libdir}/pkgconfig/*

%files static-dev
%defattr(-,root,root)
%{_x11libdir}/*.a

%files fonts
%defattr(-,root,root)
%{_x11fontsdir}/local/fonts.dir
%{_x11fontsdir}/CID/fonts.scale
%{_x11fontsdir}/CID/fonts.dir

%files cyrillic
%defattr(-,root,root)
%{_x11fontsdir}/cyrillic/*

%files 75dpi-fonts
%defattr(-,root,root)
%dir %{_x11fontsdir}/75dpi
%{_x11fontsdir}/75dpi/*.gz
%{_x11fontsdir}/75dpi/fonts.alias
%{_x11fontsdir}/75dpi/fonts.dir
%{_x11fontsdir}/75dpi/encodings.dir
%{_x11fontsdir}/75dpi/fonts.scale

%files 100dpi-fonts
%defattr(-,root,root)
%dir %{_x11fontsdir}/100dpi
%{_x11fontsdir}/100dpi/*.gz
%{_x11fontsdir}/100dpi/fonts.alias
%{_x11fontsdir}/100dpi/fonts.dir
%{_x11fontsdir}/100dpi/encodings.dir
%{_x11fontsdir}/100dpi/fonts.scale

%files 75dpi-fonts-unicode
%defattr(-,root,root)

%files 100dpi-fonts-unicode
%defattr(-,root,root)

%files ttf-fonts
%defattr(-,root,root)
%dir %{_x11fontsdir}/TTF
%{_x11fontsdir}/TTF/*.ttf
%{_x11fontsdir}/TTF/fonts.dir
%{_x11fontsdir}/TTF/fonts.scale
%{_x11fontsdir}/TTF/encodings.dir
%{_x11fontsdir}/TTF/fonts.cache-1

%files misc-fonts
%defattr(-,root,root)
%dir %{_x11fontsdir}/misc
%{_x11fontsdir}/misc/*.gz
%{_x11fontsdir}/misc/fonts.alias
%{_x11fontsdir}/misc/fonts.dir
%{_x11fontsdir}/misc/fonts.scale
%{_x11fontsdir}/misc/encodings.dir

%files type1-fonts
%defattr(-,root,root)
%dir %{_x11fontsdir}/Type1
%{_x11fontsdir}/Type1/*.pfa
%{_x11fontsdir}/Type1/*.pfb
%{_x11fontsdir}/Type1/*.afm
%{_x11fontsdir}/Type1/fonts.scale
%{_x11fontsdir}/Type1/fonts.dir
%{_x11fontsdir}/Type1/encodings.dir
%{_x11fontsdir}/Type1/fonts.cache-1

##%files speedo-fonts
##%defattr(-,root,root)
##%dir %{_x11fontsdir}/Speedo
##%{_x11fontsdir}/Speedo/*.spd
##%{_x11fontsdir}/Speedo/fonts.dir
##%{_x11fontsdir}/Speedo/fonts.scale

%files server-common
%defattr(-,root,root)
%dir %{_x11fontsdir}
%{_sysconfdir}/X11/xserver
%{_x11mandir}/man7/Xsecurity.7x*

%files server 
%defattr(-,root,root)
%doc %{_x11libdir}/X11/Cards
%doc %{_x11libdir}/X11/doc
#%%_docdir/%{name}-server-%version
%{_x11bindir}/Xorg
%{_x11bindir}/X
#%%config(noreplace) %{_sysconfdir}/pam.d/xserver
#%%config(missingok noreplace) %{_sysconfdir}/security/console.apps/xserver
%dir %{_x11libdir}/modules
%{_x11libdir}/modules/*.a
%exclude %{_x11libdir}/modules/libscanpci.a
%{_x11libdir}/modules/*.uc
%{_x11libdir}/modules/extensions
%exclude %{_x11libdir}/modules/extensions/libGLcore.a
%exclude %{_x11libdir}/modules/extensions/libglx.a
%dir %{_x11libdir}/modules/dri
%dir %{_x11libdir}/modules/drivers
%{_x11libdir}/modules/drivers/dummy_drv.o
%{_x11libdir}/modules/drivers/fbdev_drv.o
%{_x11libdir}/modules/drivers/vesa_drv.o
%{_x11libdir}/modules/drivers/vga_drv.o
%dir %{_x11libdir}/modules/input
%{_x11libdir}/modules/input/void_drv.o
%{_x11libdir}/modules/input/mouse_drv.o
%{_x11libdir}/modules/input/kbd_drv.o
%{_x11libdir}/modules/input/summa_drv.o
# 6.8.1.99
#%{_x11libdir}/modules/input/evdev_drv.o
#
%{_x11libdir}/modules/linux
%{_x11libdir}/modules/fonts
%{_x11libdir}/X11/xserver
%{_x11bindir}/startx
%{_x11libdir}/X11/xkb
%{_x11libdir}/X11/xinit
#%%{_sysconfdir}/X11/X
%{_iconsdir}/
%{_localstatedir}/lib/xkb
%{_x11mandir}/man4/fbdev.4x*
%{_x11mandir}/man4/fbdevhw.4x*
%{_x11mandir}/man4/vga.4x*
%{_x11mandir}/man4/vesa.4x*
%{_x11mandir}/man4/void.4x*
%{_x11mandir}/man4/mouse.4x*
%{_x11mandir}/man4/kbd.4x*
%{_x11mandir}/man4/glide.4x*
%{_x11mandir}/man4/sun*.4x*
%{_x11mandir}/man7/X.*7x*
%{_x11mandir}/man7/XConsortium.7x*
%{_x11mandir}/man7/XProjectTeam.7x*

%files drv-v4l
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/linux
%{_x11mandir}/man4/v4l.4x*

%files drv-input
%defattr(-,root,root)
%{_x11libdir}/modules/input/linux
%{_x11libdir}/modules/input/acecad_drv.o
%{_x11libdir}/modules/input/digitaledge_drv.o
%{_x11libdir}/modules/input/fpit_drv.o
%{_x11libdir}/modules/input/keyboard_drv.o
%{_x11libdir}/modules/input/spaceorb_drv.o
%{_x11libdir}/modules/input/wacom_drv.o
%{_x11libdir}/modules/input/aiptek_drv.o
%{_x11libdir}/modules/input/dmc_drv.o
%{_x11libdir}/modules/input/hyperpen_drv.o
%{_x11libdir}/modules/input/calcomp_drv.o
%{_x11libdir}/modules/input/dynapro_drv.o
%{_x11libdir}/modules/input/js_x_drv.o
%{_x11libdir}/modules/input/magellan_drv.o
%{_x11libdir}/modules/input/palmax_drv.o
%{_x11libdir}/modules/input/tek4957_drv.o
%{_x11libdir}/modules/input/citron_drv.o
%{_x11libdir}/modules/input/elographics_drv.o
%{_x11libdir}/modules/input/microtouch_drv.o
%{_x11libdir}/modules/input/penmount_drv.o
%{_x11libdir}/modules/input/mutouch_drv.o
%{_x11mandir}/man4/mutouch.4x*
%{_x11mandir}/man4/ur98.4x*
%{_x11mandir}/man4/fpit.4x*
%{_x11mandir}/man4/keyboard.4x*
%{_x11mandir}/man4/wacom.4x*
%{_x11mandir}/man4/aiptek.4x*
%{_x11mandir}/man4/dmc.4x*
%{_x11mandir}/man4/dynapro.4x*
%{_x11mandir}/man4/js_x.4x*
%{_x11mandir}/man4/palmax.4x*
%{_x11mandir}/man4/tek4957.4x*
%{_x11mandir}/man4/citron.4x*
%{_x11mandir}/man4/elographics.4x*
%{_x11mandir}/man4/microtouch.4x*
%{_x11mandir}/man4/penmount.4x*

%files drv-glint
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/glint_drv.o
%{_x11libdir}/modules/dri/gamma_dri.so
%{_x11mandir}/man4/glint.4x*

%files drv-savage
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/savage_drv.o
##%{_x11libdir}/modules/dri/savage_dri.so
%{_x11mandir}/man4/savage.4x*

%files drv-tdfx
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/tdfx_drv.o
%{_x11libdir}/modules/dri/tdfx_dri.so
##%{_x11libdir}/modules/dri/ffb_dri.so
%{_x11mandir}/man4/tdfx.4x*

%files drv-ati
%defattr(-,root,root)
%{_x11libdir}/modules/dri/r128_dri.so
%{_x11libdir}/modules/dri/r200_dri.so
%{_x11libdir}/modules/dri/radeon_dri.so
##%{_x11libdir}/modules/dri/mach64_dri.so
%{_x11libdir}/modules/drivers/ati_drv.o
%{_x11libdir}/modules/drivers/atimisc_drv.o
%{_x11libdir}/modules/drivers/r128_drv.o
%{_x11libdir}/modules/drivers/radeon_drv.o
# 6.8.1.99
#%{_x11libdir}/modules/multimedia
#
%{_x11mandir}/man4/r128.4x*
%{_x11mandir}/man4/radeon.4x*

%files drv-nvidia
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/nv_drv.o
%{_x11libdir}/modules/drivers/riva128.o
%{_x11mandir}/man4/nv.4x*

%files drv-i128
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/i128_drv.o
%{_x11mandir}/man4/i128.4x*

%files drv-sis
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/sis_drv.o
%{_x11libdir}/modules/dri/sis_dri.so
%{_x11mandir}/man4/sis.4x*

%files drv-apm
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/apm_drv.o
%{_x11mandir}/man4/apm.4x*

%files drv-chips
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/chips_drv.o
%{_x11mandir}/man4/chips.4x*

%files drv-cyrix
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/cyrix_drv.o
%{_x11mandir}/man4/cyrix.4x*

%files drv-i740
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/i740_drv.o
%{_x11mandir}/man4/i740.4x*

%files drv-i8xx
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/i810_drv.o
%{_x11libdir}/modules/dri/i810_dri.so
%{_x11libdir}/modules/dri/i915_dri.so
%{_x11libdir}/libI810XvMC.so.*
%{_x11mandir}/man4/i810.4x*

%files drv-newport
%defattr(-,root,root)
##%{_x11libdir}/modules/drivers/newport_drv.o
%{_x11mandir}/man4/newport.4x*

%files drv-rendition
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/rendition_drv.o
%{_x11mandir}/man4/rendition.4x*

%files drv-s3virge
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/s3virge_drv.o
%{_x11mandir}/man4/s3virge.4x*

%files drv-ark
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/ark_drv.o

%files drv-cirrus
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/cirrus_*.o
%{_x11mandir}/man4/cirrus.4x*

%files drv-trident
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/trident_*.o
%{_x11mandir}/man4/trident.4x*

%files drv-imstt
%defattr(-,root,root)
##%{_x11libdir}/modules/drivers/imstt_drv.o
##%{_x11mandir}/man4/imstt.4x*

%files drv-mga
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/mga_drv.o
%{_x11libdir}/modules/dri/mga_dri.so
%{_x11mandir}/man4/mga.4x*

%files drv-via
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/via_drv.o
##%{_x11libdir}/modules/dri/unichrome_dri.so
# 6.8.1.99
#%{_x11libdir}/libviaXvMC.so.*
#
%{_x11mandir}/man4/via.4x*

%files drv-neomagic
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/neomagic_drv.o
%{_x11mandir}/man4/neomagic.4x*

%files drv-nsc
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/nsc_drv.o
%{_x11mandir}/man4/nsc.4x*

%files drv-s3
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/s3_drv.o

%files drv-siliconmotion
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/siliconmotion_drv.o
%{_x11mandir}/man4/siliconmotion.4x*

%files drv-tga
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/tga_drv.o

%files drv-tseng
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/tseng_drv.o
%{_x11mandir}/man4/tseng.4x*

%files drv-vmware
%defattr(-,root,root)
%{_x11libdir}/modules/drivers/vmware_drv.o
%{_x11mandir}/man4/vmware.4x*

%files xapps
%defattr(-,root,root)
%dir %{_sysconfdir}/X11/app-defaults
%config(noreplace) %{_sysconfdir}/X11/app-defaults/*
%exclude %{_sysconfdir}/X11/app-defaults/Chooser
%dir %{_sysconfdir}/X11/xsm
%config(noreplace) %{_sysconfdir}/X11/xsm/system.xsm
%{_x11libdir}/X11/xsm
%{_x11bindir}/beforelight
%{_x11bindir}/bitmap
%{_x11bindir}/bmtoa
%{_x11bindir}/atobm
%{_x11bindir}/xclock
%{_x11bindir}/editres
%{_x11bindir}/viewres
%{_x11bindir}/xcalc
%{_x11bindir}/xfontsel
%{_x11bindir}/xedit
%{_x11libdir}/X11/xedit
%{_x11bindir}/xclipboard
%{_x11bindir}/xconsole
%{_x11bindir}/xload
%{_x11bindir}/xlogo
%{_x11bindir}/xkill
%{_x11bindir}/xsm
%{_x11bindir}/xditview
%{_x11bindir}/xeyes
%{_x11bindir}/xfd
%{_x11bindir}/xgc
%{_x11bindir}/xmag
%{_x11bindir}/xmh
%{_x11bindir}/xvidtune
%{_x11bindir}/xorgcfg
%{_x11bindir}/glxgears
%{_x11bindir}/glxinfo
%{_x11bindir}/texteroids
%{_x11bindir}/xbiff
%{_x11bindir}/xman
%{_x11bindir}/scanpci
%{_x11bindir}/xdriinfo
%{_x11bindir}/xrx
%{_x11mandir}/man1/xvidtune.1x*
%{_x11mandir}/man1/xmh.1x*
%{_x11mandir}/man1/xmag.1x*
%{_x11mandir}/man1/xgc.1x*
%{_x11mandir}/man1/xfd.1x*
%{_x11mandir}/man1/xeyes.1x*
%{_x11mandir}/man1/xditview.1x*
%{_x11mandir}/man1/xsm.1x*
%{_x11mandir}/man1/xkill.1x*
%{_x11mandir}/man1/xlogo.1x*
%{_x11mandir}/man1/xload.1x*
%{_x11mandir}/man1/xconsole.1x*
%{_x11mandir}/man1/xclipboard.1x*
%{_x11mandir}/man1/xedit.1x*
%{_x11mandir}/man1/xfontsel.1x*
%{_x11mandir}/man1/xcalc.1x*
%{_x11mandir}/man1/viewres.1x*
%{_x11mandir}/man1/editres.1x*
%{_x11mandir}/man1/xclock.1x*
%{_x11mandir}/man1/bmtoa.1x*
%{_x11mandir}/man1/atobm.1x*
%{_x11mandir}/man1/bitmap.1x*
%{_x11mandir}/man1/beforelight.1x*
%{_x11mandir}/man1/xorgcfg.1x*
%{_x11mandir}/man1/glxgears.1x*
%{_x11mandir}/man1/texteroids.1x*
%{_x11mandir}/man1/xbiff.1x*
%{_x11mandir}/man1/XDarwin.1x*
%{_x11mandir}/man1/glxinfo.1x*
%{_x11mandir}/man1/libxrx.1x*
%{_x11mandir}/man1/scanpci.1x*
%{_x11mandir}/man1/xdriinfo.1x*
%{_x11mandir}/man1/xman.1x*
%{_x11mandir}/man1/xrx.1x*
%{_x11includedir}/X11/pixmaps
%{_x11libdir}/X11/xman.help
#%exclude %_miconsdir/twm.xpm
#%exclude %_liconsdir/twm.xpm
#%exclude %_iconsdir/twm.xpm
#%_miconsdir/*.xpm
#%_liconsdir/*.xpm
#%_iconsdir/*.xpm
#%_menudir/%{name}-xapps

%files xfs
%defattr(-,root,root)
#%_docdir/%{name}-xfs-%version
#%config %_initdir/xfs
#%config(noreplace) %{_sysconfdir}/sysconfig/xfs
%config(noreplace) %{_sysconfdir}/X11/fs/config
%{_x11libdir}/X11/fs
%{_x11bindir}/xfsinfo
%{_x11bindir}/fslsfonts
%{_x11bindir}/fstobdf
%{_x11bindir}/xfs
%{_x11mandir}/man1/xfs.1x*
%{_x11mandir}/man1/xfsinfo.1x*
%{_x11mandir}/man1/fslsfonts.1x*
%{_x11mandir}/man1/fstobdf.1x*

%files locales
%defattr(-,root,root)
%{_x11libdir}/X11/locale

%files -n twm
%defattr(-,root,root)
%dir %{_sysconfdir}/X11/twm
%config(noreplace) %{_sysconfdir}/X11/twm/system.twmrc
%{_x11libdir}/X11/twm
%{_x11mandir}/man1/twm.1x*
%{_x11bindir}/twm
#%_menudir/twm
#%_miconsdir/twm.xpm
#%_liconsdir/twm.xpm
#%_iconsdir/twm.xpm

%files font-utils
%defattr(-,root,root)
%{_x11bindir}/bdftopcf
%{_x11bindir}/bdftruncate
%{_x11bindir}/mkfontdir
%{_x11bindir}/mkfontscale
%{_x11bindir}/mkcfm
%{_x11bindir}/ucs2any
%{_x11fontsdir}/util
%{_x11fontsdir}/encodings
%{_x11mandir}/man1/bdftopcf.1x*
%{_x11mandir}/man1/bdftruncate.1x*
%{_x11mandir}/man1/mkfontdir.1x*
%{_x11mandir}/man1/mkfontscale.1x*
%{_x11mandir}/man1/mkcfm.1x*
%{_x11mandir}/man1/ucs2any.1x*

%files libs
%defattr(-,root,root)
%{_x11libdir}/X11/Options
%{_x11libdir}/X11/XErrorDB
%{_x11libdir}/X11/XKeysymDB
%{_x11libdir}/X11/rgb.txt
%{_x11libdir}/X11/Xcms.txt
%{_x11libdir}/*.so.*
# do not include libGL*.so.1* in this package
# it in `xorg-libGL' package
%exclude %{_x11libdir}/libGL*.so.1*
%exclude %{_x11libdir}/libOSMesa.so.*
# 6.8.1.99
#%exclude %{_x11libdir}/libviaXvMC.so.*
#
%exclude %{_x11libdir}/libI810XvMC.so.*
#%{_sysconfdir}/ld.so.conf.d/X11R6.conf

%files Xprt
%defattr(-,root,root)
%{_sysconfdir}/init.d/xprint
%{_sysconfdir}/profile.d/xprint.csh
%{_sysconfdir}/profile.d/xprint.sh
%{_sysconfdir}/X11/Xsession.d/92xprint-xpserverlist.sh
%{_x11bindir}/Xprt
%{_x11bindir}/xphelloworld
%{_x11bindir}/xplsprinters
%{_x11bindir}/xprehashprinterlist
%{_x11bindir}/xpsimplehelloworld
%{_x11bindir}/xpxthelloworld
# 6.8.1.99
#%{_x11bindir}/xpr
#%{_x11bindir}/xdpr
#%{_x11bindir}/xdbedizzy
#%{_x11bindir}/pclcomp
#
%{_x11bindir}/xmore
%{_x11mandir}/man1/xphelloworld.1x*
%{_x11mandir}/man1/xplsprinters.1x*
# 6.8.1.99
#%{_x11mandir}/man1/xpr.1x*
#%{_x11mandir}/man1/xdbedizzy.1x*
#%{_x11mandir}/man1/pclcomp.1x*
#%{_x11mandir}/man1/xdpr.1x*
#
%{_x11mandir}/man1/Xprt.1x*
%{_x11mandir}/man1/xmore.1x*
%{_x11mandir}/man1/xprehashprinterlist.1x*
%{_x11mandir}/man1/xpsimplehelloworld.1x*
%{_x11mandir}/man1/xpxthelloworld.1x*
%{_x11mandir}/man7/Xprint.7x*
%{_sysconfdir}/X11/xprint

%files Xvfb
%defattr(-,root,root)
%{_x11bindir}/Xvfb
%{_x11mandir}/man1/Xvfb.1x*

%files Xnest
%defattr(-,root,root)
%{_x11bindir}/Xnest
%{_x11mandir}/man1/Xnest.1x*

%files Xdmx
%defattr(-,root,root)
%{_x11bindir}/Xdmx
#%{_x11bindir}/xdmxconfig
#%{_x11bindir}/dmxtodmx
#%{_x11bindir}/vdltodmx
%{_x11mandir}/man1/Xdmx.1x*
%{_x11mandir}/man1/dmxtodmx.1x*
%{_x11mandir}/man1/vdltodmx.1x*
%{_x11mandir}/man1/xdmxconfig.1x*
%{_x11mandir}/man3/DMX*

%files rstart
%defattr(-,root,root)
%{_sysconfdir}/X11/rstart
%{_x11libdir}/X11/rstart
%config(noreplace) %{_sysconfdir}/X11/rstart/config
%{_x11bindir}/rstart
%{_x11bindir}/rstartd
%{_x11bindir}/xon
%{_x11mandir}/man1/rstart.1x*
%{_x11mandir}/man1/rstartd.1x*
%{_x11mandir}/man1/xon.1x*

%files xdm
%defattr(-,root,root)
#%config(noreplace) %{_sysconfdir}/logrotate.d/xdm
#%config(noreplace) %{_sysconfdir}/pam.d/xdm
%dir %{_sysconfdir}/X11/app-defaults
%config(noreplace) %{_sysconfdir}/X11/app-defaults/Chooser
%dir %attr(0700,root,root) %{_sysconfdir}/X11/xdm/authdir
%config(noreplace) %{_sysconfdir}/X11/xdm/*
%{_sysconfdir}/X11/xdm/pixmaps/*.xpm
%{_x11bindir}/xdm
#%{_x11bindir}/chooser
%{_x11libdir}/X11/xdm
%{_x11mandir}/man1/xdm.1x*
%dir %{_localstatedir}/lib/xdm

%files xauth
%defattr(-,root,root)
%{_x11bindir}/xauth
%{_x11mandir}/man1/xauth.1*

%files -n xinitrc
%defattr(-,root,root)
%{_sysconfdir}/X11/xinit/

%files libGL
%defattr(-,root,root)
%{_x11libdir}/libGL*.so.1*

%changelog
* Wed Mar 3 2005 Gleb Golubitsky (Sectoid) <Sectoid_GGV@mail.ru> 6.8.2-los1
- Initial build for Los Angeles GNU/Linux.
