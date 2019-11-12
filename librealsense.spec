#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : librealsense
Version  : 2.30.1
Release  : 3
URL      : https://github.com/IntelRealSense/librealsense/archive/v2.30.1/librealsense-2.30.1.tar.gz
Source0  : https://github.com/IntelRealSense/librealsense/archive/v2.30.1/librealsense-2.30.1.tar.gz
Summary  : Intel® RealSense™ SDK 2.0 is a cross-platform library for Intel® RealSense™ depth cameras (D400 series and the SR300)
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause-LBNL BSL-1.0 MIT Zlib
Requires: librealsense-bin = %{version}-%{release}
Requires: librealsense-lib = %{version}-%{release}
Requires: librealsense-license = %{version}-%{release}
Requires: setuptools
Requires: wheel
BuildRequires : Vulkan-Headers-dev Vulkan-Loader-dev Vulkan-Tools
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-mvn
BuildRequires : buildreq-qmake
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules wayland
BuildRequires : glfw-dev
BuildRequires : glibc-dev
BuildRequires : glu-dev
BuildRequires : gradle
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(osmesa)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : python3
BuildRequires : setuptools
BuildRequires : wheel

%description
TCLAP - Templatized Command Line Argument Parser
This is a simple C++ library that facilitates parsing command line
arguments in a type independent manner.  It doesn't conform exactly
to either the GNU or POSIX standards, although it is close.  See
docs/manual.html for descriptions of how things work or look at the
simple examples in the examples dir.

%package bin
Summary: bin components for the librealsense package.
Group: Binaries
Requires: librealsense-license = %{version}-%{release}

%description bin
bin components for the librealsense package.


%package dev
Summary: dev components for the librealsense package.
Group: Development
Requires: librealsense-lib = %{version}-%{release}
Requires: librealsense-bin = %{version}-%{release}
Provides: librealsense-devel = %{version}-%{release}
Requires: librealsense = %{version}-%{release}
Requires: librealsense = %{version}-%{release}

%description dev
dev components for the librealsense package.


%package lib
Summary: lib components for the librealsense package.
Group: Libraries
Requires: librealsense-license = %{version}-%{release}

%description lib
lib components for the librealsense package.


%package license
Summary: license components for the librealsense package.
Group: Default

%description license
license components for the librealsense package.


%prep
%setup -q -n librealsense-2.30.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573517154
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573517154
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/librealsense
cp %{_builddir}/librealsense-2.30.1/LICENSE %{buildroot}/usr/share/package-licenses/librealsense/feb32923246a19b9ca9f031fb603f140e2f212fe
cp %{_builddir}/librealsense-2.30.1/third-party/easyloggingpp/LICENCE %{buildroot}/usr/share/package-licenses/librealsense/771862b9a708887e47e8c13341d580bd0e2c82c5
cp %{_builddir}/librealsense-2.30.1/third-party/glfw/LICENSE.md %{buildroot}/usr/share/package-licenses/librealsense/21c8bb406fc95e37e02393d355d00faf4d3fd732
cp %{_builddir}/librealsense-2.30.1/third-party/imgui/LICENSE %{buildroot}/usr/share/package-licenses/librealsense/4d91c0fc8635b88888b4ed6c3dc5cbb17b31aaca
cp %{_builddir}/librealsense-2.30.1/third-party/rapidxml/LICENSE %{buildroot}/usr/share/package-licenses/librealsense/f5ea943700a003596770d4775c51d02156e674cb
cp %{_builddir}/librealsense-2.30.1/third-party/realsense-file/lz4/LICENSE %{buildroot}/usr/share/package-licenses/librealsense/10bf56381baaf07f0647b93a810eb4e7e9545e8d
cp %{_builddir}/librealsense-2.30.1/third-party/tclap/COPYING %{buildroot}/usr/share/package-licenses/librealsense/ed4f829086f9054d9e63b9919e4184c7db4731de
cp %{_builddir}/librealsense-2.30.1/wrappers/python/third_party/pybind11/LICENSE %{buildroot}/usr/share/package-licenses/librealsense/71a7f368f90789db807331860cb72d10abdb4acb
cp %{_builddir}/librealsense-2.30.1/wrappers/unrealengine4/LICENSE %{buildroot}/usr/share/package-licenses/librealsense/feb32923246a19b9ca9f031fb603f140e2f212fe
cp %{_builddir}/librealsense-2.30.1/wrappers/unrealengine4/Plugins/RuntimeMeshComponent/LICENSE %{buildroot}/usr/share/package-licenses/librealsense/b4c9ccda5c30717eb1df3b5c7bb8d3a0d8e57b70
pushd clr-build
%make_install prefix=/usr LIB_SUFFIX=64
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/realsense-viewer
/usr/bin/rs-align
/usr/bin/rs-align-advanced
/usr/bin/rs-ar-basic
/usr/bin/rs-benchmark
/usr/bin/rs-callback
/usr/bin/rs-capture
/usr/bin/rs-color
/usr/bin/rs-convert
/usr/bin/rs-data-collect
/usr/bin/rs-depth
/usr/bin/rs-depth-quality
/usr/bin/rs-distance
/usr/bin/rs-enumerate-devices
/usr/bin/rs-fw-logger
/usr/bin/rs-fw-update
/usr/bin/rs-gl
/usr/bin/rs-hello-realsense
/usr/bin/rs-measure
/usr/bin/rs-motion
/usr/bin/rs-multicam
/usr/bin/rs-pointcloud
/usr/bin/rs-pose
/usr/bin/rs-pose-and-image
/usr/bin/rs-pose-predict
/usr/bin/rs-post-processing
/usr/bin/rs-record
/usr/bin/rs-record-playback
/usr/bin/rs-rosbag-inspector
/usr/bin/rs-save-to-disk
/usr/bin/rs-sensor-control
/usr/bin/rs-software-device
/usr/bin/rs-terminal
/usr/bin/rs-tracking-and-depth
/usr/bin/rs-trajectory

%files dev
%defattr(-,root,root,-)
/usr/include/librealsense2/h/rs_advanced_mode_command.h
/usr/include/librealsense2/h/rs_config.h
/usr/include/librealsense2/h/rs_context.h
/usr/include/librealsense2/h/rs_device.h
/usr/include/librealsense2/h/rs_frame.h
/usr/include/librealsense2/h/rs_internal.h
/usr/include/librealsense2/h/rs_option.h
/usr/include/librealsense2/h/rs_pipeline.h
/usr/include/librealsense2/h/rs_processing.h
/usr/include/librealsense2/h/rs_record_playback.h
/usr/include/librealsense2/h/rs_sensor.h
/usr/include/librealsense2/h/rs_types.h
/usr/include/librealsense2/hpp/rs_context.hpp
/usr/include/librealsense2/hpp/rs_device.hpp
/usr/include/librealsense2/hpp/rs_export.hpp
/usr/include/librealsense2/hpp/rs_frame.hpp
/usr/include/librealsense2/hpp/rs_internal.hpp
/usr/include/librealsense2/hpp/rs_options.hpp
/usr/include/librealsense2/hpp/rs_pipeline.hpp
/usr/include/librealsense2/hpp/rs_processing.hpp
/usr/include/librealsense2/hpp/rs_record_playback.hpp
/usr/include/librealsense2/hpp/rs_sensor.hpp
/usr/include/librealsense2/hpp/rs_types.hpp
/usr/include/librealsense2/rs.h
/usr/include/librealsense2/rs.hpp
/usr/include/librealsense2/rs_advanced_mode.h
/usr/include/librealsense2/rs_advanced_mode.hpp
/usr/include/librealsense2/rsutil.h
/usr/lib64/cmake/realsense2/realsense2-glConfig.cmake
/usr/lib64/cmake/realsense2/realsense2-glConfigVersion.cmake
/usr/lib64/cmake/realsense2/realsense2-glTargets-relwithdebinfo.cmake
/usr/lib64/cmake/realsense2/realsense2-glTargets.cmake
/usr/lib64/cmake/realsense2/realsense2Config.cmake
/usr/lib64/cmake/realsense2/realsense2ConfigVersion.cmake
/usr/lib64/cmake/realsense2/realsense2Targets-relwithdebinfo.cmake
/usr/lib64/cmake/realsense2/realsense2Targets.cmake
/usr/lib64/librealsense2-gl.so
/usr/lib64/librealsense2.so
/usr/lib64/pkgconfig/realsense2-gl.pc
/usr/lib64/pkgconfig/realsense2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/librealsense2-gl.so.2.30
/usr/lib64/librealsense2-gl.so.2.30.1
/usr/lib64/librealsense2.so.2.30
/usr/lib64/librealsense2.so.2.30.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/librealsense/10bf56381baaf07f0647b93a810eb4e7e9545e8d
/usr/share/package-licenses/librealsense/21c8bb406fc95e37e02393d355d00faf4d3fd732
/usr/share/package-licenses/librealsense/4d91c0fc8635b88888b4ed6c3dc5cbb17b31aaca
/usr/share/package-licenses/librealsense/71a7f368f90789db807331860cb72d10abdb4acb
/usr/share/package-licenses/librealsense/771862b9a708887e47e8c13341d580bd0e2c82c5
/usr/share/package-licenses/librealsense/b4c9ccda5c30717eb1df3b5c7bb8d3a0d8e57b70
/usr/share/package-licenses/librealsense/ed4f829086f9054d9e63b9919e4184c7db4731de
/usr/share/package-licenses/librealsense/f5ea943700a003596770d4775c51d02156e674cb
/usr/share/package-licenses/librealsense/feb32923246a19b9ca9f031fb603f140e2f212fe
