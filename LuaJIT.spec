#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : LuaJIT
Version  : 2.0.5
Release  : 3
URL      : http://luajit.org/download/LuaJIT-2.0.5.tar.gz
Source0  : http://luajit.org/download/LuaJIT-2.0.5.tar.gz
Summary  : Just-in-time compiler for Lua
Group    : Development/Tools
License  : MIT
Requires: LuaJIT-bin
Requires: LuaJIT-lib
Requires: LuaJIT-data
Requires: LuaJIT-doc
Patch1: build.patch

%description
-----------------------
LuaJIT is a Just-In-Time (JIT) compiler for the Lua programming language.

%package bin
Summary: bin components for the LuaJIT package.
Group: Binaries
Requires: LuaJIT-data

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
Requires: LuaJIT-lib
Requires: LuaJIT-bin
Requires: LuaJIT-data
Provides: LuaJIT-devel

%description dev
dev components for the LuaJIT package.


%package doc
Summary: doc components for the LuaJIT package.
Group: Documentation

%description doc
doc components for the LuaJIT package.


%package lib
Summary: lib components for the LuaJIT package.
Group: Libraries
Requires: LuaJIT-data

%description lib
lib components for the LuaJIT package.


%prep
%setup -q -n LuaJIT-2.0.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506530471
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1506530471
rm -rf %{buildroot}
%make_install
## make_install_append content
mv %{buildroot}/usr/lib/*so* %{buildroot}/usr/lib64
## make_install_append end

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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libluajit-5.1.so.2
/usr/lib64/libluajit-5.1.so.2.0.5
