import random
from DFA import *
from time import perf_counter_ns
from matplotlib import pyplot as plot

class Deterministic_Finite_Automata:    
    
    def __init__(self,regular_expression) -> None:
        self.regular_expression=regular_expression
        self.DFA={}
        self.accepted_states=[]
        self.light=["#C7F6EC","#DBF9DB","#8467D7","#4DD8AD"] #[back,createoutlin,out,fill]
        self.dark=["#014751","#4863A0","#00D37F","#D2EFF5"]
        self.Plot_light=["#C7F6EC","#02231C","#8467D7","#DBF9DB"]
        self.Plot_dark=["#014751","#FFEEB4","#00D37F","#4863A0"]
        
    def get_postfix(self):
        In=Infix_to_Postfix()
        self.valid=In.Postfix(self.regular_expression)
        self.post_fix=In.postfix
    
    def copy_data(self,mydict,data,dict_key,oprand,key_null=False):
            
        width=0
        count=1
        for key in list(mydict.keys()):
            data[dict_key].append([key])

            for k in oprand:
                if k not in list(mydict[key]):
                    data[dict_key][count].append('{  }')
                    continue
                if(len(mydict[key][k])>width):
                    width=len(mydict[key][k])
                data[dict_key][count].append('{ '+', '.join(map(str,mydict[key][k]))+' }')

            if(key_null):

                if 'N' not in list(mydict[key]):
                    data[dict_key][count].append('{  }')                
                else:
                    if(len(mydict[key]['N'])>width):
                        width=len(mydict[key]['N'])
                    data[dict_key][count].append('{ '+', '.join(mydict[key]['N'])+' }')
        
            count+=1
        
        if(key_null):
            return width+1,count,len(oprand)+1
        else:
            return width+1,count,len(oprand)
        
    def TEST_AUTOMATA(self,test_string):

        next_state='q0'
        Traversal_path=['q0']

        for i in test_string:

            if i in list(self.DFA[next_state].keys()):
                next_state=self.DFA[next_state][i][0]
                Traversal_path.append(next_state)
                
            else:
                Traversal_path.append('Reject')
                return(False,' -> '.join(Traversal_path))
            
        if next_state in self.accepted_states:
            Traversal_path.append('Accept')
            return(True,' -> '.join(Traversal_path))
      
        else:
            Traversal_path.append('Reject')
            return(False,' -> '.join(Traversal_path))
        
    def random_regular_expression(self,number_of_regular_exp=50,max_exp_length=10):

        oprands=['a','b','c','d','e']
        operators=['+','.']

        res=[]
        n=number_of_regular_exp
        for _ in range(n):
            length=random.randint(1,max_exp_length)
            new_re=""
            while len(new_re)<length:
                if(len(new_re)==0):
                    op1=random.choice(oprands)
                else:
                    if random.randint(0,5)==0:
                        op1='('+new_re+')'
                    else:
                        op1=new_re
                if random.randint(0,5)==0:
                    op1=op1+"*"
                op2=random.choice(oprands)
                op=random.choice(operators)
                new_re=op1+op+op2
            
            res.append(new_re)
        return res

class Method_1(Deterministic_Finite_Automata):
        
    def generate(self):
    
        self.get_postfix()
        if(not self.valid):
            print("Error")
            return "error"
        method1 = Deterministic_Finite_Automata_Method_1(self.post_fix)
        method1.NFA_NULL_FUNCTION()
        method1.NFA_FUNCTION()
        method1.DFA_FUNCTION()
        method1.MINIMIZATION_FUNCTION()
        
        self.DFA=method1.MINIMIZED_DFA
        self.accepted_states=method1.Accepted_MINIMIZED_DFA
        
        SHOW_AUTOMATA(method1.MINIMIZED_DFA,method1.Accepted_MINIMIZED_DFA,False,self.light,"output_light")
        SHOW_AUTOMATA(method1.MINIMIZED_DFA,method1.Accepted_MINIMIZED_DFA,False,self.dark,"output_dark")            
        
        l=["States"]

        for op in method1.oprand:
            l.append('Transection '+str(op))
            
        data={}
        table_details={}

        keys_1=["NFA_NULL Table","None-deterministic Finite Automata Table","Finite Automata Table","Minimized Finite Automata Table"]
        keys_2=[method1.NFA_NULL,method1.NFA,method1.DFA,method1.MINIMIZED_DFA]
        keys_3=[method1.Initial_NFA_NULL,method1.Initial_NFA,method1.Initial_DFA,method1.Initial_MINIMIZED_DFA]
        keys_4=[method1.Accepted_NFA_NULL,method1.Accepted_NFA,method1.Accepted_DFA,method1.Accepted_MINIMIZED_DFA]

        for k in keys_1:
            data[k]=[]
            table_details[k]={}
        
        for key in data:
            data[key].append(l[:])
        
        data["NFA_NULL Table"][0].append('Transection NULL')

        for i in range(len(keys_1)):
    
            if(i==0):
                w,r,c=self.copy_data(keys_2[i],data,keys_1[i],method1.oprand,False)
            else:
                w,r,c=self.copy_data(keys_2[i],data,keys_1[i],method1.oprand)
    
            table_details[keys_1[i]]["row"]=r
            table_details[keys_1[i]]["cols"]=c+1
            table_details[keys_1[i]]["width"]=max(w,5)
            table_details[keys_1[i]]["init"]='{ '+''.join(keys_3[i])+' }'
            table_details[keys_1[i]]["accept"]='{ '+', '.join(keys_4[i])+' }'
    
        keys_1.reverse()
  
        return data,table_details,keys_1
                
    
class Method_2((Deterministic_Finite_Automata)):
    
    def generate(self):
        
        self.get_postfix()
        
        if(not self.valid):
            print("Error")
            return "error"
        key_1,key_2,key_3=[],[],[]
        method2=Deterministic_Finite_Automata_Method_2(self.post_fix)
        method2.parse_tree_root=method2.parse_tree()
        method2.accepted_states,method2.DFA,method2.states=method2.find_dfa()       
        d={}
        for state in method2.DFA:
            d[state]=method2.DFA[state].copy()
            
        a=method2.accepted_states[:]
        d,a,reduced=method2.minimize_dfa(d,a,{})
        
        if not reduced:
            self.DFA=method2.DFA
            self.accepted_states=method2.accepted_states
        else:
            method2.minimized_accepted_states,method2.minimized_DFA,_=method2.rebuild_DFA(d,a,{})
            self.DFA=method2.minimized_DFA
            self.accepted_states=method2.minimized_accepted_states
            key_1.append("Minimized Finite Automata Table")
            key_2.append(method2.minimized_DFA)
            key_3.append(method2.minimized_accepted_states)

        SHOW_AUTOMATA(self.DFA,self.accepted_states,False,self.light,"output_light")
        SHOW_AUTOMATA(self.DFA,self.accepted_states,False,self.dark,"output_dark")
        
        l=["States"]
        oprand=[]
        for op in method2.oprands:
            if(op!='#'):
                l.append('Transection '+str(op))
                oprand.append(op)
        
        key_1+=["Finite Automata Table"]
        key_2+=[method2.DFA]
        key_3+=[method2.accepted_states]
   
        data={}
        table_details={}
        for i in range(len(key_1)):    
            data[key_1[i]]=[]
            table_details[key_1[i]]={}
            
            data[key_1[i]].append(l[:])
            w,r,c=self.copy_data(key_2[i],data,key_1[i],oprand)
            
            table_details[key_1[i]]["row"]=r
            table_details[key_1[i]]["cols"]=c+1
            table_details[key_1[i]]["width"]=max(w,5)
            table_details[key_1[i]]["init"]='{ '+''.join(method2.initial_state)+' }'
            table_details[key_1[i]]["accept"]='{ '+', '.join(key_3[i])+' }'
        
        key_1=key_1+["First and Follow Table","States Table"]
        data["First and Follow Table"]=[["Operand No","Operand","First","Follow"]]
        data["States Table"]=[["States Table","Follow List"]]
        
        table_details["First and Follow Table"]={}
        w,r,c=self.copy_data(method2.first_follow,data,"First and Follow Table",["oprand","first","follow"])
        
        table_details["First and Follow Table"]["row"]=r
        table_details["First and Follow Table"]["cols"]=c+1
        table_details["First and Follow Table"]["width"]=max(w,5)
        
        w=0
        for key in method2.states.keys():
            w=max(w,len(method2.states[key]))
            data["States Table"].append([key,'{ '+', '.join(map(str,method2.states[key]))+' }'])
            
        table_details["States Table"]={}
        table_details["States Table"]["row"]=len(method2.states)+1
        table_details["States Table"]["cols"]=2
        table_details["States Table"]["width"]=max(w,5)

        return data,table_details,key_1

def compare_methods(method1,method2,number_of_regular_exp=50,max_exp_length=10,input_re="",input_on=False):
    res=method1.random_regular_expression(number_of_regular_exp,max_exp_length)
    
    m1_time,m2_time=[],[]
    
    m1_input_time,m2_input_time=[],[]
    
    
    if input_on:
            
        for _ in range(100):
            start=perf_counter_ns()
            method1.regular_expression=input_re
            method1.generate()
            end=perf_counter_ns()
            m1_input_time.append((end-start)/(10**6))
            
            start=perf_counter_ns()
            method2.regular_expression=input_re
            method2.generate()
            end=perf_counter_ns()
            m2_input_time.append((end-start)/(10**6))    
        
    
    avg_time=[]
    count={"1":0,"2":0}
    j=0
    
    for i in range(5):
        # print(i)
        m1_time.clear()
        m2_time.clear()
        for exp in res:
            # print(exp)
            start_m1=perf_counter_ns()
            method1.regular_expression=exp
            method1.generate()
            end_m1=perf_counter_ns()
            m1_time.append((end_m1-start_m1)/(10**6))
                 
            start_m2=perf_counter_ns()
            method2.regular_expression=exp
            method2.generate()
            end_m2=perf_counter_ns()
            m2_time.append((end_m2-start_m2)/(10**6))

        for colr in [method1.Plot_light,method1.Plot_dark]:
            if colr==method1.Plot_light:
                plot.rcParams.update({'text.color':method1.Plot_dark[3],'axes.labelcolor':method1.Plot_dark[3],'axes.edgecolor':"Black","xtick.color":"Black","ytick.color":"Black"})
            else:
                plot.rcParams.update({'text.color':method1.Plot_light[3],'axes.labelcolor':method1.Plot_light[3],'axes.edgecolor':"White","xtick.color":"White","ytick.color":"White"})
            plot.figure(j,facecolor=colr[0])
            plot.axes().set_facecolor(colr[0])
            plot.title("Output_figure_"+str(i+1)+" : Number of RE vs Taken Time")
            plot.plot(range(0,number_of_regular_exp),m1_time,marker = 'o', label ='Table Method (Approach 1)',color=colr[1])
            plot.plot(range(0,number_of_regular_exp),m2_time,marker = '*',linestyle = 'dotted',color=colr[2],label ='Tree Method (Approach 2)')
            plot.xlabel("Random Regular Expression Number")
            plot.ylabel("Time in mili seconds")
            plot.legend(facecolor=colr[0],loc='upper right')
            plot.tight_layout(pad=1)
            if colr==method1.Plot_light:
                plot.savefig("Output_Images/figure_"+str(i)+"_light")
            else:
                plot.savefig("Output_Images/figure_"+str(i)+"_dark")
            plot.figure(j).clf()
            j+=1
    
        t1,t2=sum(m1_time)/len(m1_time),sum(m2_time)/len(m2_time)
        avg_time+=[[f'{t1:.6f}',f'{t2:.6f}']]
        if(t1<t2):
            count["1"]+=1
        else:
            count["2"]+=1
    
    if count["1"]>count["2"]:
        better_method=" Table Method (Approch 1) is better than Tree Method (Approch 2)"
    else:
        better_method=" Tree Method (Approch 2) is better than Table Method (Approch 1)"

    data=[["Method_1_Time (ms)","Method_2_Time (ms)"]]+avg_time


    if len(m1_input_time)!=0:
        t1,t2=sum(m1_input_time)/len(m1_input_time),sum(m2_input_time)/len(m2_input_time)
        return data,f"Average_Time_For_{number_of_regular_exp}_Random_Regular_Expresions",better_method,[["Method_1","Method_2"],[f'{t1:.6f}',f'{t2:.6f}']]
    else:
        return data,f"Average_Time_For_{number_of_regular_exp}_Random_Regular_Expresions",better_method
    
if __name__=="__main__":
    
    m1=Method_1("")
    
    m2=Method_2("")
    
    # m2.regular_expression="(b+c*+d)*+c"
    # m1.regular_expression="((b+a.c.e).d*+c.b.e+e)+d+b"
    m1.regular_expression="((c+c+c.c+d*+c)+d+b.b.d+c).d"
    m1.generate()
    compare_methods(m1,m2,50,10,input_on=False,input_re="((c+c+c.c+d*+c)+d+b.b.d+c).d")
    
    # ((c+c+c.c+d*+c)+d+b.b.d+c).d