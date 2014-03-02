%define	pkgname dataframe

Summary:	Data manipulation toolbox for Octave
Name:		octave-%{pkgname}
Version:	0.8.2
Release:	3
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/dataframe/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.2.0
BuildRequires:	octave-devel >= 3.2.0
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
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
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
