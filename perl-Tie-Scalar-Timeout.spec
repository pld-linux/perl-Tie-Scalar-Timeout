#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tie
%define		pnam	Scalar-Timeout
Summary:	Tie::Scalar::Timeout - scalar variables that time out
Summary(pl.UTF-8):	Tie::Scalar::Timeout - zmienne skalarne ulegające przedawnieniu
Name:		perl-Tie-Scalar-Timeout
Version:	2.101420
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7466a9d2e052556140003b49b612cef1
URL:		http://search.cpan.org/dist/Tie-Scalar-Timeout/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to tie a scalar variable whose value will be
reset (subject to an expiry policy) after a certain time and/or a
certain number of uses. One possible application for this module might
be to time out session variables in mod_perl programs.

%description -l pl.UTF-8
Ten moduł pozwala wiązanie zmiennej skalarnej, której wartość będzie
przywrócona (zgodnie z polisą przedawnienia) po danym czasie i/lub
liczbie odwołań. Jednym z zastosowań tego modułu może być
przedawnianie zmiennych sesji w programach mod_perla.

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
%dir %{perl_vendorlib}/Tie/Scalar
%{perl_vendorlib}/Tie/Scalar/*.pm
%{_mandir}/man3/*
