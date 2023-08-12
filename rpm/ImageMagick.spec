# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       ImageMagick

# >> macros
# << macros
%define mfr_revision 15
%define maj 7
%define mfr_version %{maj}.1.1
%define quantum_depth 16
%define clibver 10
%define libspec -%{maj}_Q%{quantum_depth}HDRI
%define source_version %{mfr_version}-%{mfr_revision}
%define this_is_a_hack see_yaml_for_details
%if 0%{?sailfishos_version} >= 40400
BuildRequires:  pkgconfig(libzstd)
%endif
%ifarch %{arm} %{arm64} aarch64
%ifarch %{arm64} aarch64
%define tune_arch armv8-a
%else
%define tune_arch armv7-a
%endif
%else
%ifarch %{ix86}
# J Tablet -> Intel Atom Z3735F -> silvermont
%define tune_arch silvermont
%else
%define tune_arch no
%endif
%endif

Summary:    Viewer and Converter for Images
Version:    7.1.1.15
Release:    1.1
Group:      Applications/Multimedia
License:    ImageMagick
URL:        https://imagemagick.org/
Source0:    %{name}-%{version}.tar.xz
Source100:  ImageMagick.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  bzip2-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  librsvg-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libwebp-devel
BuildRequires:  perl-devel

%description
ImageMagick®  is a software suite to create, edit, compose, or convert
bitmap images.
It can read and write images in a variety of formats (over 200) including
PNG, JPEG, GIF, HEIC, TIFF, DPX, EXR, WebP, Postscript, PDF, and SVG.
ImageMagick can resize, flip, mirror, rotate, distort, shear and transform
images, adjust image colors, apply various special effects, or draw text,
lines, polygons, ellipses and Bézier curves.

%if "%{?vendor}" == "chum"
Title: ImageMagick
PackagedBy: nephros
Type: console-application
Categories:
  - Graphics
  - Utility
  - Library
PackageIcon: https://github.com/nephros/harbour-imagemagick/raw/master/files/icon-imagemagick_sfos_256.png
Custom:
  Repo:   https://github.com/ImageMagick/ImageMagick
  PackagingRepo: https://github.com/sailfishos-chum/ImageMagick
Links:
  Homepage: https://imagemagick.org/
  Help: https://imagemagick.org/script/command-line-tools.php
%endif


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%package -n PerlMagick
Summary:    Perl module of %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description -n PerlMagick
%{summary}.

%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    CFLAGS="$RPM_OPT_FLAGS -fPIC -pie" \
    CXXFLAGS="$RPM_OPT_FLAGS -fPIC -pie" \
    --with-gcc-arch=%{tune_arch} \
    --enable-silent-rules \
    --enable-shared \
    --disable-docs \
    --disable-deprecated \
    --without-frozenpaths \
    --without-magick-plus-plus \
    --with-modules \
    --with-perl \
    --with-perl-options="PREFIX=%{_prefix}" \
    --with-djvu \
    --with-rsvg \
    --without-dps \
    --without-fftw \
    --without-flif \
    --without-fpx \
    --without-heic \
    --without-jbig \
    --without-lcms \
    --without-lqr \
    --without-openexr \
    --without-openjp2 \
    --without-raw \
    --without-x \
    --with-zstd


# >> build post
# Do *NOT* use %%{?_smp_mflags}, this causes PerlMagick to be silently misbuild
# make
#make %%{?_smp_mflags}
# lets try this from the macros
%{make_build}
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%make_install DESTDIR=$RPM_BUILD_ROOT
# << install pre

# >> install post
rm -rf %{buildroot}%{_mandir}
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE
%dir %{_sysconfdir}/ImageMagick-%{maj}
%config %{_sysconfdir}/ImageMagick-%{maj}/colors.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/delegates.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/log.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/mime.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/policy.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/quantization-table.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/thresholds.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type-apple.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type-dejavu.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type-ghostscript.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type-urw-base35.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type-windows.xml
%config %{_sysconfdir}/ImageMagick-%{maj}/type.xml
%{_datadir}/ImageMagick-%{maj}/francais.xml
%{_datadir}/ImageMagick-%{maj}/english.xml
%{_datadir}/ImageMagick-%{maj}/locale.xml
%{_bindir}/[^MW]*
%{_libdir}/libMagickCore*.so.%{clibver}*
%{_libdir}/libMagickWand*.so.%{clibver}*
%{_libdir}/ImageMagick*/config*
%{_libdir}/ImageMagick*/modules*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_libdir}/libMagickCore*.so
%{_libdir}/libMagickWand*.so
%dir %{_includedir}/ImageMagick*
%{_includedir}/ImageMagick*/MagickCore
%{_includedir}/ImageMagick*/MagickWand
%{_bindir}/MagickCore-config
%{_bindir}/MagickWand-config
%{_libdir}/pkgconfig/MagickCore*.pc
%{_libdir}/pkgconfig/ImageMagick*.pc
%{_libdir}/pkgconfig/MagickWand*.pc
# >> files devel
# << files devel

%files -n PerlMagick
%defattr(-,root,root,-)
%{_libdir}/perl5/perllocal.pod
%{_libdir}/perl5/Image/Magick.pm
%{_libdir}/perl5/Image/Magick/Q16HDRI.pm
%{_libdir}/perl5/auto/Image/Magick/.packlist
%{_libdir}/perl5/auto/Image/Magick/Magick.bs
%{_libdir}/perl5/auto/Image/Magick/Magick.so
%{_libdir}/perl5/auto/Image/Magick/Q16HDRI/Q16HDRI.bs
%{_libdir}/perl5/auto/Image/Magick/Q16HDRI/Q16HDRI.so
%{_libdir}/perl5/auto/Image/Magick/Q16HDRI/autosplit.ix
%{_libdir}/perl5/auto/Image/Magick/autosplit.ix
# >> files PerlMagick
# << files PerlMagick
