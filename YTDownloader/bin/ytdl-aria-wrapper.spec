# -*- mode: python -*-
a = Analysis(['.\\ytdl-aria-wrapper.py'],
             pathex=['C:\\Users\\Pre\\Documents\\GitHub\\YTMP3DL\\windows_youtube-dl_wrapper\\bin'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ytdl-aria-wrapper.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
