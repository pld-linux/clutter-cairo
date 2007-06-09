#
Summary:	Library integrating clutter with Cairo
Name:		clutter-cairo
Version:	0.1.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://www.clutter-project.org/sources/clutter-cairo/0.1/%{name}-%{version}.tar.gz
# Source0-md5:	69e65f708399802ffce434716ea7714e
URL:		http://www.clutter-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel
BuildRequires:	cairo-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clutter is an open source software library for creating fast, visually
rich graphical user interfaces. The most obvious example of potential
usage is in media center type applications. We hope however it can be
used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but
with an API which hides the underlying GL complexity from the
developer. The Clutter API is intended to be easy to use, efficient
and flexible.

%package devel
Summary:	Header files for clutter-cairo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki clutter-cairo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for clutter-cairo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki clutter-cairo.

%package static
Summary:	Static clutter-cairo library
Summary(pl.UTF-8):	Statyczna biblioteka clutter-cairo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static clutter-cairo library.

%description static -l pl.UTF-8
Statyczna biblioteka clutter-cairo.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/clutter-*
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
