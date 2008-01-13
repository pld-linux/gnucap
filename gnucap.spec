Summary:	Gnucap - the GNU Circuit Analysis Package
Summary(pl.UTF-8):	Gnucap - analizatorem obwodów elektronicznych GNU
Name:		gnucap
Version:	0.35
Release:	0.9
License:	GPL
Group:		Applications
Source0:	http://www.geda.seul.org/dist/%{name}-%{version}.tar.gz
# Source0-md5:	16fc7cacac987ea556753d030f2595b9
URL:		http://www.gnu.org/software/gnucap/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The primary component is a general purpose circuit simulator. It
performs nonlinear DC and transient analyses, Fourier analysis, and AC
analysis. Spice compatible models for the MOSFET (level 1-8), BJT, and
diode are included in this release.

%description -l pl.UTF-8
Główny element to symulator obwodów elektronicznych ogólnego
przeznaczenia. Przeprowadza nieliniową analizę prądu stałego i
wygasania, analizę Fouriera oraz analizę prądu zmiennego. W tym
wydaniu załączone są kompatybilne ze Spice modele układów MOSFET
(poziomu 1-8), BJT i diod.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
