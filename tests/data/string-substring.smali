#{'ret': None, 'v1': '0123456789', 'v2': 0, 'v3': 3, 'v4': '012'}

const-string v1, "0123456789"
const/4 v2, 0x0
const/16 v3, 0x3
invoke-virtual {v1, v2, v3}, Ljava/lang/String;->substring(II)Ljava/lang/String;
move-result-object v4
