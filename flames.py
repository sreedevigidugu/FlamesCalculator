from tkinter import*
from tkinter import messagebox
#creating a window
root=Tk()
root.title('flames app')
root.configure(bg='#91376d')
root.geometry('580x390')
root.resizable(False,False)
main_label=Label(root,font=('arial',30),width=22,height=7,bg='#303842')
main_label.place(x=30,y=30)
name_label=Label(root,font=('arial',14),fg='white',text='Enter your name :',bg='#303842')
name_label.place(x=80,y=125)
name=StringVar(root)
#taking your name input
name_entry=Entry(root,font=('arial',14),fg='black',bg='white',bd=5,textvariable=name)
name_entry.place(x=240,y=125)
crush_label=Label(root,font=('arial',14),fg='white',text='Enter your \n crush name ',bg='#303842')
crush_label.place(x=80,y=165)
sys_label=Label(root,font=('arial',14),fg='white',text=':',bg='#303842')
sys_label.place(x=220,y=173)
crush=StringVar(root)
#taking your crush name as input
crush_entry=Entry(root,font=('arial',14),fg='black',bg='white',bd=5,textvariable=crush)
crush_entry.place(x=240,y=175)
#test button
test=Button(root,font=('arial',14,'bold'),fg='white',bg='#3f7fbf',text='Test',width=6,command=lambda:flames_test())
test.place(x=220,y=265)

#main logic
def flames_test():
    first_mate_nam=name.get()
    second_mate_nam=crush.get()
    # if you doesn't enter data in one field
    if first_mate_nam =='' or second_mate_nam=='':
        if first_mate_nam=='' and second_mate_nam=='':
            messagebox.showerror('Name Error','Error : Enter both names')
        elif second_mate_nam=='':
            messagebox.showerror('Name Error','Error : Enter your crush name')
        else:
            messagebox.showerror('Name Error','Error : Enter your name')
    # what if you given same names
    elif first_mate_nam == second_mate_nam:
        messagebox.showerror('Input Error','Error:Enter your details properly')
    #main logic start from here    
    else:
        first_list=[str(i).lower() for i in first_mate_nam]
        first_list1=first_list.copy()
        space1=first_list.count(' ')
        #removing spaces in given name input
        for i in range(space1):
            first_list.pop(first_list.index(" "))
            first_list1.pop(first_list1.index(" "))
        second_list=[str(i).lower() for i in second_mate_nam]
        second_list1=second_list.copy()
        #removing spaces in given crush name input
        space2=second_list.count(' ')
        for i in range(space2):
            second_list.pop(second_list.index(" "))
            second_list1.pop(second_list1.index(" "))
        #deleting letters which are common in both names
        for i in first_list1:
            if i in second_list:
                first_list.pop(first_list.index(i))
                second_list.pop(second_list.index(i))
        flames_list=['F','L','A','M','E','S']
        length=len(first_list)+len(second_list)
        #working flames
        while len(flames_list)>1:
            if len(flames_list)>length:
                flames_list.pop(length-1)
            else:
                remekn=length%len(flames_list)
                flames_list.pop(remekn-1) 
        #assigning result based on flames output
        if flames_list[0] == 'F':
            result='friends'
        elif flames_list[0] == 'L':
            result='lovers'
        elif flames_list[0] == 'A':
            result='affection'
        elif flames_list[0] == 'M':
            result='married'
        elif flames_list[0] == 'E':
            result='Eneimies'
        elif flames_list[0] == 'S':
            result='brother and sister'
        #creating a result window
        pop_up=Toplevel(root)
        pop_up.title('flames result')
        pop_up.resizable(False,False)
        pop_up.configure(bg='#476388')
        pop_up.geometry('578x385')
        #disabling exit symbol('x') in result window
        def disable_event():
            pass
        pop_up.protocol("WM_DELETE_WINDOW",disable_event)
        pop_label=Label(pop_up,font=('poppins',30),width=22,height=7,bg='#303842',fg='white',wraplength=500,justify=CENTER,bd=5)
        pop_label.place(x=30,y=30)
        name_pop_label=Label(pop_up,font=('arial',14),fg='white',text='Your name ',bg='#303842')
        name_pop_label.place(x=100,y=125)
        crush_pop_label=Label(pop_up,font=('arial',14),fg='white',text='Your crush name :',bg='#303842')
        crush_pop_label.place(x=100,y=165)
        sys_pop_label=Label(pop_up,font=('arial',14),fg='white',text=':',bg='#303842')
        sys_pop_label.place(x=245,y=125)
        rel_pop_label=Label(pop_up,font=('arial',14),fg='white',text='Relationship ',bg='#303842')
        rel_pop_label.place(x=100,y=205)
        sys_pop_label1=Label(pop_up,font=('arial',14),fg='white',text=':',bg='#303842')
        sys_pop_label1.place(x=245,y=205)
        name_pop_res=Label(pop_up,font=('arial',14),fg='white',text=first_mate_nam,bg='#303842')
        name_pop_res.place(x=290,y=125)
        crush_pop_res=Label(pop_up,font=('arial',14),fg='white',text=second_mate_nam,bg='#303842')
        crush_pop_res.place(x=290,y=165)
        rel_pop_res=Label(pop_up,font=('arial',14),fg='white',text=result,bg='#303842')
        rel_pop_res.place(x=290,y=205)
        def close_win():
            result=''
            pop_up.quit()
            root.quit()
        def back_win():
            flames_list=['F','L','A','M','E','S']
            pop_up.destroy()
            
        test1=Button(pop_up,font=('arial',14,'bold'),fg='white',bg='#3f7fbf',text='CLOSE',width=6,command=close_win)
        test1.place(x=160,y=265)
        test2=Button(pop_up,font=('arial',14,'bold'),fg='white',bg='#3f7fbf',text='BACK',width=6,command=back_win)
        test2.place(x=260,y=265)
        
        pop_up.mainloop()   
root.mainloop()