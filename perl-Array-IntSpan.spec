#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Array
%define	pnam	IntSpan
Summary:	Array::IntSpan - a Module for handling arrays using IntSpan techniques
Summary(pl):	Array::IntSpan - modu³ do obs³ugi tablic z u¿yciem techniki IntSpan
Name:		perl-%{pdir}-%{pnam}
Version:	2.001
Release:	1
# http://www.ActiveState.com/corporate/artistic_license.htm or
# the license that comes with your perl distribution.
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	48f3f3f6629bcad8018aabb4e990fb23
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Array::IntSpan brings the speed advantages of Set::IntSpan (written by
Steven McDougall) to arrays.  Uses include manipulating grades,
routing tables, or any other situation where you have mutually
exclusive ranges of integers that map to given values (or objects).
This version of Array::IntSpan is able to consolidate ranges by
comparing adjacent values.

%description -l pl
Array::IntSpan przenosi zyski szybko¶ciowe Set::IntSpan do tablic.
Mo¿e byæ u¿ywany do manipulacji rangami, tablicami routingu lub
w ka¿dej innej sytuacji gdzie s± roz³±czne zakresy liczb ca³kowitych,
które maj± przypisane do nich warto¶ci lub obiekty. Ta wersja
Array::IntSpan jest w stanie konsolidowaæ zakresy poprzez porównanie
s±siaduj±cych warto¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Array/IntSpan.pm
%dir %{perl_vendorlib}/Array/IntSpan
%{perl_vendorlib}/Array/IntSpan/*.pm
%{_mandir}/man3/*
