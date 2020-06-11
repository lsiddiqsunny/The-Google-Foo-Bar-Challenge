def find(item,par,shift):
    right_node=par-1
    left_node=right_node-shift//2

    if(right_node==item or left_node==item):
        return par
    else:
        if(item<=left_node):
            return find(item,left_node,shift//2)
        else:
            return find(item,right_node,shift//2)

def solution(h, q):
    top=(2**h)-1

    p=[]
    for i in range(len(q)):
        if (q[i]<top and q[i]>0):
            p.append(find(q[i],top,top-1))
        else:
            p.append(-1)
    return p