#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Scalar-Timeout
Summary:	Tie::Scalar::Timeout - Scalar variables that time out
Summary(pl):	Tie::Scalar::Timeout - zmienne skalarne ulegaj±ce przedawnieniu
Name:		perl-Tie-Scalar-Timeout
Version:	1.3
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d0882da74c775742936c379af946796b
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to tie a scalar variable whose value will be
reset (subject to an expiry policy) after a certain time and/or a
certain number of uses. One possible application for this module might
be to time out session variables in mod_perl programs.

%description -l pl
Ten modu³ pozwala wi±zanie zmiennej skalarnej, której warto¶æ bêdzie
przywrócona (zgodnie z polis± przedawnienia) po danym czasie i/lub
liczbie odwo³añ. Jednym z zastosowañ tego modu³u mo¿e byæ
przedawnianie zmiennych sesji w programach mod_perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Tie/Scalar
%{perl_vendorlib}/Tie/Scalar/*.pm
%{_mandir}/man3/*
