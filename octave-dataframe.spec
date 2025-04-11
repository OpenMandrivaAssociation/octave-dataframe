%global octpkg dataframe

Summary:	Data manipulation toolbox for Octave
Name:		octave-dataframe
Version:	1.2.0
Release:	3
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/dataframe/
Source0:	https://downloads.sourceforge.net/octave/dataframe-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.4.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Data manipulation toolbox for Octave similar to R data.frame.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

