# revision 29803
# category Package
# catalog-ctan /macros/generic/gates
# catalog-date 2012-05-27 01:03:23 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-gates
Version:	0.2
Release:	12
Summary:	Support for writing modular and customisable code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/gates
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gates.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gates.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means of writing code in a modular
fashion: big macros or functions are divided into small chunks
(called gates) with names, which can be externally controlled
(e.g. they can be disabled, subjected to conditionals,
loops...) and/or augmented with new chunks. Thus complex code
may easily be customised without having to rewrite it, or even
understand its implementation: the behavior of existing gates
can be modified, and new ones can be added, without endangering
the whole design. This allows code to be hacked in ways the
original authors might have never envisioned. The gates package
is implemented independently for both TeX and Lua. The TeX
implementation, running in any current environment, requires
the texapi package, whereas the Lua version can be run with any
Lua interpreter, not just LuaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/gates/gates.lua
%{_texmfdistdir}/tex/generic/gates/gates.sty
%{_texmfdistdir}/tex/generic/gates/gates.tex
%{_texmfdistdir}/tex/generic/gates/t-gates.tex
%doc %{_texmfdistdir}/doc/generic/gates/README
%doc %{_texmfdistdir}/doc/generic/gates/gates-doc.pdf
%doc %{_texmfdistdir}/doc/generic/gates/gates-doc.tex
%doc %{_texmfdistdir}/doc/generic/gates/gates-doc.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
