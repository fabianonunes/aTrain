# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata
from importlib.resources import files

icon_path = str(files("aTrain.static").joinpath("favicon.ico"))

datas = []
datas += collect_data_files('aTrain')
datas += [(str(files("transformers").joinpath("")),'transformers')]
datas += [(str(files("speechbrain").joinpath("")),'speechbrain')]
datas += collect_data_files('torch')
datas += collect_data_files('transformers')
datas += collect_data_files('lightning')
datas += collect_data_files('lightning_fabric')
datas += collect_data_files('lightning_utilities')
datas += collect_data_files('pyannote')
datas += collect_data_files('pyannote.audio.models')
datas += collect_data_files('pyannote.audio.models.segmentation')
datas += collect_data_files('pyannote.audio.models.embedding')
datas += collect_data_files('pytorch_lightning')
datas += collect_data_files('faster_whisper')
datas += collect_data_files('aTrain_core')
datas += copy_metadata('transformers')
datas += copy_metadata('lightning')
datas += copy_metadata('lightning_utilities')
datas += copy_metadata('torch')
datas += copy_metadata('tqdm')
datas += copy_metadata('regex')
datas += copy_metadata('requests')
datas += copy_metadata('packaging')
datas += copy_metadata('filelock')
datas += copy_metadata('numpy')
datas += copy_metadata('tokenizers')
datas += copy_metadata('pyannote.audio')
datas += copy_metadata('huggingface-hub')
datas += copy_metadata('safetensors')
datas += copy_metadata('pyyaml')
datas += copy_metadata('pytorch_lightning')
datas += copy_metadata('aTrain_core')

hiddenimports = ['pytorch_lightning','pyyaml','safetensors','huggingface-hub','speechbrain','pyannote','pytorch','transformers','lightning',]
hiddenimports += collect_submodules('wakepy')
hiddenimports += collect_submodules('speechbrain')
hiddenimports += collect_submodules('pyannote')
hiddenimports += collect_submodules('sklearn')

a = Analysis(
    ['build.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='aTrain',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[icon_path],
    plist='Info.plist'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='aTrain',
)
