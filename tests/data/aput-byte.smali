#{'i1': 0, 'i2': 1, 'i3': 2, 'ret': None, 'v0': [3, 2, 1], 'v1': 3, 'v2': 2, 'v3': 1, 'v9': 3}

const/16 v9, 0x3
new-array v0, v9, [B

const/4 v1, 0x3
const/16 i1, 0x0
aput-byte v1, v0, i1

const/4 i2, 0x1
const/4 v2, 0x2
aput-byte v2, v0, i2

const/16 i3, 0x2
const/4 v3, 0x1
aput-byte v3, v0, i3
