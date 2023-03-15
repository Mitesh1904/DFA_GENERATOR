import pyautogui
from tkinter import messagebox
from tkinter import *

from Backend import *
from PIL import ImageTk,Image

class Window:
    
    def __init__(self,name="Project_Title"):
        
        self.GUI = Tk()     
        self.GUI.title(name)
        self.Width,self.Height= pyautogui.size()
        self.GUI.iconbitmap("Output_Images/logo.ico")
        self.method1=Method_1("")
        self.method2=Method_2("")
        self.last_re=""
        self.GUI.geometry(f"{self.Width}x{self.Height}")
        self.Method_Value= IntVar()         
        self.Method_Value.set(2)
        self.Theme_Value= IntVar()
        self.Length_value= IntVar()
        self.Number_of_re = IntVar()
        self.Number_of_re.set(100)
        self.Length_value.set(25)
        self.Theme_Value.set(2)
        self.IMG=[]
        self.tables_data=[]
        self.canvas_window()
        self.input_frame()
        self.GUI.state('zoomed')    
        self.change_theme_colors()
        self.GUI.mainloop()
        
    def change_theme_colors(self):
        
        if(self.Theme_Value.get()==1):
        
            self.background_color="#014751" #background
            self.button_color="#FFEEB4"
            self.outline_color="#00D37F"
            self.fill_color="#D2EFF5"
            self.create_outline_color="#4863A0"
        
        else:
        
            self.background_color="#C7F6EC"
            self.outline_color="#02231C"
            self.button_color="#02231C" 
            self.fill_color="#4DD8AD"
            self.create_outline_color="#DBF9DB"
            
        self.__set_colors()
    
    def __set_colors(self):
        
        self.frame.config(background=self.background_color,highlightbackground=self.outline_color)    
        self.canvas.config(background=self.background_color,highlightbackground=self.outline_color)  
        
        for data in [self.MyInsert,self.MyHelp,self.MySearch,self.MyClear]:
            data.config(activebackground=self.create_outline_color,activeforeground=self.button_color,bg=self.button_color,fg=self.create_outline_color)
        
        self.Insert_Entry.config(bg=self.create_outline_color,fg=self.outline_color)
        self.Search_Entry.config(bg=self.create_outline_color,fg=self.outline_color)
        
        self.camper_frame.config(background=self.background_color,highlightthickness=3,highlightbackground=self.outline_color)
        self.status_bar_frame.config(background=self.outline_color)
        
        self.status_bar.config(background=self.fill_color,foreground=self.outline_color)
        self.camper_button.config(activebackground=self.outline_color,activeforeground=self.background_color,bg=self.background_color,fg=self.outline_color,border=0)
       
        self.space.config(background=self.fill_color,foreground=self.outline_color)
                        
        for data in [self.radio_table_method,self.radio_tree_method,self.radio_dark,self.radio_light,self.radio_length_5,self.radio_length_10,self.radio_length_25,self.radio_Num_re_50,self.radio_Num_re_100,self.radio_Num_re_200]:
            data.config(background=self.background_color,foreground=self.outline_color,activebackground=self.background_color, activeforeground=self.create_outline_color) 
        
        self.__set_items_color()    
    
    def __set_items_color(self):
        for table in self.tables_data:
            
            for i in table["box"][0]:
                self.canvas.itemconfig(i,outline=self.outline_color,fill=self.fill_color)
                
            for i in table["box"][1]:
                self.canvas.itemconfig(i,outline=self.fill_color,fill=self.outline_color)
                
            for i in table["text"][0]:
                self.canvas.itemconfig(i,fill=self.outline_color)
                
            for i in table["text"][1]:
                self.canvas.itemconfig(i,fill=self.fill_color)
                
            for i in table["title"]:
                self.canvas.itemconfig(i,fill=self.outline_color)
                
        if len(self.tables_data)!=0: 
            if len(self.IMG)!=0:
                self.__set_images()
            else:
                if self.Theme_Value.get()==1:
                    img1=Image.open("Output_Images/output_dark.png")
                else:
                    img1=Image.open("Output_Images/output_light.png")
        
                self.img=ImageTk.PhotoImage(img1)
                self.canvas.create_image(184,150,anchor=NW,image=self.img)
    
    def input_frame(self): 
    
        self.frame=Frame(self.GUI,width=50,height=50,highlightthickness=2)
        self.frame.pack(fill=X,padx=0,pady=0)
        self.input_box()
        
    def canvas_window(self):
        
        self.scroll_y=Scrollbar(self.GUI,orient="vertical")
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_x=Scrollbar(self.GUI,orient="horizontal")
        self.scroll_x.pack(side=BOTTOM,fill=X)
        
        self.canvas=Canvas(self.GUI,borderwidth=0,width=168,height=100,highlightthickness=3,yscrollcommand=self.scroll_y.set,xscrollcommand=self.scroll_x.set)
        self.canvas.pack(fill=BOTH,expand=True,padx=0,pady=0)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
        self.Status_bar_variable= StringVar()
        self.Status_bar_variable.set("Regular Expression to Deterministic Finite Automata")
        self.status_bar_frame=Frame(self.canvas,relief="groove",bd=2)
        self.status_bar_frame.pack(fill=X,side=TOP)
        self.camper_frame=Frame(self.canvas)
        self.camper_frame.pack(fill=X,side=TOP)
        
        
        self.radio_length_5=Radiobutton(self.camper_frame,text="Max_RE_length 5",font="Comic 10 bold",variable=self.Length_value,value=5)
        self.radio_length_5.grid(row=0,column=1,padx=25)
        self.radio_length_10=Radiobutton(self.camper_frame,text="Max_RE_length 10",font="Comic 10 bold",variable=self.Length_value,value=10)
        self.radio_length_10.grid(row=0,column=2,padx=25)
        self.radio_length_25=Radiobutton(self.camper_frame,text="Max_RE_length 25",font="Comic 10 bold",variable=self.Length_value,value=25)
        self.radio_length_25.grid(row=0,column=3,padx=25)
        
        self.space=Label(self.camper_frame,height=1,bd=0,font="Comic 14 bold")
        self.space.grid(row=0,column=4,padx=50)
        self.radio_Num_re_50=Radiobutton(self.camper_frame,text="Random 50 RE",font="Comic 10 bold",variable=self.Number_of_re,value=50)
        self.radio_Num_re_50.grid(row=0,column=7,padx=25)
        self.radio_Num_re_100=Radiobutton(self.camper_frame,text="Random 100 RE",font="Comic 10 bold",variable=self.Number_of_re,value=100)
        self.radio_Num_re_100.grid(row=0,column=8,padx=25)
        self.radio_Num_re_200=Radiobutton(self.camper_frame,text="Random 200 RE",font="Comic 10 bold",variable=self.Number_of_re,value=200)
        self.radio_Num_re_200.grid(row=0,column=9,padx=25)
        
        self.camper_button = Button(self.camper_frame,text="Compare",font="Comic 14 bold",command=self.Method_Comparison,padx=0,pady=0,justify=LEFT,bd=2,relief="groove",width=27,height=2)
        self.camper_button.grid(row=0,column=10,padx=198)
        
        self.status_bar = Label(self.status_bar_frame,height=1,textvariable=self.Status_bar_variable,relief="groove",font="Comic 14 bold")
        self.status_bar.pack(fill=X,side=TOP,padx=3,pady=3)
        
    def _on_mousewheel(self,e):
        self.canvas.yview_scroll(int(-1*(e.delta/120)), "units")      
        
    def input_box(self):
        
        self.radio_table_method=Radiobutton(self.frame,text="Table Method (Approch 1)",font="Comic 10 bold",variable=self.Method_Value,value=1,command=self.change_method)
        self.radio_table_method.grid(row=7,column=0,padx=20)
        self.radio_tree_method=Radiobutton(self.frame,text="Tree Method (Aproch 2)",font="Comic 10 bold",variable=self.Method_Value,value=2,command=self.change_method)
        self.radio_tree_method.grid(row=7,column=1,padx=10)
        
        self.MyInsert = Button(self.frame,text="Insert",command=self.get_input,padx=10,pady=5,justify=CENTER,bd=2,relief="groove",width=8,height=1)
        self.MyInsert.grid(row=7,column=4,padx=5,pady=10)
        self.MySearch = Button(self.frame,text="Test",command=self.test,padx=10,pady=5,justify=CENTER,bd=2,relief="groove",width=8,height=1)
        self.MySearch.grid(row=7,column=6,padx=5,pady=10)
        
        self.Insert_value = StringVar()
        self.Search_value = StringVar()
        
        self.Insert_Entry = Entry(self.frame,textvariable=self.Insert_value,font="Comic 16 bold",justify=CENTER,relief="ridge",width=17)
        self.Search_Entry = Entry(self.frame,textvariable=self.Search_value,font="Comic 16 bold",justify=CENTER,relief="ridge",width=17)
        self.Insert_Entry.grid(row=7,column=3,padx=10)
        self.Search_Entry.grid(row=7,column=5,padx=10)
        
        self.MyClear = Button(self.frame,text="clear",command=self.clear_screen,padx=10,pady=5,justify=CENTER,bd=2,relief="groove",width=8,height=1)
        self.MyClear.grid(row=7,column=7,padx=25,pady=10)
        
        self.radio_dark=Radiobutton(self.frame,text="Dark mode",font="Comic 10 bold",variable=self.Theme_Value,value=1,command=self.change_theme_colors)
        self.radio_dark.grid(row=7,column=11,padx=50)
        self.radio_light=Radiobutton(self.frame,text="Light mode",font="Comic 10 bold",variable=self.Theme_Value,value=2,command=self.change_theme_colors)
        self.radio_light.grid(row=7,column=12,padx=0)
        
        self.MyHelp = Button(self.frame,text="Help",command=self.get_help,padx=10,pady=5,justify=CENTER,bd=2,relief="groove",width=8,height=1)
        self.MyHelp.grid(row=7,column=15,padx=75,pady=10)
        
        self.update_scroll_bar_region()
        
    def update_scroll_bar_region(self):   
        self.Width+=self.Width*2
        self.Height+=self.Height*4
        self.canvas.config(scrollregion=(0,0,self.Width,self.Height))
        self.scroll_x.config(command=self.canvas.xview)
        self.scroll_y.config(command=self.canvas.yview)
        self.canvas.update()
        
    def get_help(self):
        messagebox.showinfo("Help", "\tIts a RE to DFA converter !!!\n"+self.get_default_message())
    
    def get_default_message(self):
        return '''\n*** Note : Follow the below rules for RE ***\n---> 1. for Union use '+' Ex. a+b \n---> 2. for concatenation use '.' Ex. a.b \n---> 3. for Kleene use '*' Ex a* \n---> 4. Use only alphabets Ex (a,b,c) \n---> Example of input : (a+b)*\n---> for comparison click on compare'''
    
    def show_error(self,error_message,error_code="Error"):
        messagebox.showerror(error_code,error_message)        
    
    def clear_screen(self):
        self.tables_data.clear()
        self.canvas.delete("all")
        self.Insert_value.set("")
        self.Search_value.set("")
        self.IMG.clear()
        self.Status_bar_variable.set("Regular Expression to Deterministic Finite Automata")    
    
    def change_method(self):
        if(self.Insert_value.get()!="") and len(self.IMG)==0:
            self.get_input()        
       
    def get_input(self):
        
        self.Insert_value.set(self.Insert_value.get().strip()) 
        self.last_re=self.Insert_value.get()
        self.method1.regular_expression=self.Insert_value.get() 
        self.method2.regular_expression=self.Insert_value.get() 
        self.method1.get_postfix()
        self.tables_data.clear()
        self.IMG.clear()
        self.canvas.delete('all')
        
        if(not self.method1.valid):
            self.show_error(" \tInvalid Regular Expression \n"+self.get_default_message(),"Invalid Input")
            return 
 
        self.Status_bar_variable.set("Regular Expression : "+self.Insert_value.get())
        if(self.Method_Value.get()==1):
            data,td,keys_1=self.method1.generate()
        else:
            data,td,keys_1=self.method2.generate()
            
        if self.Theme_Value.get()==1:
            self.img1=Image.open("Output_Images/output_dark.png")
        else:
            self.img1=Image.open("Output_Images/output_light.png")
        _,p_height=self.img1.size
        
        next_h=p_height+150+100

        total_cols=0
        total_rows=0
        
        for key in keys_1:
            self.generate_table(100,next_h+50*total_rows,td[key]["width"]*50,50,td[key]["row"],td[key]["cols"],data[key],key) 
            total_cols=((td[key]["width"])*50)*td[key]["cols"]+100
            if('init' in list(td[key].keys())):
                self.generate_table(100+total_cols,next_h+50*total_rows,td[key]["width"]*50,50,2,1,[["Initial State"],[td[key]['init']]],'')
                total_cols=total_cols+(td[key]["width"])*50
                self.generate_table(total_cols+200,next_h+50*total_rows,td[key]["width"]*50,50,2,1,[["Accepted State"],[td[key]['accept']]],'')
            total_rows+=td[key]["row"]+2
                   
        self.__set_items_color()
   
    def test(self):
        if len(self.tables_data)==0:
            self.show_error("Invalid Input please first generate DFA and then check")
            return
    
        if self.Method_Value.get()==1:
            valid,path=self.method1.TEST_AUTOMATA(self.Search_value.get().strip()) 

        else:
            valid,path=self.method2.TEST_AUTOMATA(self.Search_value.get().strip()) 
    
        if(valid):
            messagebox.showinfo("OUTPUT", " Given string is accepted by this Finite_Automata \n Traversal_path : "+path)
    
        else:
            self.show_error(" Given string is rejected by this Finite_Automata \n Traversal_path : "+path,"OUTPUT")
    
    def Method_Comparison(self):
        self.Status_bar_variable.set("Comparison in Process..., Wait for a while it takes some time !!!!")
        self.canvas.update()
        
        re_num=self.Number_of_re.get()
        re_len=self.Length_value.get()
        check = len(self.tables_data)!=0 and self.last_re!=""
        self.clear_screen()
        if check:
            data,title,better,input_time=compare_methods(self.method1,self.method2,re_num,re_len,input_re=self.last_re,input_on=True)
            self.generate_table(1250,300,250,75,2,2,input_time,"Average Time for "+self.last_re)
        else:
            data,title,better=compare_methods(self.method1,self.method2,re_num,re_len)        
        
        self.Status_bar_variable.set("Comparison Output")
        self.generate_table(200,250,250,75,6,2,data,title,"Comic 14 bold","Comic 11 bold")
        
        self.generate_table(850,500,1250,100,1,1,[[better]],"",data_font="Comic 17 bold")
        self.__set_images()
        self.__set_colors()
        
    def __set_images(self):
        next_h=750
        next_w=100
        self.IMG.clear()
        for i in range(5):
            if self.Theme_Value.get()==1:
                img1=Image.open("Output_Images/figure_"+str(i)+"_dark.png")
            else:
                img1=Image.open("Output_Images/figure_"+str(i)+"_light.png")
            
            self.IMG.append(ImageTk.PhotoImage(img1))
            p_width,p_height=img1.size
            if(i==4):
                next_w=p_width+155
                next_h=800+p_height/2
                self.canvas.create_image(next_w,next_h,anchor=NW,image=self.IMG[i])
                
            elif(i%2==0):
                self.canvas.create_image(100,next_h,anchor=NW,image=self.IMG[i])
            else:
                self.canvas.create_image(next_w,next_h,anchor=NW,image=self.IMG[i])
                next_h+=p_height+100
            
            next_w=p_width+850
        
    
    def generate_table(self,x_point,y_point,box_width,box_height,no_rows,no_columns,table_data,table_title,title_font="Comic 15 bold",data_font="Comic 13 bold"):
        
        table={"box":[[],[]],"text":[[],[]],"title":[]}
        table["title"].append(self.canvas.create_text(x_point+(no_columns*box_width/2),y_point-(box_height/2),text=table_title,font=title_font))
        for i in range(0,no_rows):
            for j in range (0,no_columns):
                x1,y1=(j*box_width+x_point,i*box_height+y_point)
                x2,y2=(j*box_width+x_point+box_width,i*box_height+y_point+box_height)
                if i==0:
                    table["box"][0].append(self.canvas.create_rectangle(x1,y1,x2,y2))
                    table["text"][0].append(self.canvas.create_text(x1+(box_width/2),y1+(box_height/2),text=str(table_data[i][j]),font=data_font))
                else:
                    table["box"][1].append(self.canvas.create_rectangle(x1,y1,x2,y2))
                    table["text"][1].append(self.canvas.create_text(x1+(box_width/2),y1+(box_height/2),text=str(table_data[i][j]),font=data_font))
                
        self.tables_data.append(table)
        
if __name__=="__main__":        
    Window()