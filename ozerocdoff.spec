%define __debug_package %nil
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Tool for switching modes of Option USB devices
Name:		ozerocdoff
Version:	0.4
Release:	11
Group:		System/Base
License:	GPLv2
Url:		https://www.pharscape.org/ozerocdoff.html
Source0:	ozerocdoff-%{version}.tar.bz2
Patch0:		ozerocdoff-mda.patch
Patch1:		ozerocdoff-0.4-udev.patch
BuildRequires:	pkgconfig(libusb)
Obsoletes:		hso-rezero

%description
Ozerocdoff - an improved ZeroCD switching utility

This is the improved Option software for temporarily disabling ZeroCD
and allowing the modem to be a modem. It has replaced rezero.

%prep
%setup -q
%autopatch -p1

%build
%make

%install
LIBNAME=%{_lib} %makeinstall_std
ln -s ozerocdoff %{buildroot}%{_sbindir}/rezero

%files
%{_sysconfdir}/udev/rules.d/49-hso-udev.rules
%config(noreplace) %attr(0644,root,root) /etc/hso-suspend.conf
%{_sbindir}/ozerocdoff
%{_sbindir}/rezero
%{_sbindir}/osetsuspend
%{_libdir}/hal/scripts/hal-serial-hsotype
%{_datadir}/hal/fdi/preprobe/20thirdparty/10-wwan-hso-preprobe.fdi
%{_datadir}/hal/fdi/information/20thirdparty/10-wwan-quirk.fdi
