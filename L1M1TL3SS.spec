# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\L3VI\\Desktop\\L1M1TL3SS\\L1M1TL3SS.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\L3VI\\Desktop\\L1M1TL3SS\\dist\\background.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='L1M1TL3SS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
