#{'ret': None, 'v0': 'hello', 'v1': 4, 'v2': 'o', 'v3': 'hell'}

new-instance v0, Ljava/lang/StringBuffer;
const-string v3, "hell"
invoke-direct {v0, v3}, Ljava/lang/StringBuffer;-><init>(Ljava/lang/String;)V
const/4 v1, 0x4
const-string v2, "o"
invoke-virtual {v0, v1, v2}, Ljava/lang/StringBuilder;->insert(ILjava/lang/String;)Ljava/lang/StringBuilder;
