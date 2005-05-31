#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	I18N
%define	pnam	AcceptLanguage
Summary:	I18N::AcceptLanguage - matches language preference to available languages
Summary(pl):	I18N::AcceptLanguage - wybór preferowanego jêzyka spo¶ród dostêpnych
Name:		perl-I18N-AcceptLanguage
Version:	1.04
Release:	1
License:	IBM Public License v1.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1701416f97aeb857dab6f3905e396864
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More) >= 0.45
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I18N::AcceptLanguage matches language preference to available
languages per rules defined in RFC 2616, section 14.4: HTTP/1.1 -
Header Field Definitions - Accept-Language.

%description -l pl
I18N::AcceptLanguage dokonuje wyboru jêzyków na podstawie preferencji
jêzykowych oraz dostêpnych jêzyków, zgodnie z zasadami okre¶lonymi w
rozdziale 14.4 RFC 2616: HTTP/1.1 - Header Field Definitions -
Accept-Language (HTTP/1.1 - definicje pól nag³ówka - Accept-Language).

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
%doc Changes
%{perl_vendorlib}/I18N/*.pm
%{_mandir}/man3/*
