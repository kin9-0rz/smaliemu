# {'i': 1, 'r': 'e', 'ret': 'e', 's': 'hello'}
const-string s, "hello"
const/12 i, 1

invoke-virtual {s, i}, Ljava/lang/String;->charAt(I)C
move-result r
return-object r
