Name:		ozerocdoff
Version:	0.4
Release:	%mkrel 1.1
Summary:	Tool for switching modes of Option USB devices
Group:		System/Base
License:	GPL
URL:		http://www.pharscape.org/ozerocdoff.html
Source0:	ozerocdoff-%{version}.tar.bz2
Patch0:		ozerocdoff-mda.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  usb-compat-devel

Obsoletes:      hso-rezero

%description
Ozerocdoff - an improved ZeroCD switching utility
This is the improved Option software for temporarily disabling ZeroCD and allowing the modem to be a modem. It has replaced rezero.

%prep
%setup -q
%patch0 -p1

%build
%make


%install
%__rm -rf %buildroot
LIBNAME=%{_lib} %makeinstall_std
%__ln_s ozerocdoff %{buildroot}%{_sbindir}/rezero


%post


%preun


%clean
%__rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%_sbindir/ozerocdoff
%_sbindir/rezero
%_sbindir/osetsuspend

%_sysconfdir/udev/rules.d/49-hso-udev.rules

%{_libdir}/hal/scripts/hal-serial-hsotype
%{_datadir}/hal/fdi/preprobe/20thirdparty/10-wwan-hso-preprobe.fdi
%{_datadir}/hal/fdi/information/20thirdparty/10-wwan-quirk.fdi

%config(noreplace) %attr(0644,root,root) /etc/hso-suspend.conf

%doc
