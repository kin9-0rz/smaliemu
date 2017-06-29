# {'a': [1, 2, 3], 'ia': 0, 'ib': 1, 'ic': 2, 'ret': None, 'size': 3, 'va': 1, 'vb': 2, 'vc': 3}
const/16 va,1
const/16 vb,2
const/16 vc,3

const/16 ia,0
const/16 ib,1
const/16 ic,2

const/16 a,0
const/16 size,3

new-array a, size, dummy

aput va,a,ia
aput vb,a,ib
aput vc,a,ic