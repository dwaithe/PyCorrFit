# -*- mode: python -*-
a = Analysis(['C:\\Python27\\PyCorrFit\\src\\PyCorrFit.py'],
             pathex=['C:\\Python27\\pyinstaller'],
             hiddenimports=[],
             hookspath=None)
a.datas += [('doc\\ChangeLog.txt', 'C:\\Python27\\PyCorrFit\\ChangeLog.txt', 'DATA'),
            ('doc\\PyCorrFit_doc.pdf', 'C:\\Python27\\PyCorrFit\\PyCorrFit_doc.pdf', 'DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'PyCorrFit.exe'),
          debug=False,
          strip=None,
          upx=True,
          icon='C:\\Python27\\PyCorrFit\\pyinstaller-howto\\PyCorrFit.ico',
#          console=False )
          console=True )
#app = BUNDLE(exe,
#             name=os.path.join('dist', 'PyCorrFit.exe.app'))
# Plotting with latex did not work in windowes mode...
