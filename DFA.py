from tabnanny import check
import pydot
import os
import matplotlib.pyplot as plot
from PIL import Image
os.environ["PATH"] += os.pathsep+"C:\Program Files\Graphviz\bin"

class Infix_to_Postfix():

    def __init__(self):
        self.top = 0
        self.stack = []
        self.stack.append("(")
        self.postfix = ""
        self.rank = 0
        self.PRECEDENCE_F = {'+': 1, '.': 3,'*': 5, 'oprand': 7, '(': 9, ')': 0}
        self.PRECEDENCE_G = {'+': 2, '.': 4, '*': 6, 'oprand': 8, '(': 0}
        self.RANK = {'+': -1, '.': -1, '*': 0, 'oprand': 1, '(': 0, ')': 0}

    def is_oprand(self, char):
        if(str(char).isalpha()):
            return True
        else:
            return False

    def pop(self):
        c = self.stack[self.top]
        self.stack.pop(self.top)
        self.top -= 1
        return(c)

    def push(self, c):
        self.stack.append(c)
        self.top += 1

    def get_values(self, c, stack_top):
        if(self.is_oprand(c)):
            next = 'oprand'
        else:
            next = c
        if(self.is_oprand(stack_top)):
            stacktop = 'oprand'
        else:
            stacktop = stack_top
        return(next, stacktop)

    def Postfix(self, infix_expression):
        infix_expression += ')'
        for c in infix_expression:
            if(str(c).isdigit()):
                return False
            while(True):
                if self.top < 0:
                    return(False)
                next, stacktop = self.get_values(c, self.stack[self.top])
                f = self.PRECEDENCE_F[next]
                g = self.PRECEDENCE_G[stacktop]
                if(f < g):
                    stacktop = self.pop()
                    self.postfix += stacktop
                    _, stacktop = self.get_values(" ", stacktop)
                    self.rank += self.RANK[stacktop]
                else:
                    break
            if(self.top > 0):
                next, stacktop = self.get_values(c, self.stack[self.top])
            if(self.PRECEDENCE_F[next] != self.PRECEDENCE_G[stacktop]):
                self.push(c)
            else:
                _ = self.pop()
        if(self.top!=-1 or self.rank!=1):
            return(False)
        else:
            return(True)

class Deterministic_Finite_Automata_Method_1():

    def __init__(self, postfix_expersion):

        self.stack = []   # stack ~ evalution of post fix  
        self.top = -1
        self.oprand = []    # Number of oprand which used to change state or for transection

        self.Traversal_path=[]

        self.NFA_NULL = {}
        self.NFA = {}
        self.DFA = {}
        self.MINIMIZED_DFA={}

        self.state_list={}

        self.Initial_NFA_NULL=""
        self.Initial_NFA=""
        self.Initial_DFA=""
        self.Initial_MINIMIZED_DFA=""

        self.Accepted_NFA_NULL=""
        self.Accepted_NFA=""
        self.Accepted_DFA=""
        self.Accepted_MINIMIZED_DFA=""

        self.postfix_expersion = postfix_expersion

    def push(self, c):
        self.stack.append(c)
        self.top += 1

    def pop(self):
        c = self.stack[self.top]
        self.stack.pop(self.top)
        self.top -= 1
        return(c)

    def NFA_NULL_FUNCTION(self):
        input_state = 0
        output_state = 0
        number_of_state = 0
        
        for i in self.postfix_expersion:
            if(i == '+' or i == '*'):
                number_of_state += 1
            if(i.isalpha()):
                number_of_state += 2

        for i in range(0, number_of_state):
            self.NFA_NULL['q'+str(i+1)] = {}
            self.NFA['q'+str(i+1)] = {}

        for c in self.postfix_expersion:
            
            if(c.isalpha()):
                if c not in self.oprand:
                    self.oprand.append(c)
                    
                input_state = output_state+1 
                output_state += 2 

                self.NFA_NULL['q'+str(input_state)][c] = []
                self.NFA_NULL['q'+str(input_state)]['accepted'] = []
                self.NFA_NULL['q'+str(input_state)][c].append('q'+str(output_state))
                self.NFA_NULL['q'+str(input_state)]['accepted'].append('q'+str(output_state))
                self.push('q'+str(input_state))
            
            if(c == '+'):
                input_state = output_state+1
                output_state += 1
                self.NFA_NULL['q'+str(input_state)]['N'] = []
                self.NFA_NULL['q'+str(input_state)]['accepted'] = []
                state=self.pop()
                self.NFA_NULL['q'+str(input_state)]['N'].append(state)
          
                for s in self.NFA_NULL[state]['accepted']:
                    if s not in self.NFA_NULL['q'+str(input_state)]['accepted']: 
                        self.NFA_NULL['q'+str(input_state)]['accepted'].append(s)
          
                self.NFA_NULL[state]['accepted'].clear()
                state= self.pop()
                self.NFA_NULL['q'+str(input_state)]['N'].append(state)
          
                for s in self.NFA_NULL[state]['accepted']:
                    if s not in self.NFA_NULL['q'+str(input_state)]['accepted']: 
                        self.NFA_NULL['q'+str(input_state)]['accepted'].append(s)
          
                self.NFA_NULL[state]['accepted'].clear()
                self.push('q'+str(input_state))

            if(c=='.'):
                state2=self.pop()
                state1=self.pop()
                for s in self.NFA_NULL[state1]['accepted']:
                    if 'N' not in list(self.NFA_NULL[s].keys()):
                        self.NFA_NULL[s]['N']=[]
                    self.NFA_NULL[s]['N'].append(state2)
          
                self.NFA_NULL[state1]['accepted'].clear()
          
                for s in self.NFA_NULL[state2]['accepted']:
                    if s not in self.NFA_NULL[state1]['accepted']:
                        self.NFA_NULL[state1]['accepted'].append(s)
                self.NFA_NULL[state2]['accepted'].clear()
                self.push(state1)
                
            if(c=='*'):
                input_state=output_state+1
                output_state+=1
                self.NFA_NULL['q'+str(input_state)]['N']=[]
                self.NFA_NULL['q'+str(input_state)]['accepted']=[]
                state=self.pop()
                self.NFA_NULL['q'+str(input_state)]['N'].append(state)
              
                for s in self.NFA_NULL[state]['accepted']:
                    if 'N' not in list(self.NFA_NULL[s].keys()):
                        self.NFA_NULL[s]['N']=[]
                    self.NFA_NULL[s]['N'].append('q'+str(input_state))
              
                self.NFA_NULL['q'+str(input_state)]['accepted'].append('q'+str(input_state))
                self.NFA_NULL[state]['accepted'].clear()
                self.push('q'+str(input_state))

        self.Initial_NFA_NULL=self.stack[self.top]        
        self.Accepted_NFA_NULL=self.NFA_NULL[self.Initial_NFA_NULL]['accepted'].copy()
        
    def find_NULL(self,states,nlist):
        for s in states:
            if s not in nlist:
                nlist.append(s)
                if 'N' in list(self.NFA_NULL[s].keys()):
                    nlist=self.find_NULL(self.NFA_NULL[s]['N'],nlist)
        return(nlist)
    
    def delta_fun(self,states,op):
        out=[]
        for s in states:
            if op in list(self.NFA_NULL[s].keys()):
                for i in self.NFA_NULL[s][op]:
                    out.append(i)
        return(out) 
    
    def union(self,l1,l2):
        return(list(set(l1+l2)))

    def intersection(self,l1,l2):
        return(list(set(l1)&set(l2)))
    
    def NFA_FUNCTION(self):
        
        for state in self.NFA_NULL:
            self.NFA[state]['N']=[]
            if 'N' not in list(self.NFA_NULL[state].keys()):
                self.NFA[state]['N'].append(state)
            else:
                for s in self.NFA_NULL[state]['N']:
                    if s not in self.NFA[state]['N']:
                        self.NFA[state]['N'].append(s)
                        if 'N' in list(self.NFA_NULL[s].keys()):
                            self.find_NULL(self.NFA_NULL[s]['N'],self.NFA[state]['N'])
                if state not in self.NFA[state]['N']:
                    self.NFA[state]['N'].append(state)

        for state in self.NFA_NULL:
            for key in self.oprand:
                l=self.delta_fun(self.NFA[state]['N'],key)
                self.NFA[state][key]=self.find_NULL(l,[])
  
            if 'accepted' in list(self.NFA_NULL[state].keys()):
                self.NFA[state]['accepted']=self.NFA_NULL[state]['accepted'].copy()

        l=self.intersection(self.NFA[self.stack[self.top]]['N'],self.NFA[self.stack[self.top]]['accepted'])    
        if(len(l)>0):
            if self.stack[self.top] not in self.NFA[self.stack[self.top]]['accepted']:
                self.NFA[self.stack[self.top]]['accepted'].append(self.stack[self.top])
        self.Initial_NFA=self.stack[self.top]        
        self.Accepted_NFA=self.NFA[self.Initial_NFA]['accepted'].copy()
        
    def rebuild_DFA(self,dict):
        new_state_list=[]
        state_list=[]
        for i in range(0,len(dict)):
            new_state_list.append('q'+str(i))
            state_list.append(list(dict.keys())[i])
        new_Dict={}
        i=0
        for state in state_list:
            new_Dict[new_state_list[i]]={}
            for op in list(dict[state].keys()):
                new_Dict[new_state_list[i]][op]=[]
                for j in dict[state][op]:
                    new_Dict[new_state_list[i]][op].append(new_state_list[state_list.index(j)])
            i+=1
        return(new_state_list,new_Dict)
    
    def DFA_FUNCTION(self):
        
        check_list=[[self.stack[self.top]]]
        state_list=[self.stack[self.top]]
        j=0
        dead_state=False
        while True:
            self.DFA[state_list[j]]={}
            for op in self.oprand:
                self.DFA[state_list[j]][op]=[]
                str1=""
                l=[]
                for k in check_list[j]:
                    if op in list(self.NFA[k].keys()):
                        for i in self.NFA[k][op]:
                            if i not in str1:
                                str1+=i
                                l.append(i)
                if(len(l)<1):
                    self.DFA[state_list[j]][op].append('D')
                    dead_state=True
                else:    
                    self.DFA[state_list[j]][op].append(str1)
                if(str1 not in state_list and len(l)>=1):
                    state_list.append(str1)
                    check_list.append(l)

            for s in self.NFA[self.stack[self.top]]['accepted']:
                if s in state_list[j]:
                    if 'accepted' not in list(self.DFA[self.stack[self.top]].keys()):
                        self.DFA[self.stack[self.top]]['accepted']=[]
                    if state_list[j] not in self.DFA[self.stack[self.top]]['accepted']:
                        self.DFA[self.stack[self.top]]['accepted'].append(state_list[j])
            j+=1
            if(j==len(state_list)):
                break
        
        if(dead_state):    
            self.DFA['D']={}
            for op in self.oprand:
                self.DFA['D'][op]=[] 
                self.DFA['D'][op].append('D')
            state_list.append('D')
        self.state_list,self.DFA=self.rebuild_DFA(self.DFA)
        self.state_list=self.state_list.copy()
        self.DFA=self.DFA.copy()
        self.Initial_DFA='q0'        
        self.Accepted_DFA=self.DFA['q0']['accepted'].copy()
        
    
    def MINIMIZATION_FUNCTION(self):
        
        minimization_matrix=[]
        self.MINIMIZED_DFA={}
        
        for state in self.DFA:
            self.MINIMIZED_DFA[state]={}
            for op in self.DFA[state]:
                self.MINIMIZED_DFA[state][op]=self.DFA[state][op].copy()
        
        for i in range(1,len(self.state_list)):
            l=[]
            for j in range(0,i):
                l.append(0)
            minimization_matrix.append(l)
    
        for i in range(1,len(self.state_list)):
            for j in range(0,i):
                if('q'+str(j) in self.MINIMIZED_DFA['q0']['accepted'] and 'q'+str(i) in self.MINIMIZED_DFA['q0']['accepted']):
                    continue
                if('q'+str(j) in self.MINIMIZED_DFA['q0']['accepted'] or 'q'+str(i) in self.MINIMIZED_DFA['q0']['accepted']):
                    minimization_matrix[i-1][j]=1
        
        exit_check=True
        k=2
        while(True): 
            exit_check=True
            for i in range(1,len(self.state_list)):
                for j in range(0,i):
                    if(minimization_matrix[i-1][j]==0):
                        for op in self.oprand:
                            i1=self.state_list.index(self.MINIMIZED_DFA['q'+str(i)][op][0])
                            i2=self.state_list.index(self.MINIMIZED_DFA['q'+str(j)][op][0])
                            if(i1==i2):
                                continue
                            else:
                                if(i1>i2):
                                    if(minimization_matrix[i1-1][i2]==0):
                                        continue
                                    else:
                                        exit_check=False
                                        minimization_matrix[i-1][j]=k
                                else:
                                    if(minimization_matrix[i2-1][i1]==0):
                                        continue
                                    else:
                                        exit_check=False
                                        minimization_matrix[i-1][j]=k
            k=k+1
            if(exit_check):
                break
        combine=[]
        
        for i in range(1,len(self.state_list)):
            for j in range(0,i):
                if(minimization_matrix[i-1][j])==0:
                    combine.append([i,j])
        i=0
        j=1
            
        while True:
            if len(combine)<2:
                break
            while(j<len(combine)):
                l=self.intersection(combine[i],combine[j])
                if(len(l)>0):
                
                    l=self.union(combine[i],combine[j])
                    l1=combine[i]
                    l2=combine[j]
                    combine.remove(l1)
                    combine.remove(l2)
                    combine.append(l)
                    i=0
                    j=1
                    break
                else:
                    j+=1
            else:
                i+=1
                j=i+1

                
            if(i==len(combine)):
                break
            
        combine_state=[]
        str_combine_state=[]
    
        for i in combine:
            x=[]
            for j in i:
                x.append('q'+str(j))
            combine_state.append(x)
            str_combine_state.append(''.join(x))
   
   
        for i in range(0,len(combine_state)):
            self.MINIMIZED_DFA[str_combine_state[i]]={}
            for state in self.MINIMIZED_DFA:
                if state not in combine_state[i]:
                    for key in self.MINIMIZED_DFA[state]:
                        for s in combine_state[i]:
                            if s in self.MINIMIZED_DFA[state][key]:
                                self.MINIMIZED_DFA[state][key].remove(s)
                                if str_combine_state[i] not in self.MINIMIZED_DFA[state][key]:
                                    self.MINIMIZED_DFA[state][key].append(str_combine_state[i])
                else:
                    for key in self.MINIMIZED_DFA[state]:
                        if key not in list(self.MINIMIZED_DFA[str_combine_state[i]].keys()):
                            self.MINIMIZED_DFA[str_combine_state[i]][key]=[]
                        for s in self.MINIMIZED_DFA[state][key]:
                            if s not in combine_state[i]:
                                if s not in self.MINIMIZED_DFA[str_combine_state[i]][key]:
                                    self.MINIMIZED_DFA[str_combine_state[i]][key].append(s)
                            else:
                                if str_combine_state[i] not in self.MINIMIZED_DFA[str_combine_state[i]][key]:  
                                    self.MINIMIZED_DFA[str_combine_state[i]][key].append(str_combine_state[i])
        for i in combine_state:
            for s in i: 
                del self.MINIMIZED_DFA[s]
        NEW_DFA={}
        for state in self.MINIMIZED_DFA:
            if 'accepted' in list(self.MINIMIZED_DFA[state].keys()):
                NEW_DFA[state]=self.MINIMIZED_DFA[state].copy()
                break
        
        for state in self.MINIMIZED_DFA:
            if 'accepted' not in list(self.MINIMIZED_DFA[state].keys()):
                NEW_DFA[state]=self.MINIMIZED_DFA[state].copy()
        
        self.state_list,self.MINIMIZED_DFA=self.rebuild_DFA(NEW_DFA) 
        self.Initial_MINIMIZED_DFA='q0'        
        self.Accepted_MINIMIZED_DFA=self.MINIMIZED_DFA['q0']['accepted'].copy()  

class Deterministic_Finite_Automata_Method_2():
    
    class Tree:
        
        def __init__(self,value,op_no,left,right,first,nullable):
    
            self.value=value
            self.oprand_no=op_no
            self.left=left
            self.right=right
            self.first=first
            self.nullable=nullable
            if(value=='#'):
                self.follow=[None]
    
    def __init__(self,postfix_exp):
    
        self.postfix_expression=postfix_exp
        self.oprands=[]
        self.oprands_no={}
        self.first_follow={}
        self.parse_tree_root=None
        self.initial_state=["q0"]
        self.accepted_states=[]
        self.states={}
        self.DFA={}
        self.minimized_DFA={}
        self.minimized_accepted_states={}
        
    def parse_tree(self):

        self.postfix_expression+='#.'
        stack=[]
        op_no=1
        
        for c in self.postfix_expression:

            if c=='+' or c=='.':
        
                node1=stack.pop()
                node2=stack.pop()
                node=self.Tree(c,None,node2,node1,[],False)
                self.find_first(c,node)
                stack.append(node)
            
            elif c=='*':
        
                node1=stack.pop()
                node=self.Tree(c,None,node1,None,[],True)
                self.find_first(c,node)
                stack.append(node)
                
            elif c.isalpha() or c=='#':
      
                if c not in self.oprands:
                    self.oprands.append(c)
                    self.oprands_no[c]=[op_no]
                else:
                    self.oprands_no[c].append(op_no)
                
                self.first_follow[op_no]={"oprand":c}
                stack.append(self.Tree(c,op_no,None,None,[op_no],False))
                op_no+=1
    
        root=stack.pop()
        
        self.find_follow(root.left,[{"node":root,"rchild":True}])
        self.first_follow[op_no-1]["first"]=root.right.first[:]
        self.first_follow[op_no-1]["follow"]=root.right.follow[:]
        
        if(len(stack)!=0):
            return None
        else:
            self.parse_tree_root=root
            return root
        
    def find_first(self,c,root):
   
        if(c=='+'):
            root.first=root.left.first[:]+root.right.first[:]
            if(root.left.nullable or root.right.nullable):
                root.nullable=True
  
        elif(c=='.'):
            if(root.left.nullable):
                root.first=root.left.first[:]+root.right.first[:]
            else:
                root.first=root.left.first[:]
            if(root.left.nullable and root.right.nullable):
                root.nullable=True
  
        else:
            root.first=root.left.first[:]

    def find_follow(self,root,stack):
        
        if(root.left==None and root.right==None):
        
            temp=[]
            follow=[]
           
            while(len(stack)!=0):
                node=stack.pop()
                temp.append(node)
           
                if(node["node"].value=='*'):
                    follow=follow+node["node"].left.first[:]
           
                elif(node["node"].value=='.'):
                    if(node["node"].right.value=='*'):
                        follow=follow+node["node"].right.left.first[:]
                        continue
                    if(node["rchild"]):
                        continue
                    else:
                        break
            
            follow=follow+node["node"].right.first[:]
            root.follow=list(set(follow[:]))
            
            while(len(temp)!=0):
                stack.append(temp.pop())
        
            self.first_follow[root.oprand_no]["first"]=root.first[:]
            self.first_follow[root.oprand_no]["follow"]=root.follow[:]
        
        if(root.left!=None):
      
            stack.append({"node":root,"rchild":False})
            self.find_follow(root.left,stack)
            stack.pop()
            
        if(root.right!=None):
      
            stack.append({"node":root,"rchild":True})
            self.find_follow(root.right,stack)
            stack.pop()
    
    def find_dfa(self):
    
        DFA={}
        states={}
        accepted_states=[]
        DFA["q0"]={}
        dead=True
        count=0
        states["D"]=[]
        states["q0"]=self.parse_tree_root.first
        queue=["q0"]
        
        while(len(queue)!=0):
        
            state=queue.pop()

            for op in self.oprands:
                
                follow_states=[]

                l=list(set(self.oprands_no[op])&set(states[state]))
                for i in l:
                    follow_states=follow_states+self.first_follow[i]["follow"][:]
             
                if(state not in list(DFA.keys())):
                    DFA[state]={}
        
             
                if(len(follow_states)==0 or None in follow_states):
             
                    if(None in follow_states):
                        accepted_states.append(state)
                        continue
                  
                    if(dead and op!='#'):
                        DFA['D']={}
                        for ops in self.oprands:
                            if ops=='#':
                                continue
                            DFA['D'][ops]='D'
                        dead=False
                
                    if op!='#':                  
                        DFA[state][op]=['D']
                  
                    continue
                
                if(follow_states not in list(states.values())):
                    
                    count+=1
                    states['q'+str(count)]=follow_states
                    queue.append('q'+str(count))

                key=list(states.keys())
                value=list(states.values())
                
                DFA[state][op]=[key[value.index(follow_states)]]
        
        return self.rebuild_DFA(DFA,accepted_states,states)
    
    def minimize_dfa(self,DFA,accepted_states,reduced=False):

        combine=[]
        key=list(DFA.keys())
        for i in range(0,len(key)):
            for j in range(i+1,len(key)):
                if DFA[key[i]]==DFA[key[j]] and ( (key[i] in accepted_states and key[j] in accepted_states) or (key[i] not in accepted_states and key[j] not in accepted_states) ):
                    combine.append([key[i],key[j]])
        
        if len(combine)==0:
            return DFA,accepted_states,reduced
        
        i=0
        j=1

        while True:
            if len(combine)<2:
                break
            while(j<len(combine)):
                l=list(set(combine[i]) & set(combine[j]))
                if(len(l)>0):
                    l=list(set(combine[i]+combine[j]))
                    l1=combine[i]
                    l2=combine[j]
                    combine.remove(l1)
                    combine.remove(l2)
                    combine.append(l)
                    i=0
                    j=1
                    break
                j+=1
            else:
                i+=1
                j=i+1
            if(i==len(combine)):
                break
        
        str_combine_state=[]
        
        for i in combine:
            str_combine_state.append(''.join(i))
        
        for i in range(0,len(combine)):
            if combine[i][0] in accepted_states:
                accepted_states.append(str_combine_state[i])
            DFA[str_combine_state[i]]={}
            for state in DFA:
                if state not in combine[i]:
                    for key in DFA[state]:
                        for s in combine[i]:
                            if s in DFA[state][key]:
                                DFA[state][key]=[]
                                if str_combine_state[i] not in DFA[state][key]:
                                    DFA[state][key].append(str_combine_state[i])
                else:
                    for key in DFA[state]:
                        if key not in list(DFA[str_combine_state[i]].keys()):
                            DFA[str_combine_state[i]][key]=[]
                        for s in DFA[state][key]:
                            if s not in combine[i]:
                                if s not in DFA[str_combine_state[i]][key]:
                                    DFA[str_combine_state[i]][key].append(s)
                            else:
                                if str_combine_state[i] not in DFA[str_combine_state[i]][key]:  
                                    DFA[str_combine_state[i]][key].append(str_combine_state[i])
        for i in combine:
            for s in i:
                del DFA[s]
                if s in accepted_states:
                    accepted_states.remove(s)
        
        return self.minimize_dfa(DFA,accepted_states,True)
        
    def rebuild_DFA(self,DFA,accepted_states,s):

        new_DFA={}
        new_state_list=[]
        state_list=[]
        new_accepted_states=[]
        states={}
   
        for i in range(0,len(DFA)):
            new_state_list.append('q'+str(i))
            state_list.append(list(DFA.keys())[i])
        
        i=0
        for state in state_list:
            new_DFA[new_state_list[i]]={}
            for op in list(DFA[state].keys()):
                new_DFA[new_state_list[i]][op]=[]
                new_DFA[new_state_list[i]][op].append(new_state_list[state_list.index(DFA[state][op][0])])
            
            if(state in accepted_states):
                new_accepted_states.append(new_state_list[i])

            if state in list(s.keys()): 
                states[new_state_list[i]]=s[state]

            i+=1
        
        return(new_accepted_states,new_DFA,states)                        
                      
def SHOW_AUTOMATA(DFA,accepted_state,show,color_codes=['white',"#E3F9A6","#6AFB92","#93FFE8"],file_name="output"):
        
    graph = pydot.Dot('my_graph', graph_type='digraph', bgcolor=color_codes[0], rankdir="LR")
    
    graph.add_node(pydot.Node('I/P',lable='I/P',shape='circle',color=color_codes[1],style="filled"))
    
    for s in list(DFA.keys()):
        if (s in accepted_state):
            graph.add_node(pydot.Node(s,lable=s,shape='doublecircle',color=color_codes[2],style="filled"))
        else:
            graph.add_node(pydot.Node(s,lable=s,shape='circle',color=color_codes[3],style="filled"))    
            
    for state in DFA:
        for key in DFA[state]:
            if key!='accepted':
                graph.add_edge(pydot.Edge(state,DFA[state][key][0],color=color_codes[2],label=key,labelfontcolor="#E41B17",labeldistance=2,labelangle=0))
    graph.add_edge(pydot.Edge('I/P','q0',color=color_codes[2],label='^',labelfontcolor="#E41B17",labeldistance=2,labelangle=0))
    graph.write_png("Output_Images/"+file_name+".png")
    if(show):
        im = Image.open(r"Output_Images/output.png")
        im.show()
    

if __name__=="__main__":
    print("\n\n\n")
    print('*'*182)
    print("*** Note : Follow the below rules for RE ***".center(182),end="\n\n")
    print(" "*70," ---> 1. for Union use '+' Ex. a+b ")
    print(" "*70," ---> 2. for concatenation use '.' Ex. a.b ")
    print(" "*70," ---> 3. for Kleene use '*' Ex a*")
    print(" "*70," ---> Example of input : (a+b)*",end="\n\n")
    
    # infix=input(str(" "*68)+" >>>> Enter yout RE (Regular exprestion) : ")
    
    
    In=Infix_to_Postfix()
    # valid=In.Postfix(infix)
    # valid=In.Postfix("a+b*")
    # valid=In.Postfix("(a+b)*.a.b.b")
    valid=In.Postfix("(b+c*+d)*+c")
    # valid=In.Postfix("(a+b)*.b.a*.b.a*")
    # valid=In.Postfix("a.b.c")
    if valid:
        method1=Deterministic_Finite_Automata_Method_1(In.postfix)
        method2=Deterministic_Finite_Automata_Method_2(In.postfix)
    
        method2.parse_tree_root=method2.parse_tree()
        
        if(method2.parse_tree_root==None):
            print("Error")
        else:
            method2.accepted_states,method2.DFA,method2.states=method2.find_dfa()

        d,a,valid=method2.minimize_dfa(method2.DFA.copy(),method2.accepted_states.copy())
        if valid:
            method2.minimized_accepted_states,method2.minimized_DFA,_=method2.rebuild_DFA(d,a,{})
        # method1.NFA_NULL_FUNCTION()
        # method1.NFA_FUNCTION()
        # method1.DFA_FUNCTION()
        # method1.MINIMIZATION_FUNCTION()
        print()
        SHOW_AUTOMATA(method2.minimized_DFA,method2.minimized_accepted_states,True)

    else:
        print("\n")
        print(" Invalid Regular exprestion !!".center(182))
        print("\n")
    print('*'*182)
    print("\n\n\n")


  # def post(self,root):
        #     if(root.left!=None and root.right!=None):
        #         print("root : ",root.value," | l : ",root.left.value,"| r : ",root.right.value," | first : ",root.first," | follow : ",root.follow)
        #     elif(root.left!=None):
        #         print("root : ",root.value," | l : ",root.left.value,"| r : None"," | first : ",root.first," | follow : ",root.follow)
        #     elif(root.right!=None): 
        #         print("root : ",root.value," | l : ",None,"| r : ",root.right.value," | first : ",root.first," | follow : ",root.follow)
        #     else:
        #         print("root : ",root.value," | l : ",None,"| r : None"," | first : ",root.first," | follow : ",root.follow)
        #     if(root.left!=None): 
        #         self.post(root.left)
        #     if(root.right!=None):
        #         self.post(root.right)