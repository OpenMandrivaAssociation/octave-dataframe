%define	pkgname dataframe
%define name	octave-%{pkgname}

Summary:	Data manipulation toolbox for Octave
Name:		%{name}
Version:	0.8.2
Release:	2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/dataframe/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.2.0
BuildRequires:	octave-devel >= 3.2.0
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildArch:	noarch

%description
Data manipulation toolbox for Octave. Similar to data.frame for R.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}


%changelog
* Tue Jun 28 2011 Lev Givon <lev@mandriva.org> 0.8.2-1mdv2011.0
+ Revision: 687894
- import octave-dataframe


