Summary:	XML 1.0 parser
Summary(es):	Parser de XML 1.0
Summary(pl):	Analizator skЁadni XML-a 1.0
Summary(pt_BR):	Biblioteca XML expat
Summary(ru):	Переносимая библиотека разбора XML (expat)
Summary(uk):	Переносима б╕бл╕отека розбору XML (expat)
Name:		expat
Version:	2.0.0
Release:	1
Epoch:		1
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/expat/%{name}-%{version}.tar.gz
# Source0-md5:	d945df7f1c0868c5c73cf66ba9596f3f
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-am18.patch
URL:		http://expat.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
Obsoletes:	libexpat1_95
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

%description -l es
Expat es un parser de XML escrito en C. Pretende conformarse totalmente
al estАndar. Actualmente no es un parser XML validante.

%description -l pl
Expat to napisany w jЙzyku C analizator skЁadni XML-a. D╠©y do peЁnej
zgodno╤ci ze specyfikacj╠. Aktualnie nie jest analizatorem, ktСry
potwiedzaЁ by zgodno╤Ф ze specyfikacj╠.

%description -l pt_BR
Esta И a biblioteca, em C, XML expat, de James Clark. и um analisador
orientado a fluxo de informaГУes que pede o uso de handlers para lidar
com a estrutura que o analisador encontrar no documento.

%description -l ru
Expat -- парсер XML 1.0, написанный на C. Он предназначен для того,
чтобы быть полностью совместимым. В настоящее время это не проверяющий
("not a validating") XML парсер.

%description -l uk
Expat -- парсер XML 1.0, написаний на C. Розрахований на те, щоб бути
повн╕стю сум╕сним. Нараз╕ це не перев╕ряючий ("not a validating") XML
парсер.

%package devel
Summary:	Expat header files
Summary(es):	Archivos de inclusiСn del expat
Summary(pl):	Pliki nagЁСwkowe do biblioteki expat
Summary(pt_BR):	Arquivos de inclusЦo do expat
Summary(ru):	Хедеры и библиотека, необходимые для программирования с expat
Summary(uk):	Хедери та б╕бл╕отека, необх╕дн╕ для програмування з expat
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libexpat1_95-devel

%description devel
Expat header files.

%description devel -l es
Archivos de inclusiСn del expat.

%description devel -l pl
Pliki nagЁСwkowe do biblioteki expat.

%description devel -l pt_BR
Arquivos de inclusЦo do expat.

%description devel -l ru
Этот пакет содержит хедеры и библиотеки, необходимые для написания
программ, использующих libexpat.

%description devel -l uk
Цей пакет м╕стить хедери та б╕бл╕отеки, необх╕дн╕ для написання
програм, що використовують libexpat.

%package static
Summary:	Expat static library
Summary(es):	Biblioteca estАtica de expat
Summary(pl):	Biblioteka statyczna expat
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com a biblioteca expat
Summary(ru):	Статическая библиотека для программирования с libexpat
Summary(uk):	Статична б╕бл╕отека для програмування з libexpat
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description static
Expat static library.

%description static -l es
Biblioteca estАtica de expat.

%description static -l pl
Biblioteka statyczna expat.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com a biblioteca expat.

%description static -l ru
Этот пакет содержит статическую библиотеку, необходимую для написания
программ, использующих libexpat.

%description static -l uk
Цей пакет м╕стить статичну б╕бл╕отеку, необх╕дну для написання
програм, що використовують libexpat.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_aclocaldir}
install conftools/expat.m4 $RPM_BUILD_ROOT%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING Changes README
%attr(755,root,root) %{_bindir}/xmlwf
%attr(755,root,root) %{_libdir}/libexpat.so.*.*
%{_mandir}/man1/xmlwf.1*

%files devel
%defattr(644,root,root,755)
%doc doc/{reference.html,style.css}
%attr(755,root,root) %{_libdir}/libexpat.so
%{_libdir}/libexpat.la
%{_includedir}/expat*.h
%{_aclocaldir}/expat.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libexpat.a
