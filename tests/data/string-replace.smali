#{'ret': None, 'v0': 'hello', 'v2': 'hxxlo', 'v3': 'xx', 'v4': 'el'}

const-string v2, "hxxlo"
const-string v3, "xx"
const-string v4, "el"
invoke-virtual {v2, v3, v4}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;
move-result-object v0
