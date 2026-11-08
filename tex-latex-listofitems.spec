Summary:	Grab items in lists using user-specified sep char
Name:		tex-latex-listofitems
Version:	1.65
Release:	1
License:	LaTeX Project Public License v1.3+
Group:		Applications/Publishing
Source0:	http://mirrors.ctan.org/macros/generic/listofitems.zip
# Source0-md5:	9dc62c5da2112e6e16f0cd1c02dcfe86
URL:		https://ctan.org/pkg/listofitems/
BuildRequires:	/usr/bin/latex
BuildRequires:	rpmbuild(macros) >= 1.751
BuildRequires:	unzip
Requires(post,postun):	/usr/bin/texhash
# TODO: use generic
Requires:	texlive-latex
Provides:	tex(listofitems) = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This simple package is designed to read a list of items whose parsing
character may be selected by the user.

%prep
%setup -q -n listofitems

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{doc,tex}/latex/listofitems

cp -p *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/listofitems
cp -p listofitems.tex *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/listofitems

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README
%doc %{_datadir}/texmf/doc/latex/listofitems
%{_datadir}/texmf/tex/latex/listofitems
