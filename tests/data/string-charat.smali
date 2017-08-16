# {'ret': None, 'v0': 'hello', 'v2': 1, 'v3': 'e'}

const-string/jumbo v0, "hello"
const/4 v2, 0x1
invoke-virtual {v0, v2}, Ljava/lang/String;->charAt(I)C
move-result v3
