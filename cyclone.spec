Summary:	The Cyclone compiler
Summary(pl.UTF-8):	Kompilator języka Cyclone
Name:		cyclone
Version:	0.5
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	http://www.eecs.harvard.edu/~greg/cyclone/software/%{name}-%{version}.tar.gz
# Source0-md5:	20d2177e8bc432831fbdaa10aca462ee
Source1:	http://www.eecs.harvard.edu/~greg/cyclone/software/%{name}-%{version}-docs.tar.gz
# Source1-md5:	a3e557032b3444613089894a0e11dff7
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-options.patch
URL:		http://www.eecs.harvard.edu/~greg/cyclone/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cyclone is a language for C programmers who want to write secure,
robust programs. It's a dialect of C designed to be safe: free of
crashes, buffer overflows, format string attacks, and so on.

%description -l pl.UTF-8
Cyclone jest językiem dla programistów C, którzy chcą pisać bezpieczne
i szybkie programy. Jest on dialektem C zaprojektowanym by być
bezpiecznym: wolnym od SEGV, przepełnień buforów, format string
attacks, itd.

%prep
%setup -q -n %{name}-%{version}-%{version} -a1
%patch -P0 -p1
#%%patch1 -p1

%build
cp -f /usr/share/automake/config.* config
CFLAGS="%{rpmcflags}"
LDFLAGS="%{rpmldflags}"
%configure

%{__make}
%{__make} cyclone_src
%{__make} update
# hack, there is no doc/ in source distribution
mkdir doc
echo 'clean:' > doc/Makefile
%{__make} clean_nogc
# here we got C sources generated from patched cyclone,
# we can build for real.
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CYC_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc online-manual/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_includedir}/%{name}
