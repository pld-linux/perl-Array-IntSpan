#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Array
%define		pnam	IntSpan
%include	/usr/lib/rpm/macros.perl
Summary:	Array::IntSpan - a module for handling arrays using IntSpan techniques
Summary(pl.UTF-8):	Array::IntSpan - moduł do obsługi tablic z użyciem techniki IntSpan
Name:		perl-Array-IntSpan
Version:	2.002
Release:	1
# http://www.ActiveState.com/corporate/artistic_license.htm or
# the license that comes with your perl distribution.
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a21691f17c714ee82ee6cdd14f2b899c
URL:		http://search.cpan.org/dist/Array-IntSpan/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Array::IntSpan brings the speed advantages of Set::IntSpan (written by
Steven McDougall) to arrays. Uses include manipulating grades, routing
tables, or any other situation where you have mutually exclusive
ranges of integers that map to given values (or objects). This version
of Array::IntSpan is able to consolidate ranges by comparing adjacent
values.

%description -l pl.UTF-8
Array::IntSpan przenosi zyski szybkościowe Set::IntSpan do tablic.
Może być używany do manipulacji rangami, tablicami routingu lub w
każdej innej sytuacji gdzie są rozłączne zakresy liczb całkowitych,
które mają przypisane do nich wartości lub obiekty. Ta wersja
Array::IntSpan jest w stanie konsolidować zakresy poprzez porównanie
sąsiadujących wartości.

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
