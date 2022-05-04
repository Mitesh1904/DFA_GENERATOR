import DFA
from tkinter import messagebox
import pyautogui
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image


class DFA_GUI():
    
    def __init__(self):
        self.GUI = Tk()
        self.GUI.title("DFA")
        self.D=DFA.Deterministic_Finite_Automata("")
        self.I=DFA.Infix_to_Postfix()
        self.Width,self.Height= pyautogui.size()
        self.GUI.geometry(f"{self.Width}x{self.Height}")
        self.Theme_value= IntVar()
        self.Theme_value.set(2)
        self.default_Screen=True
        self.default_txt=[]
        self.table1=[]
        self.table2=[]
        self.txt1=[]
        self.txt2=[]
        self.lastinput=""
        self.Create_Canvas()
        self.Create_frame()
        self.note_message='''\n*** Note : Follow the below rules for RE ***\n---> 1. for Union use '+' Ex. a+b \n---> 2. for concatenation use '.' Ex. a.b \n---> 3. for Kleene use '*' Ex a* \n---> 4. Use only alphabets Ex (a,b,c) \n---> Example of input : (a+b)*'''
        self.Set_Colors()
        self.Set_Defaul_Screen() 
        self.GUI.state('zoomed')
        self.GUI.mainloop()
    
    def Set_Defaul_Screen(self):
        self.default_txt.clear()
        w,_=pyautogui.size()
        self.Status_bar_variable.set("Regular Expression to Deterministic Finite Automata")
        self.default_txt.append(self.canvas.create_text(w/2,150,text="INNOVATIVE ASSIGNMENT",fill=self.fill_color,font="Comic 30 bold underline"))
        self.default_txt.append(self.canvas.create_text(w/2-300,250,text="COURSE : ",fill=self.fill_color,font="Comic 24 bold"))
        self.default_txt.append(self.canvas.create_text(w/2-262,300,text="CREATED BY : ",fill=self.fill_color,font="Comic 24 bold"))
        self.default_txt.append(self.canvas.create_text(w/2+80,250,text="THEORY OF COMPUTATION (2CS601)",fill=self.outline_color,font="Comic 24 italic"))
        self.default_txt.append(self.canvas.create_text(w/2+50,300,text="Parth Nimbadkar ~ 19BCE143",fill=self.outline_color,font="Comic 20 "))
        self.default_txt.append(self.canvas.create_text(w/2+43,350,text="Mitesh Panchal ~ 19BCE149",fill=self.outline_color,font="Comic 20 "))
        self.default_txt.append(self.canvas.create_text(w/2+43,400,text="Jayesh Pandya ~ 19BCE151",fill=self.outline_color,font="Comic 20 "))
        self.canvas.update()
        
    def Set_Colors(self):
        if(self.Theme_value.get()==1):
            self.background_color="#36454F"
            self.button_color="#550A35"
            self.outline_color="#550A35"
            self.fill_color="#D2EFF5"
            self.create_outline_color="#CCCCFF"
            self.node_color_1=self.fill_color
            self.node_color_2=self.outline_color
        else:
            self.background_color="#C7F6EC"
            self.outline_color="#02231C"
            self.button_color="#02231C" 
            self.fill_color="#4DD8AD"
            self.create_outline_color="#DBF9DB"
            self.node_color_1=self.fill_color
            self.node_color_2="#8467D7"
        self.Update_Theme_colors()
        self.High_light_color()
    
    def High_light_color(self):
        self.frame.config(highlightcolor=self.outline_color)
        self.canvas.config(highlightcolor=self.outline_color)
        self.status_bar.config(highlightcolor=self.outline_color,highlightbackground=self.create_outline_color,highlightthickness=3)
        self.canvas.update()
    
    def Update_Theme_colors(self):
        self.frame.config(background=self.background_color,highlightbackground=self.outline_color)
        self.canvas.config(background=self.background_color,highlightbackground=self.outline_color)  
        self.MyInsert.config(activebackground=self.create_outline_color,activeforeground=self.button_color,bg=self.button_color,
                            fg=self.create_outline_color)
        self.MySearch.config(activebackground=self.create_outline_color,activeforeground=self.button_color,bg=self.button_color,
                            fg=self.create_outline_color)
        self.MyHelp.config(activebackground=self.create_outline_color,activeforeground=self.button_color,bg=self.button_color,
                            fg=self.create_outline_color)
        self.Insert_Entry.config(bg=self.create_outline_color,fg=self.outline_color)
        self.Search_Entry.config(bg=self.create_outline_color,fg=self.outline_color)
        self.status_bar.config(background=self.fill_color,foreground=self.outline_color)
        self.status_bar_frame.config(background=self.outline_color)
        self.radio_1.config(background=self.background_color,foreground=self.outline_color,activebackground=self.background_color,
                            activeforeground=self.create_outline_color)
        self.radio_2.config(background=self.background_color,foreground=self.outline_color,activebackground=self.background_color,
                            activeforeground=self.create_outline_color)
        
            
        if(self.default_Screen): 
            for i in range(len(self.default_txt)):
                if(i<3):
                    self.canvas.itemconfig(self.default_txt[i],fill=self.fill_color)
                else:
                    self.canvas.itemconfig(self.default_txt[i],fill=self.outline_color)
                    
        else:
            for i in self.txt1:
                self.canvas.itemconfig(i,fill=self.outline_color)
            
            for i in self.txt2:
                self.canvas.itemconfig(i,fill=self.fill_color)
            
            for i in self.table1:
                self.canvas.itemconfig(i,outline=self.outline_color,fill=self.fill_color)
                
            for i in self.table2:
                self.canvas.itemconfig(i,outline=self.fill_color,fill=self.outline_color)
            
            if(self.lastinput!=""):
                self.Insert_value.set(self.lastinput)
                self.Get_input()    
            
    def Create_frame(self): 
        self.frame=Frame(self.GUI,width=50,height=50,highlightthickness=2)
        self.frame.pack(fill=X,padx=0,pady=0)
        self.Input_from_GUI()
        
    def High_light_color(self):
        self.frame.config(highlightcolor=self.outline_color)
        self.canvas.config(highlightcolor=self.outline_color)
        self.status_bar.config(highlightcolor=self.outline_color,highlightbackground=self.create_outline_color,highlightthickness=3)
        self.canvas.update()
        
    def Create_Canvas(self):
        self.scroll_y=Scrollbar(self.GUI,orient="vertical")
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x=Scrollbar(self.GUI,orient='horizontal')
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.canvas=Canvas(self.GUI,borderwidth=0,width=168,height=100,highlightthickness=3,yscrollcommand=self.scroll_y.set,xscrollcommand=self.scroll_x.set)
        self.canvas.pack(fill=BOTH,expand=True,padx=0,pady=0)
        self.Status_bar_variable= StringVar()
        self.Status_bar_variable.set("Regular Expression to Deterministic Finite Automata")
        self.status_bar_frame=Frame(self.canvas)
        self.status_bar_frame.pack(fill=X,side=TOP)
        self.status_bar = Label(self.status_bar_frame,height=1,textvariable=self.Status_bar_variable,relief="groove",font="Comic 14 bold")
        self.status_bar.pack(fill=X,side=TOP,padx=3,pady=3)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.MyScroll()
    
    def _on_mousewheel(self,e): 
        self.canvas.yview_scroll(int(-1*(e.delta/120)), "units")

    def Input_from_GUI(self):
        
        self.MyHelp = Button(self.frame,text="Help",command=self.Get_Help,padx=0,pady=0,justify=CENTER,bd=2,relief="groove",width=8,height=1)
        self.MyHelp.grid(row=7,column=2,padx=5,pady=10)
        self.MyInsert = Button(self.frame,text="Insert",command=self.Get_input,padx=10,pady=5,justify=CENTER,bd=2,relief="groove",width=8,height=1)
        self.MyInsert.grid(row=7,column=4,padx=5,pady=10)
        self.MySearch = Button(self.frame,text="Test",command=self.Test,padx=10,pady=5,justify=CENTER,bd=2,relief="groove",width=8,height=1)
        self.MySearch.grid(row=7,column=6,padx=5,pady=10)
        self.Insert_value = StringVar()
        self.Search_value = StringVar()
        self.Insert_Entry = Entry(self.frame,textvariable=self.Insert_value,font="Comic 16 bold",justify=CENTER,relief="ridge",width=20)
        self.Search_Entry = Entry(self.frame,textvariable=self.Search_value,font="Comic 16 bold",justify=CENTER,relief="ridge",width=20)
        self.Insert_Entry.grid(row=7,column=3,padx=10)
        self.Search_Entry.grid(row=7,column=5,padx=10)
        self.Insert_Entry = Entry(self.frame,textvariable=self.Insert_value,font="Comic 16 bold",justify=CENTER,relief="ridge",width=20)
        self.Insert_Entry.grid(row=7,column=3,padx=10)
        self.radio_1=Radiobutton(self.frame,text="Dark mode",font="Comic 10 bold",variable=self.Theme_value,value=1,command=self.Set_Colors)
        self.radio_1.grid(row=7,column=10,padx=20)
        self.radio_2=Radiobutton(self.frame,text="Light mode",font="Comic 10 bold",variable=self.Theme_value,value=2,command=self.Set_Colors)
        self.radio_2.grid(row=7,column=11,padx=10)
    
    def MyScroll(self):   
        self.Width+=self.Width*2
        self.Height+=self.Height*4
        self.canvas.config(scrollregion=(0,0,self.Width,self.Height))
        self.scroll_x.config(command=self.canvas.xview)
        self.scroll_y.config(command=self.canvas.yview)
        self.canvas.update()
    
    def Get_input(self):
        check=self.I.Postfix(self.Insert_value.get())
        self.canvas.delete('all')
        if(check):
            self.default_Screen=False
            self.D=DFA.Deterministic_Finite_Automata('')
            self.D.postfix_expersion=self.I.postfix
            self.lastinput=self.Insert_value.get()
            self.Status_bar_variable.set("Regular Expression : "+self.Insert_value.get())
            self.D.NFA_NULL_FUNCTION()
            self.D.NFA_FUNCTION()
            self.D.DFA_FUNCTION()
            self.D.MINIMIZATION_FUNCTION()
            self.D.SHOW_AUTOMATA(False,[self.background_color,self.create_outline_color,self.node_color_2,self.node_color_1])
            self.img1=Image.open("output.png")
            p_width,p_height=self.img1.size
            self.table1.clear()
            self.table2.clear()
            self.txt1.clear()
            self.txt2.clear()
            self.txt1.append(self.canvas.create_text(184+p_width/2,75,text="Finite Automata",fill=self.outline_color,font="Comic 15 bold"))
            self.img=ImageTk.PhotoImage(self.img1)
            self.canvas.create_image(184,100,anchor=NW,image=self.img)
            next_h=p_height+100+75
            self.table_dict={'d':[self.D.MINIMIZED_DFA,self.D.DFA,self.D.NFA,self.D.NFA_NULL],'dfa':[True,True,False,False],'nfa':[False,False,False,True],'Mess':["Minimized Finite Automata Table","Finite Automata Table","None-deterministic Finite Automata Table","NFA_NULL Table"]}
            initial_accept=[[self.D.Initial_MINIMIZED_DFA,self.D.Accepted_MINIMIZED_DFA],[self.D.Initial_DFA,self.D.Accepted_DFA],[self.D.Initial_NFA,self.D.Accepted_NFA],[self.D.Initial_NFA_NULL,self.D.Accepted_NFA_NULL]] 
            for i in range(0,4):
                if(i==0):
                    if len(self.D.MINIMIZED_DFA)==len(self.D.DFA):
                        continue
                data,r,c,max_width=self.tabale_data(self.table_dict['d'][i],self.table_dict['dfa'][i],self.table_dict['nfa'][i])
                if(max_width>4):
                    self.txt1.append(self.canvas.create_text(184+25*max_width*c,next_h,text=self.table_dict['Mess'][i],fill=self.outline_color,font="Comic 15 bold"))
                    self.create_table(184,next_h+25,r,c,data,initial_accept[i],max_width)
                else:
                    self.txt1.append(self.canvas.create_text(184+100*c,next_h,text=self.table_dict['Mess'][i],fill=self.outline_color,font="Comic 15 bold"))
                    self.create_table(184,next_h+25,r,c,data,initial_accept[i])
                next_h+=40*r+100
            self.canvas.update()
        else:
            self.default_Screen=True
            self.Set_Defaul_Screen()
            self.Status_bar_variable.set("Regular Expression to Deterministic Finite Automata")
            messagebox.showerror("Input Error", "Error : Invalid Regular Expression !!!"+self.note_message)
            self.D=DFA.Deterministic_Finite_Automata('')
        self.Insert_value.set("")
        self.I=DFA.Infix_to_Postfix()
        
    def Get_Help(self):
        messagebox.showinfo("Help", "Its a RE to DFA converter !!!"+self.note_message)
        
    def tabale_data(self,dict,DFA,NFA_NULL):
        x=['States']
        max_width=0
        data=[]
        for op in self.D.oprand:
            x.append('Transection '+str(op))
        if(NFA_NULL):
            x.append('Transection NULL("^")')
        data.append(x)
        for state in dict:
            x=[]
            x.append(state)
            for op in self.D.oprand:
                if(DFA):
                    x.append(dict[state][op][0])   
                else:
                    if(op in list(dict[state].keys())):
                        if(len(dict[state][op])==1):
                            x.append(dict[state][op][0])
                        elif(len(dict[state][op])==0):
                            x.append('-')
                        else:
                            x.append(dict[state][op])
                            if(len(dict[state][op])>max_width):
                                max_width=len(dict[state][op])
                    else:
                        x.append('-')
            if(NFA_NULL):
                if 'N' in list(dict[state].keys()): 
                    if(len(dict[state]['N'])==1):
                        x.append(dict[state]['N'][0])
                    elif(len(dict[state]['N'])==0):
                        x.append('-')
                    else:
                        x.append(dict[state]['N'])
                        if(len(dict[state]['N'])>max_width):
                            max_width=len(dict[state]['N'])
                else:
                    x.append('-')
            data.append(x)
        return(data,len(dict)+1,len(x),max_width)            

    def Test(self):
        if(self.default_Screen):
            self.Search_value.set("")
            messagebox.showerror("Error", " First Add Regular expresion then check "+self.note_message)
            return
        test_string=self.Search_value.get()
        if(self.D.TEST_AUTOMATA(test_string)):
            messagebox.showinfo("OUTPUT", " Given string is accepted by this Finite_Automata \n Traversal_path : "+''.join(self.D.Traversal_path))
        else:
            messagebox.showerror("OUTPUT", " Given string is not accepted by this Finite_Automata \n Traversal_path : "+''.join(self.D.Traversal_path))
        self.Search_value.set("")
        
    def create_table(self,w,h,row,column,data,accept,max_width=4):
        new_width=50*max_width
        if(new_width*3>=self.Width):
            self.MyScroll()
        for i in range(0,row):
            for j in range(column):    
                if(i==0):
                    self.table2.append(self.canvas.create_rectangle(w+new_width*j,h+40*i,w+new_width*(j+1),h+40*(i+1),fill=self.outline_color,outline=self.fill_color))
                    self.txt2.append(self.canvas.create_text(w+new_width*j+new_width/2,h+40*i+20,text=str(data[i][j]),fill=self.fill_color,font="Comic 12 bold"))
                else:    
                    self.table1.append(self.canvas.create_rectangle(w+new_width*j,h+40*i,w+new_width*(j+1),h+40*(i+1),fill=self.fill_color,outline=self.outline_color))
                    self.txt1.append(self.canvas.create_text(w+new_width*j+new_width/2,h+40*i+20,text=str(data[i][j]),fill=self.outline_color,font="Comic 12 bold"))
        self.canvas.update()
        s=["Initial State","Accepted State"]
        for i in range(0,2):
            self.table2.append(self.canvas.create_rectangle(w+new_width*(column+i)+50,h,w+new_width*(column+1+i),h+40,fill=self.outline_color,outline=self.fill_color))
            self.txt2.append(self.canvas.create_text(w+new_width*(column+i)+new_width/2+25,h+20,text=s[i],fill=self.fill_color,font="Comic 12 bold"))
            self.table1.append(self.canvas.create_rectangle(w+new_width*(column+i)+50,h+40,w+new_width*(column+1+i),h+40*2,fill=self.fill_color,outline=self.outline_color))
            self.txt1.append(self.canvas.create_text(w+new_width*(column+i)+new_width/2+25,h+60,text=accept[i],fill=self.outline_color,font="Comic 12 bold"))

G = DFA_GUI()