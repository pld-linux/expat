Summary:	XML 1.0 parser
Summary(es):	Parser de XML 1.0
Summary(pl):	Analizator sk�adni XML-a 1.0
Summary(pt_BR):	Biblioteca XML expat
Summary(ru):	����������� ���������� ������� XML (expat)
Summary(uk):	���������� ¦�̦����� ������� XML (expat)
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
al est�ndar. Actualmente no es un parser XML validante.

%description -l pl
Expat to napisany w j�zyku C analizator sk�adni XML-a. D��y do pe�nej
zgodno�ci ze specyfikacj�. Aktualnie nie jest analizatorem, kt�ry
potwiedza� by zgodno�� ze specyfikacj�.

%description -l pt_BR
Esta � a biblioteca, em C, XML expat, de James Clark. � um analisador
orientado a fluxo de informa��es que pede o uso de handlers para lidar
com a estrutura que o analisador encontrar no documento.

%description -l ru
Expat -- ������ XML 1.0, ���������� �� C. �� ������������ ��� ����,
����� ���� ��������� �����������. � ��������� ����� ��� �� �����������
("not a validating") XML ������.

%description -l uk
Expat -- ������ XML 1.0, ��������� �� C. ������������ �� ��, ��� ����
���Φ��� ��ͦ����. ����ڦ �� �� ����צ������ ("not a validating") XML
������.

%package devel
Summary:	Expat header files
Summary(es):	Archivos de inclusi�n del expat
Summary(pl):	Pliki nag��wkowe do biblioteki expat
Summary(pt_BR):	Arquivos de inclus�o do expat
Summary(ru):	������ � ����������, ����������� ��� ���������������� � expat
Summary(uk):	������ �� ¦�̦�����, ����Ȧ�Φ ��� ������������� � expat
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libexpat1_95-devel

%description devel
Expat header files.

%description devel -l es
Archivos de inclusi�n del expat.

%description devel -l pl
Pliki nag��wkowe do biblioteki expat.

%description devel -l pt_BR
Arquivos de inclus�o do expat.

%description devel -l ru
���� ����� �������� ������ � ����������, ����������� ��� ���������
��������, ������������ libexpat.

%description devel -l uk
��� ����� ͦ����� ������ �� ¦�̦�����, ����Ȧ�Φ ��� ���������
�������, �� �������������� libexpat.

%package static
Summary:	Expat static library
Summary(es):	Biblioteca est�tica de expat
Summary(pl):	Biblioteka statyczna expat
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a biblioteca expat
Summary(ru):	����������� ���������� ��� ���������������� � libexpat
Summary(uk):	�������� ¦�̦����� ��� ������������� � libexpat
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description static
Expat static library.

%description static -l es
Biblioteca est�tica de expat.

%description static -l pl
Biblioteka statyczna expat.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com a biblioteca expat.

%description static -l ru
���� ����� �������� ����������� ����������, ����������� ��� ���������
��������, ������������ libexpat.

%description static -l uk
��� ����� ͦ����� �������� ¦�̦�����, ����Ȧ��� ��� ���������
�������, �� �������������� libexpat.

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
