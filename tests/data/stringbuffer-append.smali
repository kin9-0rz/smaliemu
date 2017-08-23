#{'ret': None, 'v0': 'aaa ccc bbb', 'v2': ' ccc', 'v3': 'aaa', 'v4': ' bbb'}

const-string v2, " ccc"
new-instance v0, Ljava/lang/StringBuffer;
const-string v3, "aaa"
const-string v4, " bbb"
invoke-direct {v0, v3}, Ljava/lang/StringBuffer;-><init>(Ljava/lang/String;)V
invoke-virtual {v0, v2}, Ljava/lang/StringBuffer;->append(Ljava/lang/String;)Ljava/lang/StringBuffer;
invoke-virtual {v0, v4}, Ljava/lang/StringBuffer;->append(Ljava/lang/String;)Ljava/lang/StringBuffer;
move-result-object v0
invoke-virtual {v0}, Ljava/lang/StringBuffer;->toString()Ljava/lang/String;
