Summary:	The Cyclone compiler
Summary(pl):	Kompilator j�zyka Cyclone
Name:		cyclone
Version:	0.2
Release:	1
License:	GPL
#Vendor:		
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/J�zyki
Source0:	http://www.cs.cornell.edu/projects/%{name}/%{name}-%{version}.tar.gz
Source1:	http://www.cs.cornell.edu/projects/%{name}-%{version}-docs.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-options.patch
URL:		http://www.cs.cornell.edu/projects/cyclone/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cyclone is a language for C programmers who want to write secure, robust
programs. It's a dialect of C designed to be safe: free of crashes,
buffer overflows, format string attacks, and so on.

%description -l pl
Cyclone jest j�zykiem dla programist�w C, kt�rzy chc� pisa� bezpieczne i
szybkie programy. Jest on dialektem C zaprojektowanym by by� bezpiecznym:
wolnym od SEGV, przepe�nie� bufor�w, format string attacks, itd.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
tar zxf %{SOURCE1}

%build
./configure \
	-sh /bin/sh \
	-bindir %{_bindir} \
	-libdir %{_libdir}/%{name} \
	-incdir %{_includedir}/%{name} 

%{__make}
%{__make} cyclone_src
%{__make} update
# hack, there is no doc/ in source distribution
mkdir doc
echo 'clean:' > doc/Makefile
%{__make} clean_nogc
# here we got C sources generated from patched cyclone,
# we can build for real.
%{__make} CFLAGS="%{rpmcflags}" CYC_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf INSTALL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz online-manual/*
%attr(755, root, root) %{_bindir}/*
%{_libdir}/%{name}
%{_includedir}/%{name}
