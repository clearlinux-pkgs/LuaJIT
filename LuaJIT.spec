#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : LuaJIT
Version  : 2.0.5
Release  : 6
URL      : http://luajit.org/download/LuaJIT-2.0.5.tar.gz
Source0  : http://luajit.org/download/LuaJIT-2.0.5.tar.gz
Summary  : Just-in-time compiler for Lua
Group    : Development/Tools
License  : MIT
Requires: LuaJIT-bin = %{version}-%{release}
Requires: LuaJIT-data = %{version}-%{release}
Requires: LuaJIT-lib = %{version}-%{release}
Requires: LuaJIT-license = %{version}-%{release}
Requires: LuaJIT-man = %{version}-%{release}
Patch1: build.patch

%description
-----------------------
LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language.

%package bin
Summary: bin components for the LuaJIT package.
Group: Binaries
Requires: LuaJIT-data = %{version}-%{release}
Requires: LuaJIT-license = %{version}-%{release}

%description bin
bin components for the LuaJIT package.


%package data
Summary: data components for the LuaJIT package.
Group: Data

%description data
data components for the LuaJIT package.


%package dev
Summary: dev components for the LuaJIT package.
Group: Development
Requires: LuaJIT-lib = %{version}-%{release}
Requires: LuaJIT-bin = %{version}-%{release}
Requires: LuaJIT-data = %{version}-%{release}
Provides: LuaJIT-devel = %{version}-%{release}

%description dev
dev components for the LuaJIT package.


%package lib
Summary: lib components for the LuaJIT package.
Group: Libraries
Requires: LuaJIT-data = %{version}-%{release}
Requires: LuaJIT-license = %{version}-%{release}

%description lib
lib components for the LuaJIT package.


%package license
Summary: license components for the LuaJIT package.
Group: Default

%description license
license components for the LuaJIT package.


%package man
Summary: man components for the LuaJIT package.
Group: Default

%description man
man components for the LuaJIT package.


%prep
%setup -q -n LuaJIT-2.0.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554422960
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags} MULTILIB=lib64


%install
export SOURCE_DATE_EPOCH=1554422960
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/LuaJIT
cp COPYRIGHT %{buildroot}/usr/share/package-licenses/LuaJIT/COPYRIGHT
%make_install MULTILIB=lib64

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/luajit
/usr/bin/luajit-2.0.5

%files data
%defattr(-,root,root,-)
/usr/share/luajit-2.0.5/jit/bc.lua
/usr/share/luajit-2.0.5/jit/bcsave.lua
/usr/share/luajit-2.0.5/jit/dis_arm.lua
/usr/share/luajit-2.0.5/jit/dis_mips.lua
/usr/share/luajit-2.0.5/jit/dis_mipsel.lua
/usr/share/luajit-2.0.5/jit/dis_ppc.lua
/usr/share/luajit-2.0.5/jit/dis_x64.lua
/usr/share/luajit-2.0.5/jit/dis_x86.lua
/usr/share/luajit-2.0.5/jit/dump.lua
/usr/share/luajit-2.0.5/jit/v.lua
/usr/share/luajit-2.0.5/jit/vmdef.lua

%files dev
%defattr(-,root,root,-)
/usr/include/luajit-2.0/lauxlib.h
/usr/include/luajit-2.0/lua.h
/usr/include/luajit-2.0/lua.hpp
/usr/include/luajit-2.0/luaconf.h
/usr/include/luajit-2.0/luajit.h
/usr/include/luajit-2.0/lualib.h
/usr/lib64/libluajit-5.1.so
/usr/lib64/pkgconfig/luajit.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libluajit-5.1.so.2
/usr/lib64/libluajit-5.1.so.2.0.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/LuaJIT/COPYRIGHT

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/luajit.1
