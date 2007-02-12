Summary:	XML 1.0 parser
Summary(es.UTF-8):	Parser de XML 1.0
Summary(pl.UTF-8):	Analizator składni XML-a 1.0
Summary(pt_BR.UTF-8):	Biblioteca XML expat
Summary(ru.UTF-8):	Переносимая библиотека разбора XML (expat)
Summary(uk.UTF-8):	Переносима бібліотека розбору XML (expat)
Name:		expat
Version:	2.0.0
Release:	3
Epoch:		1
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/expat/%{name}-%{version}.tar.gz
# Source0-md5:	d945df7f1c0868c5c73cf66ba9596f3f
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-am18.patch
Patch2:		%{name}-soname.patch
URL:		http://expat.sourceforge.net/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
Obsoletes:	libexpat1_95
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Expat is an XML parser written in C. It aims to be fully conforming.
It is currently not a validating XML parser.

%description -l es.UTF-8
Expat es un parser de XML escrito en C. Pretende conformarse totalmente
al estándar. Actualmente no es un parser XML validante.

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libexpat1_95-devel

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
Requires:	%{name} = %{epoch}:%{version}-%{release}

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
