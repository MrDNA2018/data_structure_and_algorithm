# -*- coding: utf-8 -*-

#%%
def constraint():
    return True

def bound():
    return True

def perm_backtracking(depth,lst):
    size = len(lst)
    
    if depth == size:
        print(lst)
    else:
        for i in range(depth,size):          
            if constraint() and bound():
                lst[depth],lst[i] = lst[i],lst[depth]
                perm_backtracking(depth+1,lst)
                lst[depth],lst[i] = lst[i],lst[depth]
                
def perm_backtracking_iteration2(depth,lst):
    size = len(lst)
    Selected =[i for i in range(size)]
    change = [-1]*size   
    count = 0
    
    while depth >=0:
        
        if Selected[depth] < size:
            
            for i in range(Selected[depth],size):
                
                lst[depth],lst[i] = lst[i],lst[depth]
                change[depth] = i
                
                Selected[depth] +=1
                
                if depth == size-1:
                    count +=1
                    print (lst)
                    print (count)

                else:                    
                    depth +=1
                    Selected[depth] = depth
                    break
        else:
            depth -=1  
            lst[depth],lst[change[depth]] = lst[change[depth]],lst[depth]
            change[depth] = -1
            
            



    
def perm_backtracking_iteration(depth,lst):
    size = len(lst)
    Selected =[-1]*size
    
    def place(k):
        for i in range(k):
            if Selected[i] == Selected[k]:
                return False
        return True
    

    
    while depth >=0:
        
        Selected[depth] +=1
        while Selected[depth]<size and not place(depth):
            Selected[depth] +=1
        
        if Selected[depth] <= size-1:
            if depth == size-1:
#                print Selected
                for i in Selected:
                    print (lst[i],end =' ')
                print (end = "\n")
            else:
                depth +=1
                Selected[depth] =-1
        else:
            depth -=1


        
      
A = ['A','B','C','D']
#perm_backtracking(0,A)
perm_backtracking_iteration2(0,A)
#%%

class FlowShop:
    def __init__(self,N,mission):   
        self.N = N
        self.mission = mission
        self.bestFinishtime = 10000
        self.schedule = [i for i in range(N)]
        self.bestSchedule = [0]*N
        self.f2 = [0]*N
        self.f1 =0
        self.totaltime = 0
        self.depth = 0
    
    def back_tracking(self,depth):
        if depth > self.N-1:
            self.bestFinishtime = self.totaltime
            self.bestSchedule[:] = self.schedule[:]
            return 
        else:
            for i in range(depth,self.N):
                self.f1 +=self.mission[0][self.schedule[i]]
                if depth ==0:
                    self.f2[depth] = self.f1 + self.mission[1][self.schedule[i]]
                else:
                    self.f2[depth] = max(self.f1,self.f2[depth-1]) + self.mission[1][self.schedule[i]]
                    
                self.totaltime += self.f2[depth]
                
                if self.totaltime < self.bestFinishtime:
                    self.schedule[i],self.schedule[depth] = self.schedule[depth],self.schedule[i]
                    self.back_tracking(depth+1)
                    self.schedule[i],self.schedule[depth] = self.schedule[depth],self.schedule[i]
                    
                self.f1 -=self.mission[0][self.schedule[i]]
                self.totaltime -= self.f2[depth]
            
    def print_back_tracking(self):
        self.back_tracking(self.depth)
        print (self.bestSchedule)
        print (self.bestFinishtime)
        
        
    
            
N = 6
mission = [[2,3,2,4,5,7],[1,1,3,2,3,4]]       
instance = FlowShop(N,mission)
instance.print_back_tracking()
            
#%%


class Nqueen:
    def __init__(self,N):
        self.N = N
        self.sum = 0
        self.solution = [-1]*N
        self.solutionlist = []
        self.depth = 0
        
    def place(self,k):
        for i in range(k):
            if abs(k-i) == abs(self.solution[k]-self.solution[i]) or self.solution[k]==self.solution[i]:
                return False
        return True
        
    def back_tracking(self,depth):
        if depth > N-1:
            self.sum +=1
#            print self.solution
            self.solutionlist += [self.solution[:]]
        else:
            for i in range(N):
                self.solution[depth] = i
                if self.place(depth):
                    self.back_tracking(depth+1)
                self.solution[depth] = -1
            
    def output_nQueen(self):
        self.back_tracking(self.depth)
        return self.solutionlist,self.sum    

if __name__ =='__main__':    
    N=4
    nqueen = Nqueen(N)
    list,sum =nqueen.output_nQueen()
    print list
    print sum
        
#%%

class Nqueen2:
    def __init__(self,N):
        self.N = N
        self.sum = 0
        self.solution = [-1]*N
        self.solutionlist = []
        self.depth = 0
        
    def place(self,k):
        for i in range(k):
            if abs(k-i) == abs(self.solution[k]-self.solution[i]) or self.solution[k]==self.solution[i]:
                return False
        return True
        
    def back_tracking_iteration(self):
        
        
        while self.depth >=0:
            
            self.solution[self.depth] +=1
            
            while self.solution[self.depth] < self.N and not self.place(self.depth):
                self.solution[self.depth] +=1
            
            if self.solution[self.depth] <= N-1:
                if self.depth == N-1:
                    self.sum += 1
                    self.solutionlist += [self.solution[:]]
                else:
                    self.depth +=1
                    self.solution[self.depth] =-1
            else:
                self.depth -=1

                
  
            
    def output_nQueen(self):
        self.back_tracking_iteration()
        return self.solutionlist,self.sum    

if __name__ =='__main__':    
    N=4
    nqueen = Nqueen2(N)
    list,sum =nqueen.output_nQueen()
    print list
    print sum
                
           