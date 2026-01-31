#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	XML 1.0 parser
Summary(es.UTF-8):	Parser de XML 1.0
Summary(pl.UTF-8):	Analizator składni XML-a 1.0
Summary(pt_BR.UTF-8):	Biblioteca XML expat
Summary(ru.UTF-8):	Переносимая библиотека разбора XML (expat)
Summary(uk.UTF-8):	Переносима бібліотека розбору XML (expat)
Name:		expat
Version:	2.7.4
Release:	1
Epoch:		1
License:	MIT
Group:		Applications/Publishing/XML
Source0:	https://downloads.sourceforge.net/expat/%{name}-%{version}.tar.xz
# Source0-md5:	5d3d1e1c829f8fb6f42b8e3e2371afa3
URL:		http://www.libexpat.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	docbook2X
BuildRequires:	gcc >= 5:3.2
BuildRequires:	glibc-headers >= 6:2.36
BuildRequires:	libtool >= 2:2.4
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	libexpat1_95 < 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

%description -l es.UTF-8
Expat es un parser de XML escrito en C. Pretende conformarse
totalmente al estándar. Actualmente no es un parser XML validante.

%description -l pl.UTF-8
Expat to napisany w języku C analizator składni XML-a. Dąży do pełnej
zgodności ze specyfikacją. Aktualnie nie jest analizatorem, który
potwiedzał by zgodność ze specyfikacją.

%description -l pt_BR.UTF-8
Esta é a biblioteca, em C, XML expat, de James Clark. É um analisador
orientado a fluxo de informações que pede o uso de handlers para lidar
com a estrutura que o analisador encontrar no documento.

%description -l ru.UTF-8
Expat -- парсер XML 1.0, написанный на C. Он предназначен для того,
чтобы быть полностью совместимым. В настоящее время это не проверяющий
("not a validating") XML парсер.

%description -l uk.UTF-8
Expat -- парсер XML 1.0, написаний на C. Розрахований на те, щоб бути
повністю сумісним. Наразі це не перевіряючий ("not a validating") XML
парсер.

%package devel
Summary:	Expat header files
Summary(es.UTF-8):	Archivos de inclusión del expat
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki expat
Summary(pt_BR.UTF-8):	Arquivos de inclusão do expat
Summary(ru.UTF-8):	Хедеры и библиотека, необходимые для программирования с expat
Summary(uk.UTF-8):	Хедери та бібліотека, необхідні для програмування з expat
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	libexpat1_95-devel < 2

%description devel
Expat header files.

%description devel -l es.UTF-8
Archivos de inclusión del expat.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki expat.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão do expat.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры и библиотеки, необходимые для написания
программ, использующих libexpat.

%description devel -l uk.UTF-8
Цей пакет містить хедери та бібліотеки, необхідні для написання
програм, що використовують libexpat.

%package static
Summary:	Expat static library
Summary(es.UTF-8):	Biblioteca estática de expat
Summary(pl.UTF-8):	Biblioteka statyczna expat
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com a biblioteca expat
Summary(ru.UTF-8):	Статическая библиотека для программирования с libexpat
Summary(uk.UTF-8):	Статична бібліотека для програмування з libexpat
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description static
Expat static library.

%description static -l es.UTF-8
Biblioteca estática de expat.

%description static -l pl.UTF-8
Biblioteka statyczna expat.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com a biblioteca expat.

%description static -l ru.UTF-8
Этот пакет содержит статическую библиотеку, необходимую для написания
программ, использующих libexpat.

%description static -l uk.UTF-8
Цей пакет містить статичну бібліотеку, необхідну для написання
програм, що використовують libexpat.

%package tools
Summary:	Expat utilities (xmlwf)
Summary(pl.UTF-8):	Programy narzędziowe do biblioteki Expat (xmlwf)
Group:		Applications/Text
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description tools
Expat utilities:
- xmlwf: determines if an XML document is well-formed.

%description tools -l pl.UTF-8
Programy narzędziowe do biblioteki Expat:
- xmlwf: sprawdza, czy dokument XML jest dobrze sformułowany.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# remove SIZEOF_VOID_P define, see buildconf.sh
%{__sed} -i -e '/^\/\* The size of `void \*/,/^$/ d' expat_config.h.in
%configure \
	DOCBOOK_TO_MAN=docbook2X2man \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_aclocaldir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING Changes README.md
%attr(755,root,root) %{_libdir}/libexpat.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexpat.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/{reference.html,style.css}
%attr(755,root,root) %{_libdir}/libexpat.so
%{_libdir}/libexpat.la
%{_includedir}/expat*.h
%{_pkgconfigdir}/expat.pc
%{_libdir}/cmake/expat-%{version}
%{_examplesdir}/%{name}-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libexpat.a
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmlwf
%{_mandir}/man1/xmlwf.1*
