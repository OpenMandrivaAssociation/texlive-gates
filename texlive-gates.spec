%global tl_name gates
%global tl_revision 29803

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Support for writing modular and customisable code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/gates
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gates.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gates.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means of writing code in a modular fashion: big
macros or functions are divided into small chunks (called gates) with
names, which can be externally controlled (e.g. they can be disabled,
subjected to conditionals, loops...) and/or augmented with new chunks.
Thus complex code may easily be customised without having to rewrite it,
or even understand its implementation: the behavior of existing gates
can be modified, and new ones can be added, without endangering the
whole design. This allows code to be hacked in ways the original authors
might have never envisioned. The gates package is implemented
independently for both TeX and Lua. The TeX implementation, running in
any current environment, requires the texapi package, whereas the Lua
version can be run with any Lua interpreter, not just LuaTeX.

