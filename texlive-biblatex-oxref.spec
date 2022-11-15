Name:		texlive-biblatex-oxref
Version:	57513
Release:	1
Summary:	BibLaTeX styles inspired by the Oxford Guide to Style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-oxref
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-oxref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-oxref.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-oxref.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides four BibLaTeX styles that implement (many
of) the stipulations and examples provided by the 2014 New
Hart's Rules and the 2002 Oxford Guide to Style: 'oxnotes' is a
style similar to the standard 'verbose', intended for use with
footnotes; 'oxnum' is a style similar to the standard
'numeric', intended for use with numeric in-text citations;
'oxalph' is a style similar to the standard 'alphabetic',
intended for use with alphabetic in-text citations; 'oxyear' is
a style similar to the standard 'author-year', intended for use
with parenthetical in-text citations. The bundle provides
support for a wide variety of content types, including
manuscripts, audiovisual resources, social media and legal
references.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/biblatex-oxref
%{_texmfdistdir}/tex/latex/biblatex-oxref
%doc %{_texmfdistdir}/doc/latex/biblatex-oxref

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
