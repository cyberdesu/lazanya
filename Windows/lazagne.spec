# -*- mode: python ; coding: utf-8 -*-
# Build:  pyinstaller lazagne.spec      -> dist/lazagne.exe (onefile, console)
# Compatible with PyInstaller 5.x and 6.x.

import sys
sys.path.append(".")

from lazagne.config.manage_modules import get_modules_names
from lazagne.softwares.browsers.chromium_browsers import chromium_based_module_location
from lazagne.softwares.browsers.firefox_browsers import mozilla_module_location

all_hidden_imports_module_names = get_modules_names() + [mozilla_module_location, chromium_based_module_location]
hiddenimports = [package_name for package_name, module_name in all_hidden_imports_module_names]

# Drop packages LaZagne never uses. Shrinks the exe and cuts onefile extraction
# time at startup. Kept conservative on purpose (no setuptools/distutils removal,
# some crypto deps import pkg_resources at runtime).
excludes = [
    'tkinter', 'unittest', 'test', 'tests', 'pydoc', 'doctest',
    'lib2to3', 'xmlrpc', 'pdb', 'ensurepip', 'venv',
]

a = Analysis(
    ['laZagne.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=excludes,
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='lazagne',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,          # UPX slows startup (runtime decompression); off = faster launch
    runtime_tmpdir=None,
    console=True,
)
