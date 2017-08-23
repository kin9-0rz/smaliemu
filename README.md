# smaliemu

It's the PY3 version for [evilsocket/smali_emulator](https://github.com/evilsocket/smali_emulator).

#### Install
```
pip install smaliemu
```

#### Usage

```

from smaliemu.emulator import Emulator

emu = Emulator()

snippet = [
    'const/4 v4, 0x1',
    'const/4 v3, 0x0',
    'new-instance v0, Ljava/lang/String;',
    'new-array v1, v4, [B',
    'const/16 v2, 0x44',
    'aput-byte v2, v1, v3',
    'invoke-direct {v0, v1}, Ljava/lang/String;-><init>([B)V',
    'return-object v0'
]
ret = emu2.call(snippet)
print("'%s'" % ret)
```

print
```
'DE'
```
---

#### Note

This is highly experimental, a very small subset of the Dalvik opcodes is currently supported, see the `smali/opcodes.py` file for more details.

OpCodes List (Feel free to request access)

https://docs.google.com/spreadsheets/d/1RfB_LsBoYnJxOh-lDCSMR0mfLBl1UlwdW9eKw2p03DY/edit?usp=sharing

#### License

Copyright (c) 2016 Simone Margaritelli | [Twitter](https://twitter.com/evilsocket) | [Blog](http://www.evilsocket.net)  
Released under the GPL 3 license.
