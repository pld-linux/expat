Summary:	XML 1.0 parser
Summary(pl):	Parser XML 1.0
Summary(pt_BR):	Biblioteca XML expat
Summary(ru):	Переносимая библиотека разбора XML (expat)
Summary(uk):	Переносима б╕бл╕отека розбору XML (expat)
Name:		expat
Version:	1.95.3
Release:	3
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/expat/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://expat.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libexpat1_95

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

%description -l pl
Expat to parser XML napisany w jЙzyku C.

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
Requires:	%{name} = %{version}
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
Summary(pl):	Biblioteka statyczna expat
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com a biblioteca expat
Summary(ru):	Статическая библиотека для программирования с libexpat
Summary(uk):	Статична б╕бл╕отека для програмування з libexpat
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Expat static library.

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
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc Changes COPYING README doc/{reference.html,style.css}
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
