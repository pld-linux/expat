Summary:	XML 1.0 parser
Summary(pl):	XML 1.0 parser
Name:		expat
Version:	1.1
Release:	1
URL:		http://www.jclark.com/xml/expat.html
Source0:	ftp://ftp.jclark.com/pub/xml/%{name}.zip
Patch0:		expat.patch
License:	GPL
Group:		Applications/Publishing/XML
Group(pl):	Aplikacje/Publikowanie/XML
##Provides:	xmlmf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expat is an XML 1.0 parser written in C. It aims to be fully
conforming. It is currently not a validating XML parser.

%description -l pl
Expat to parser XML 1.0 napisany w jêzyku C.

%package devel
Summary:	%{name} header files
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
%{name} header files.

%description -l pl devel
Pliki nag³ówkowe %{name}.

%prep
%setup -q -T -c
unzip -qa %{SOURCE0}
mv %{name}/* . && rmdir %{name}
chmod -R a+rX *
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS %{?debug:-g -O}"; export CFLAGS
%{__make} libexpat.a
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}
install libexpat.a $RPM_BUILD_ROOT%{_libdir}
install xmlwf/xmlwf  $RPM_BUILD_ROOT%{_bindir}
install xmlparse/xmlparse.h  $RPM_BUILD_ROOT%{_includedir}
%{!?debug:strip $RPM_BUILD_ROOT%{_bindir}/*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.a
