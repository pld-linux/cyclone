Summary:	The Cyclone compiler
Summary(pl):	Kompilator jêzyka Cyclone
Name:		cyclone
Version:	0.2
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://www.cs.cornell.edu/projects/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f27081a442bff470f9e477e5d017d2d9
Source1:	http://www.cs.cornell.edu/projects/%{name}-%{version}-docs.tar.gz
# Source1-md5:	395c1b64bee877a69c314cf33fda1a1e
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-options.patch
URL:		http://www.cs.cornell.edu/projects/cyclone/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cyclone is a language for C programmers who want to write secure,
robust programs. It's a dialect of C designed to be safe: free of
crashes, buffer overflows, format string attacks, and so on.

%description -l pl
Cyclone jest jêzykiem dla programistów C, którzy chc± pisaæ bezpieczne
i szybkie programy. Jest on dialektem C zaprojektowanym by byæ
bezpiecznym: wolnym od SEGV, przepe³nieñ buforów, format string
attacks, itd.

%prep
%setup -q -n %{name} -a1
%patch0 -p1
%patch1 -p1

%build
%ifarch ppc
echo "y" | \
%endif
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc online-manual/*
%attr(755, root, root) %{_bindir}/*
%{_libdir}/%{name}
%{_includedir}/%{name}
