Summary:	XML 1.0 parser
Summary(pl):	XML 1.0 parser
Name:		expat
Version:	1.95.2
Release:	2
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Group(de):	Applikationen/Publizieren/XML
Group(pl):	Aplikacje/Publikowanie/XML
Source0:	ftp://download.sourceforge.net/pub/sourceforge/expat/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fix.patch
URL:		http://expat.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libexpat1_95

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

%description -l pl
Expat to parser XML napisany w jêzyku C.

%package devel
Summary:	Expat header files
Summary(pl):	Pliki nag³ówkowe do biblioteki expat
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	libexpat1_95-devel

%description devel
Expat header files.

%description -l pl devel
Pliki nag³ówkowe do biblioteki expat.

%package static
Summary:	Expat static library
Summary(pl):	Biblioteka statyczna expat
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description static
Expat static library.

%description -l pl static
Bioblioteka statyczna expat.

%prep
%setup -q
%patch0 -p1

%build
libtoolize --copy --force
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes COPYING README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
