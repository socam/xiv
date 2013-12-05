%define name xiv
%define version 0.9
%define prefix /usr

Summary: A simple yet powerful image viewer for X11.
Name: %{name}
Version: %{version}
Source: %{name}-%{version}.tgz
Release: 1%{?dist}
License: BSD
Group: Graphisme
Url: http://sourceforge.net/projects/xiv/
BuildRequires: libexif-devel libjpeg-devel libtiff-devel libX11-devel

%description
xiv is a very simple image viewer without GUI (but an X11 window) and only controled by keys and mouse.
As opposed to most of the image viewers, it does not rely on scrollbar for image panning.
It is a powerful tool to analyse huge images.
The Window is a view of the image in which you can zoom, pan, rotate...
xiv reads natxively 8 and 16 bits binary PPM/JPG and TIF images and uses ImageMagick to convert other formats.

%prep
%setup -q -n %{name}-%{version}

%build
export CXXFLAGS=-O3
export LDFLAGS="-Wl,--build-id"
./configure --prefix=%{prefix}
make %{?jobs:-j%jobs} clean
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{prefix}
make PREFIX=%{buildroot}%{prefix} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
# %doc README INSTALL ChangeLog TODO LICENSE
%{_bindir}/xiv
%{_bindir}/xiv.sh
/usr/share/applications/xiv.desktop
/usr/share/icons/xiv.png
/usr/share/man/man1/xiv.1.gz
/usr/share/xiv/LICENSE
/usr/share/xiv/ChangeLog
/usr/share/xiv/INSTALL
/usr/share/xiv/README
/usr/share/xiv/TODO
/usr/share/xiv/xiv.ppm


%changelog
