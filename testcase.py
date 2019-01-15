

a = "red"
b = "bluegreen"
c = "yellow"
d = "darkblue"
e = "purple"
f = "lightblue"
h = "pink"
i = "rosered"
j = "orange"
k = "grassgreen"
l = "purplered"
m = "brightred"
n = "white"
g = "darkgreen"
o ="sky"
p = "grey"
q = "darkpink"
r = "darkgrey"
s = "dust"
t = "blue"

"""
sloveable
"""
r1 = [a,a,a,a,a,a,b,b,c,c,c,c,c,c,c,c,c,c,c,c]
r2 = [a,a,a,a,a,a,b,b,c,c,c,c,c,c,d,d,d,c,c,c]
r3 = [a,a,a,a,e,e,b,b,c,c,c,c,c,d,d,d,d,d,d,c]
r4 = [a,a,h,a,e,e,b,b,l,l,c,c,d,d,d,d,d,d,i,i]
r5 = [a,h,h,h,e,e,b,b,l,l,c,c,d,d,j,d,k,k,i,i]
r6 = [h,h,h,h,e,e,f,f,l,l,c,c,j,j,j,d,k,k,i,i]
r7 = [h,h,h,e,e,e,f,f,l,l,c,l,j,j,j,d,k,k,i,i]
r8 = [h,h,h,e,e,e,f,f,l,l,l,l,j,j,j,k,k,k,i,i]
r9 = [h,h,h,e,e,e,f,f,l,l,l,l,j,j,j,k,k,i,i,i]
r10= [h,h,h,e,e,e,f,f,l,l,l,j,j,j,j,k,k,i,i,i]
r11= [g,g,e,e,e,e,m,m,n,l,l,j,j,j,o,k,k,i,i,i]
r12= [g,g,g,g,p,p,m,m,n,n,l,o,o,o,o,k,k,i,i,i]
r13= [g,g,g,g,p,p,m,m,n,n,l,o,o,o,q,k,k,k,k,r]
r14 =[g,g,g,g,p,p,m,m,n,n,n,o,o,o,q,q,k,k,k,r]
r15 =[g,g,p,p,p,p,m,m,n,n,o,o,o,o,q,q,q,q,k,r]
r16 =[g,p,p,p,p,p,n,n,n,n,s,s,s,o,q,q,q,r,k,r]
r17 =[g,p,p,n,n,n,n,n,n,s,s,s,s,s,s,q,q,r,r,r]
r18 =[g,p,p,p,n,n,n,n,n,s,s,s,s,s,s,q,q,r,r,r]
r19= [g,t,t,t,t,t,t,t,t,t,t,s,s,q,q,q,q,r,r,r]
r20 =[g,t,t,t,t,t,t,t,t,t,t,s,s,s,q,q,r,r,r,r]

solveable_3trees =[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20]


"""
unsolveable
"""

unsolveable_3trees = [[a,a,a,a,a,b,b,b,b,b,c,c,c,c,c,c,c,c,c,c]
,[a,a,a,a,b,b,b,b,b,c,c,c,c,c,d,d,d,c,c,c]
,[a,a,a,a,e,b,b,b,f,c,c,c,c,d,d,d,d,d,d,c]
,[a,a,h,a,e,b,b,f,f,f,c,c,d,d,d,d,d,d,i,i]
,[a,h,h,h,e,f,f,f,f,f,c,c,d,d,j,d,k,k,i,i]
,[h,h,h,h,e,f,f,f,f,f,c,c,j,j,j,d,k,k,i,i]
,[h,h,h,e,e,f,f,f,f,l,c,l,j,j,j,d,k,k,i,i]
,[h,h,h,e,e,f,f,f,l,l,l,l,j,j,j,k,k,k,i,i]
, [h,h,h,e,e,f,f,f,l,l,l,l,j,j,j,k,k,i,i,i]
,[h,h,h,e,e,e,m,m,l,l,l,j,j,j,j,k,k,i,i,i]
,[g,g,e,e,e,e,m,m,n,l,l,j,j,j,o,k,k,i,i,i]
,[g,g,g,g,p,p,m,m,n,n,l,o,o,o,o,k,k,i,i,i]
,[g,g,g,g,p,p,m,m,n,n,l,o,o,o,q,k,k,k,k,r]
,[g,g,g,g,p,p,m,m,n,n,n,o,o,o,q,q,k,k,k,r]
,[g,g,p,p,p,p,m,m,n,n,o,o,o,o,q,q,q,q,k,r]
,[g,p,p,p,p,p,n,n,n,n,s,s,s,o,q,q,q,r,k,r]
,[g,p,p,n,n,n,n,n,n,s,s,s,s,s,s,q,q,r,r,r]
,[g,p,p,p,n,n,n,n,n,s,s,s,s,s,s,q,q,r,r,r]
,[g,t,t,t,t,t,t,t,t,t,t,s,s,q,q,q,q,r,r,r]
,[g,t,t,t,t,t,t,t,t,t,t,s,s,s,q,q,r,r,r,r]]


"""
1 tree 2 trees unsolveable 5 cases each
"""
#1 tree
#1
r1 = [a,a,b,b,b]
r2 = [c,c,b,d,d]
r3 = [c,e,b,d,d]
r4 = [c,e,e,e,d]
r5 = [c,e,d,d,d]
unsolveable_1tree1 =[r1,r2,r3,r4,r5]
#2
r1 = [a,a,a,b,b,f]
r2 = [c,c,b,b,d,f]
r3 = [c,e,b,d,d,f]
r4 = [c,e,e,e,d,f]
r5 = [c,e,d,d,d,f]
r6 = [c,e,d,d,f,f]
unsolveable_1tree2 =[r1,r2,r3,r4,r5,r6]
#3
r1 = [a,a,b,b,b,b]
r2 = [c,a,a,b,d,b]
r3 = [c,a,a,d,d,b]
r4 = [c,e,e,e,d,d]
r5 = [c,c,e,e,d,d]
r6 = [c,e,e,d,d,d]
unsolveable_1tree3 =[r1,r2,r3,r4,r5,r6]
#4
r1 = [a,a,b,b,b,b]
r2 = [c,a,a,b,d,b]
r3 = [c,a,a,d,d,b]
r4 = [c,e,e,e,d,d]
r5 = [c,c,e,e,d,d]
r6 = [c,e,e,d,d,d]
unsolveable_1tree4 =[r1,r2,r3,r4,r5,r6]
#5
r1 = [a,e,e,b,b,b,b]
r2 = [a,e,d,b,b,b,b]
r3 = [d,d,d,b,d,b,g]
r4 = [d,d,d,f,d,d,g]
r5 = [d,f,d,f,f,d,g]
r6 = [f,f,f,f,f,f,g]
r7 = [f,f,f,f,f,g,g]
unsolveable_1tree5 =[r1,r2,r3,r4,r5,r6,r7]

#2 tree
#1
r1 = [a,e,e,b,b,b,b,h,h]
r2 = [a,e,d,b,b,b,b,h,h]
r3 = [d,d,d,b,d,b,g,h,i]
r4 = [d,d,d,f,d,d,g,i,i]
r5 = [d,f,d,f,f,d,g,i,i]
r6 = [f,f,f,f,f,f,g,i,i]
r7 = [f,f,f,f,f,g,g,i,i]
r8 = [f,f,f,g,g,g,g,i,i]
r9 = [f,f,f,f,f,g,g,i,i]
unsolveable_2tree1 =[r1,r2,r3,r4,r5,r6,r7,r8,r9]
#2
r1 = [a,b,b,b,b,b,b,h,h]
r2 = [a,b,b,b,b,b,b,b,h]
r3 = [a,b,b,c,c,h,h,h,h]
r4 = [a,d,d,c,c,c,h,h,h]
r5 = [d,d,d,d,d,g,g,h,h]
r6 = [d,d,d,d,d,g,g,i,i]
r7 = [f,f,d,d,e,e,g,i,i]
r8 = [f,f,f,e,e,g,g,i,i]
r9 = [f,f,f,e,e,g,g,g,i]
unsolveable_2tree2 =[r1,r2,r3,r4,r5,r6,r7,r8,r9]
#3
r1 = [b,b,b,b,a,a,a,a,c]
r2 = [b,b,b,b,a,a,a,c,c]
r3 = [b,d,c,c,c,c,c,c,c]
r4 = [d,d,d,c,c,c,c,h,i]
r5 = [d,d,d,d,h,h,h,h,i]
r6 = [d,d,d,e,e,e,i,i,i]
r7 = [d,d,e,e,e,e,i,i,i]
r8 = [f,f,f,f,e,e,g,i,g]
r9 = [f,f,f,f,e,g,g,g,g]
unsolveable_2tree3 =[r1,r2,r3,r4,r5,r6,r7,r8,r9]


#sloveable:
#1
r1 = [a,a,a,b,b,b]
r2 = [a,c,a,a,b,b]
r3 = [a,c,a,b,b,d]
r4 = [c,c,e,e,b,d]
r5 = [c,e,e,f,f,d]
r6 = [c,f,f,f,d,d]
solveable_1tree1 =[r1,r2,r3,r4,r5,r6]
#2
r1 = [a,a,a,a,b,b]
r2 = [a,a,a,e,b,b]
r3 = [a,a,a,d,d,b]
r4 = [a,a,a,d,d,d]
r5 = [c,d,d,d,d,d]
r6 = [f,f,f,f,f,f]
solveable_1tree2 =[r1,r2,r3,r4,r5,r6]
#3
r1 = [a,a,b,b,e]
r2 = [a,a,d,b,e]
r3 = [d,d,d,b,b]
r4 = [d,d,d,d,d]
r5 = [c,c,c,c,d]
solveable_1tree3 =[r1,r2,r3,r4,r5]

#4
r1 = [a,b,b,b,b]
r2 = [a,b,b,b,b]
r3 = [a,b,e,e,e]
r4 = [a,a,e,d,d]
r5 = [c,c,c,c,d]
solveable_1tree4 =[r1,r2,r3,r4,r5]
#5
r1 = [a,e,e,b,b,b,b]
r2 = [a,e,c,b,b,b,b]
r3 = [c,c,c,b,b,b,g]
r4 = [c,c,c,f,d,d,g]
r5 = [c,f,c,f,f,d,g]
r6 = [f,f,f,f,f,f,g]
r7 = [f,f,f,f,f,g,g]
solveable_1tree5 =[r1,r2,r3,r4,r5,r6,r7]
#2 tree
#1
r1 = [a,b,b,b,b,b,b,h,h]
r2 = [a,b,b,b,b,b,b,h,h]
r3 = [a,b,b,c,c,h,h,h,h]
r4 = [a,d,d,c,c,c,h,h,h]
r5 = [d,d,d,d,d,g,g,h,h]
r6 = [d,d,d,d,d,g,g,i,i]
r7 = [f,f,d,d,e,e,g,i,i]
r8 = [f,f,f,e,e,g,g,i,i]
r9 = [f,f,f,e,e,g,g,g,i]
solveable_2tree1 =[r1,r2,r3,r4,r5,r6,r7,r8,r9]
#2
r1 = [b,b,b,b,a,a,a,a,c]
r2 = [b,b,b,b,a,a,a,c,c]
r3 = [b,d,c,c,c,c,c,c,c]
r4 = [d,d,d,c,c,c,c,h,i]
r5 = [d,d,d,d,h,h,h,h,i]
r6 = [d,d,d,e,e,e,i,i,i]
r7 = [d,d,e,e,e,e,i,i,i]
r8 = [f,f,f,f,e,e,g,g,g]
r9 = [f,f,f,f,e,g,g,g,g]
solveable_2tree2 =[r1,r2,r3,r4,r5,r6,r7,r8,r9]
#3
r1 = [b,b,b,b,b,a,a,a,a,a]
r2 = [b,b,b,b,b,b,b,a,a,a]
r3 = [b,d,d,d,d,d,b,a,i,a]
r4 = [c,c,c,c,c,d,d,a,i,a]
r5 = [c,j,j,j,d,d,d,i,i,i]
r6 = [c,j,j,j,j,j,j,h,h,i]
r7 = [f,f,e,e,e,e,g,h,h,i]
r8 = [f,f,e,e,e,e,g,h,h,g]
r9 = [f,f,e,e,g,g,g,g,g,g]
r0 = [f,f,f,f,f,f,f,f,f,g]
solveable_2tree3 =[r1,r2,r3,r4,r5,r6,r7,r8,r9,r0]

#2 tree
r1 = [a, b, b, b, b, b, c, c, c]
r2 = [a, a, b, c, b, c, c, c, c]
r3 = [a, a, a, c, c, c, d, c, e]
r4 = [a, c, c, c, f, d, d, d, e]
r5 = [f, f, c, f, f, d, e, e, e]
r6 = [f, f, f, f, f, e, e, e, e]
r7 = [g, f, f, g, h, e, e, e, e]
r8 = [g, f, g, g, h, i, i, i, e]
r9 = [g, g, g, h, h, h, h, e, e]


r1 = [a, a, b, b, b, b, c, d, d, d]
r2 = [a, a, a, b, c, c, c, c, d, d]
r3 = [a, b, b, b, c, e, c, d, d, d]
r4 = [a, b, b, e, e, e, e, d, f, d]
r5 = [a, f, f, g, e, g, f, d, f, d]
r6 = [a, f, f, g, g, g, f, f, f, h]
r7 = [a, a, f, f, g, f, f, i, h, h]
r8 = [a, a, a, f, f, f, j, i, h, h]
r9 = [a, a, a, j, j, j, j, i, h, h]
r10 = [i, i, i, i, i, i, i, i, i, h]


r1 = [a, a, a, a, b, b, b, b, b, b]
r2 = [a, b, a, a, b, b, b, b, b, b]
r3 = [b, b, b, b, c, b, b, d, d, b]
r4 = [b, b, b, b, c, c, b, e, d, d]
r5 = [b, c, c, c, c, c, c, e, d, d]
r6 = [b, b, f, f, c, f, e, e, d, d]
r7 = [b, f, f, f, f, f, f, e, d, d]
r8 = [b, g, g, h, f, f, e, e, i, d]
r9 = [g, g, h, h, h, i, i, i, i, d]
r10 = [g, g, h, h, i, i, i, i, i, i]


#1 tree
r1 = [a, a, a, a, b, b, b, b]
r2 = [a, c, c, a, a, b, b, b]
r3 = [a, d, c, c, c, b, b, e]
r4 = [d, d, d, f, c, e, b, e]
r5 = [g, g, g, f, c, e, b, e]
r6 = [g, g, f, f, c, e, e, e]
r7 = [h, h, c, c, c, e, e, e]
r8 = [h, h, h, c, c, c, c, c]

r1 = [a, a, a, b, b, c, d]
r2 = [e, a, a, b, c, c, d]
r3 = [e, e, a, b, a, d, d]
r4 = [f, f, a, a, a, d, g]
r5 = [f, a, a, d, d, d, g]
r6 = [f, a, a, d, d, d, d]
r7 = [a, a, d, d, d, d, d]

r1 = [a, a, b, b, b, b]
r2 = [a, a, a, b, b, b]
r3 = [a, a, a, a, c, b]
r4 = [d, a, a, c, c, c]
r5 = [d, e, e, e, f, c]
r6 = [d, d, e, e, f, f]