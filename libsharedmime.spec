Summary:	Reads the Shared Mime Info database
Summary(pl.UTF-8):	Biblioteka czytająca bazę Shared Mime Info
Name:		libsharedmime
Version:	0.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.memecode.com/src/%{name}-%{version}.tar.bz2
# Source0-md5:	5f561b51e42b1719955447f21eb715b2
URL:		http://www.memecode.com/libsharedmime.php
Patch0:		%{name}-destdir.patch
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library reads the freedesktop Shared Mime Info database and
returns you the MIME-TYPE of a file.

%description -l pl.UTF-8
Biblioteka odczytuje informacje z bazy Shared Mime Info
(freedesktop.org) i zwraca typ MIME pliku.

%package devel
Summary:	Header files for libsharedmime library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsharedmime
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libsharedmime library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsharedmime.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/mime-types.h
