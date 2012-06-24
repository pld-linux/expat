Summary:	XML 1.0 parser
Summary(es):	expat XML library
Summary(pl):	XML 1.0 parser
Summary(pt_BR):	Biblioteca XML expat
Name:		expat
Version:	1.95.2
Release:	3
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Group(cs):	Aplikace/Publikov�n�/XML
Group(da):	Programmer/Udgivelse/XML
Group(de):	Applikationen/Publizieren/XML
Group(es):	Aplicaciones/Edici�n/XML
Group(fr):	Applications/Edition/XML
Group(is):	Forrit/Umbrot/XML
Group(it):	Applicazioni/Publishing/XML
Group(ja):	���ץꥱ�������/�ѥ֥�å���/XML
Group(no):	Applikasjoner/Publisering/XML
Group(pl):	Aplikacje/Publikowanie/XML
Group(pt):	Aplica��es/Publica��o/XML
Group(pt_BR):	Aplica��es/Editora��o/XML
Group(ru):	����������/������������/XML
Group(sl):	Programi/Zalo�ni�tvo/XML
Group(sv):	Till�mpningar/Publicering/XML
Group(uk):	�������Φ ��������/�������Ʀ�/XML
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

%description -l es
This is James Clark's expat XML parser library in C. It is a stream
oriented parser that requires setting handlers to deal with the
structure that the parser discovers in the document.

%description -l pl
Expat to parser XML napisany w j�zyku C.

%description -l pt_BR
Esta � a biblioteca, em C, XML expat, de James Clark. � um analisador
orientado a fluxo de informa��es que pede o uso de handlers para lidar
com a estrutura que o analisador encontrar no documento.

%package devel
Summary:	Expat header files
Summary(es):	Archivos de inclusi�n del expat
Summary(pl):	Pliki nag��wkowe do biblioteki expat
Summary(pt_BR):	Arquivos de inclus�o do expat
Group:		Development/Libraries
Group(cs):	V�vojov� prost�edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	�r�unart�l/A�ger�as�fn
Group(it):	Sviluppo/Librerie
Group(ja):	��ȯ/�饤�֥��
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(sl):	Razvoj/Knji�nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}
Obsoletes:	libexpat1_95-devel

%description devel
Expat header files.

%description devel -l es
Archivos de inclusi�n del expat

%description devel -l pl
Pliki nag��wkowe do biblioteki expat.

%description devel -l pt_BR
Arquivos de inclus�o do expat

%package static
Summary:	Expat static library
Summary(es):	Expat static libs
Summary(pl):	Biblioteka statyczna expat
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a biblioteca expat
Group:		Development/Libraries
Group(cs):	V�vojov� prost�edky/Knihovny
Group(da):	Udvikling/Biblioteker
Group(de):	Entwicklung/Bibliotheken
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(is):	�r�unart�l/A�ger�as�fn
Group(it):	Sviluppo/Librerie
Group(ja):	��ȯ/�饤�֥��
Group(no):	Utvikling/Bibliotek
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(pt):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(sl):	Razvoj/Knji�nice
Group(sv):	Utveckling/Bibliotek
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description static
Expat static library.

%description static -l es
Expat static libs

%description static -l pl
Bioblioteka statyczna expat.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com a biblioteca expat

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
