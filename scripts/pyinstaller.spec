# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\app.py'],
             pathex=[],
             binaries=None,
             datas=[
                ('.\\..\\assets\\imgs\\logo-md.png', '.\\ePinXtractr\\assets\\imgs'),
                ('.\\..\\assets\\imgs\\app-ui.png', '.\\ePinXtractr\\assets\\imgs'),
                ('.\\..\\assets\\fonts\\*.ttf', '.\\ePinXtractr\\assets\\fonts'),
                ('.\\..\\assets\\epx.min.css', '.\\ePinXtractr\\assets\\.'),
                ('.\\ePinXtractr.bat', '.\\ePinXtractr\\'),
                ('.\\..\\epx.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ePinXtractr',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='bin')
