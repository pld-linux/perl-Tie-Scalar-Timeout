#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Scalar-Timeout
Summary:	Tie::Scalar::Timeout - scalar variables that time out
Summary(pl):	Tie::Scalar::Timeout - zmienne skalarne ulegaj±ce przedawnieniu
Name:		perl-Tie-Scalar-Timeout
Version:	1.3.2
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	196b8df8b93339701f3271a9fa28551f
BuildRequires:	perl-devel >= 1:5.8.0
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
