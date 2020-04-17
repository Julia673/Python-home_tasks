# task 1 

def enumerate(iterable,start=0):

     for indx in range(start,len(iterable)):
         print(iterable[indx])

enumerate([1,2,3,4,5],2)

# task 2
def in_range(start ,end,step=1):
    r=[]
    if step>0:
      while start<=end:
        r.append(start)
        start+=step
        
      return r
    elif step<0:
      while start>=end:
        r.append(start)
        start+=step
      return r
    else :
        return r

print(in_range(0,9))

#task 3
    
func = lambda *args: args
print(func(9,8,7,6,5,4,3,2,1,0))
def function(itterator):
    print([itterator[i] for i in range(len(itterator))])
function([9,8,7,6,5,4,3,2,1,0])

