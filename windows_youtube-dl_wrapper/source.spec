# -*- mode: python -*-
a = Analysis(['source.py'],
             pathex=['C:\\Users\\Pre\\Documents\\GitHub\\YTMP3DL\\windows_youtube-dl_wrapper'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='source.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
