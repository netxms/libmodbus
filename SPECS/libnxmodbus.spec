# vim: ts=3 sw=3 expandtab
Summary:       Fork of libmodbus
Name:          libnxmodbus
Version:       3.1.10
Release:       5%{?dist}
License:       LGPLv2+
URL:           https://github.com/netxms/libmodbus
Group:         Applications/System
Source0:       %{name}-%{version}.tar.gz

Conflicts:     libmodbus
Conflicts:     libmodbus-devel

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
This is a fork of http://libmodbus.org/. Main reason for this fork - original author
does not accept pull requests and fixes.

%prep
%setup -q

aclocal
automake --add-missing
autoreconf

%build

%configure
make %{?_smp_mflags}

%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%exclude %{_libdir}/*.la
%{_libdir}/libnxmodbus.so.*

%doc
%{_docdir}/libnxmodbus/AUTHORS
%{_docdir}/libnxmodbus/NEWS
%{_docdir}/libnxmodbus/README.md

%package devel
Summary: Development files for libnxmodbus
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development package for libnxmodbus

%files devel
%{_includedir}/modbus/
%{_libdir}/pkgconfig/libnxmodbus.pc
%{_libdir}/libnxmodbus.so

%changelog
* Tue Jul 25 2023 Alex Kirhenshtein <alk@netxms.org> - 3.1.10-4
- Initial release
