Summary:	XML 1.0 parser
Summary(pl):	Parser XML 1.0
Summary(pt_BR):	Biblioteca XML expat
Summary(ru):	����������� ���������� ������� XML (expat)
Summary(uk):	���������� ¦�̦����� ������� XML (expat)
Name:		expat
Version:	1.95.6
Release:	5
Epoch:		1
License:	Thai Open Source Software Center Ltd (distributable)
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/expat/%{name}-%{version}.tar.gz
# Source0-md5: ca78d94e83e9f077b5da2bfe28ba986a
Source1:	%{name}.m4
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-gcc3-c++.patch
Patch2:		%{name}-ac_fixes.patch
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
Expat to parser XML napisany w j�zyku C.

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
Requires:	%{name} = %{epoch}:%{version}
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
Summary(pl):	Biblioteka statyczna expat
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com a biblioteca expat
Summary(ru):	����������� ���������� ��� ���������������� � libexpat
Summary(uk):	�������� ¦�̦����� ��� ������������� � libexpat
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description static
Expat static library.

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
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_aclocaldir}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING Changes README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc doc/{reference.html,style.css}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
