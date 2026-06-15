from mydb import Database
from tkinter import *
from tkinter import messagebox
from myapi import API
class NLPApp:

    def __init__(self):
        # create database object

        self.db = Database()
        self.api = API()

        self.root = Tk()
        self.root.title("NLPApp")
        icon = PhotoImage(file='resources/NLPApp.png')
        self.root.iconphoto(True, icon)
        self.root.geometry("400x620")
        self.root.configure(bg="#47462D")

        self.login_gui()

        self.root.mainloop()




    def login_gui(self):
        self.clear()

        card = Frame(self.root, bg="#A39C90", padx=40, pady=40)
        card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=520)

        heading = Label(card,text="NLPApp", bg="#A39C90", fg="#C66342")
        heading.grid(row=0, column=0, columnspan=2, pady=(0, 6))
        heading.configure(font=("Verdana", 26, "bold"))

        subtitle = Label(card, text="Sign in to continue", bg="#A39C90", fg="#1C1C1C")
        subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 28))
        subtitle.configure(font=("Verdana", 9))

        label1 = Label(card, text="EMAIL", bg="#A39C90", fg="#373535")
        label1.grid(row=2, column=0, columnspan=2, sticky="w", pady=(0, 4))
        label1.configure(font=("Verdana", 8, "bold"))

        self.email_input = Entry(card, width=34, bg="#D9C5A0", fg="#262525")
        self.email_input.grid(row=3, column=0, columnspan=2, ipady=8, ipadx=8, pady=(0, 18), sticky="ew")

        label2 = Label(card, text="PASSWORD", bg="#A39C90", fg="#202020")
        label2.grid(row=4, column=0, columnspan=2, sticky="w", pady=(0, 4))
        label2.configure(font=("Verdana", 8, "bold"))

        self.password_input = Entry(card, width=34, show='*',bg="#D9C5A0", fg="#2A2928")
        self.password_input.grid(row=5, column=0, columnspan=2, ipady=8, ipadx=8, pady=(0, 28), sticky="ew")
        

        login_btn = Button(card, text="LOGIN", width=28, height=2, bg="#E85B34", fg="white", font=("Verdana", 10, "bold"), command = self.perform_login)
        login_btn.grid(row=6, column=0, columnspan=2, pady=(0, 24))

        divider = Frame(card, bg="#C4A882", height=1)
        divider.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(0, 16))

        label3 = Label(card, text="Not a member?", bg="#F2E8D9", fg="#7D6B5D")
        label3.grid(row=8, column=0, columnspan=2, pady=(0, 8))
        label3.configure(font=("Verdana", 9))
        

        redirect_btn = Button(card, text="Sign Up", width=15, command=self.register_gui, bg="#47462D", fg="#F2E8D9", font=("Verdana", 9, "bold"))
        redirect_btn.grid(row=9, column=0, columnspan=2)




    def register_gui(self):
        self.clear()

        card = Frame(self.root, bg="#A39C90", padx=40, pady=40)
        card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=520)

        heading = Label(card,text="NLPApp", bg="#A39C90", fg="#C66342")
        heading.grid(row=0, column=0, columnspan=2, pady=(0, 6))
        heading.configure(font=("Verdana", 26, "bold"))

        subtitle = Label(card, text="Create your account", bg="#A39C90", fg="#1C1C1C")
        subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 28))
        subtitle.configure(font=("Verdana", 9))

        label0 = Label(card, text="FULL NAME", bg="#A39C90", fg="#373535")
        label0.grid(row=2, column=0, columnspan=2, sticky="w", pady=(0, 4))
        label0.configure(font=("Verdana", 8, "bold"))

        self.name_input = Entry(card, width=34, bg="#D9C5A0", fg="#262525")
        self.name_input.grid(row=3, column=0, columnspan=2, ipady=8, ipadx=8, pady=(0, 18), sticky="ew")

        label1 = Label(card, text="EMAIL", bg="#A39C90", fg="#373535")
        label1.grid(row=4, column=0, columnspan=2, sticky="w", pady=(0, 4))
        label1.configure(font=("Verdana", 8, "bold"))

        self.email_input = Entry(card, width=34, bg="#D9C5A0", fg="#262525")
        self.email_input.grid(row=5, column=0, columnspan=2, ipady=8, ipadx=8, pady=(0, 18), sticky="ew")

        label2 = Label(card, text="PASSWORD", bg="#A39C90", fg="#202020")
        label2.grid(row=6, column=0, columnspan=2, sticky="w", pady=(0, 4))
        label2.configure(font=("Verdana", 8, "bold"))

        self.password_input = Entry(card, width=34, show='*',bg="#D9C5A0", fg="#2A2928")
        self.password_input.grid(row=7, column=0, columnspan=2, ipady=8, ipadx=8, pady=(0, 28), sticky="ew")
        

        register_btn = Button(card, text="REGISTER", width=28, height=2, bg="#E85B34", fg="white", font=("Verdana", 10, "bold"), command = self.perform_registration)
        register_btn.grid(row=8, column=0, columnspan=2, pady=(0, 24))

        divider = Frame(card, bg="#C4A882", height=1)
        divider.grid(row=9, column=0, columnspan=2, sticky="ew", pady=(0, 16))

        label3 = Label(card, text="Already a member?", bg="#F2E8D9", fg="#7D6B5D")
        label3.grid(row=10, column=0, columnspan=2, pady=(0, 8))
        label3.configure(font=("Verdana", 9))
        

        redirect_btn = Button(card, text="Sign In",width=15, command=self.login_gui, bg="#47462D", fg="#F2E8D9", font=("Verdana", 9, "bold"))
        redirect_btn.grid(row=11, column=0, columnspan=2)



    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()



    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.db.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success', 'Resistration successful You can login now')
            self.login_gui()

        else:
            messagebox.showerror('Error','Email already exists')




    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.db.search(email,password)

        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email/password')




    def home_gui(self):
        self.clear()
        card = Frame(self.root, bg="#A39C90", padx=30, pady=30)
        card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=520)

        heading = Label(card, text="NLPApp", bg="#A39C90", fg="#C66342")
        heading.grid(row=0, column=0, columnspan=2, pady=(0, 6))
        heading.configure(font=("Verdana", 26, "bold"))

        
        subtitle = Label(card, text="Welcome to NLPApp", bg="#A39C90", fg="#1C1C1C")
        subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        subtitle.configure(font=("Verdana", 9,"bold"))

        divider = Frame(card, bg="#C4A882", height=1)
        divider.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 28))

        langdetect_btn = Button(card, text="Language detection", width=28, height=3, bg="#8B7B1E", fg="white", font=("Verdana", 10, "bold"), command =  self.detectlang_gui)
        langdetect_btn.grid(row=4, column=0, columnspan=2, pady=(0, 24))

        ner_btn = Button(card, text="Name Entity Recognization", width=28, height=3, bg="#8B7B1E", fg="white", font=("Verdana", 10, "bold"), command = self.ner_gui)
        ner_btn.grid(row=5, column=0, columnspan=2, pady=(0, 24))

        emotion_btn = Button(card, text="Emotion Prediction", width=28, height=3, bg="#8B7B1E", fg="white", font=("Verdana", 10, "bold"), command =  self.emotion_gui)
        emotion_btn.grid(row=6, column=0, columnspan=2, pady=(0, 50))

        logout_btn = Button(card, text="LOGOUT", width=15, height=1, bg="#BE0707", fg="white", font=("Verdana", 10, "bold"), command = self.login_gui)
        logout_btn.grid(row=7, column=1, columnspan=2,sticky="ew")     




    def detectlang_gui(self):
        self.clear()
        card = Frame(self.root, bg="#A39C90", padx=30, pady=30)
        card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=530)

        heading = Label(card, text="NLPApp", bg="#A39C90", fg="#C66342")
        heading.grid(row=0, column=0, columnspan=2, pady=(0, 6))
        heading.configure(font=("Verdana", 26, "bold"))

        
        subtitle = Label(card, text="Language detection", bg="#A39C90", fg="#1C1C1C")
        subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        subtitle.configure(font=("Verdana", 9,"bold"))

        divider = Frame(card, bg="#C4A882", height=1)
        divider.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 28))

        label1 = Label(card, text="Enter Text:", bg="#F2E8D9", fg="#7D6B5D")
        label1.grid(row=5, column=0, columnspan=2, pady=(0, 15), sticky='w')
        label1.configure(font=("Verdana", 14))

        self.language_input = Text(card, width=28,height = 5, bg="#D9C5A0", fg="#262525", wrap = WORD)
        self.language_input.grid(row=6, column=0, columnspan=2, ipady=28, ipadx=28, pady=(0, 20), sticky="ew")

        detectlang_btn = Button(card, text="Proceed", width=28, height=2, bg="#8B7B1E", fg="white", font=("Verdana", 10, "bold"), command = self.do_language_detection)
        detectlang_btn.grid(row=7, column=0, columnspan=2, pady=(0, 20))

        self.language_result = Label(card, text="", bg="#F2E8D9", fg="#7D6B5D")
        self.language_result.grid(row=8, column=0, columnspan=2, pady=(0, 15))
        self.language_result.configure(font=("Verdana", 12))

        back_btn = Button(card, text="BACK", width=15, height=1, bg="#8B2B1E", fg="white", font=("Verdana", 10, "bold"), command =  self.home_gui)
        back_btn.grid(row=11, column=0, columnspan=2, sticky='e')




    def ner_gui(self):
        self.clear()
        card = Frame(self.root, bg="#A39C90", padx=30, pady=30)
        card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=530)

        heading = Label(card, text="NLPApp", bg="#A39C90", fg="#C66342")
        heading.grid(row=0, column=0, columnspan=2, pady=(0, 6))
        heading.configure(font=("Verdana", 26, "bold"))

        
        subtitle = Label(card, text="NER Analysis", bg="#A39C90", fg="#1C1C1C")
        subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        subtitle.configure(font=("Verdana", 9,"bold"))

        divider = Frame(card, bg="#C4A882", height=1)
        divider.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 28))

        label1 = Label(card, text="Enter Text:", bg="#F2E8D9", fg="#7D6B5D")
        label1.grid(row=5, column=0, columnspan=2, pady=(0, 15), sticky='w')
        label1.configure(font=("Verdana", 14))

        self.ner_input = Text(card, width=28,height = 5, bg="#D9C5A0", fg="#262525", wrap = WORD)
        self.ner_input.grid(row=6, column=0, columnspan=2, ipady=28, ipadx=28, pady=(0, 30), sticky="ew")

        ner_btn = Button(card, text="Proceed", width=28, height=2, bg="#8B7B1E", fg="white", font=("Verdana", 10, "bold"))
        ner_btn.grid(row=7, column=0, columnspan=2, pady=(0, 20))

        self.ner_result = Label(card, text="", bg="#F2E8D9", fg="#7D6B5D")
        self.ner_result.grid(row=8, column=0, columnspan=2, pady=(0, 15))
        self.ner_result.configure(font=("Verdana", 12))

        back_btn = Button(card, text="BACK", width=15, height=1, bg="#8B2B1E", fg="white", font=("Verdana", 10, "bold"), command =  self.home_gui)
        back_btn.grid(row=11, column=0, columnspan=2, sticky='e')



    def emotion_gui(self):
        self.clear()
        card = Frame(self.root, bg="#A39C90", padx=30, pady=30)
        card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=530)

        heading = Label(card, text="NLPApp", bg="#A39C90", fg="#C66342")
        heading.grid(row=0, column=0, columnspan=2, pady=(0, 6))
        heading.configure(font=("Verdana", 26, "bold"))

        
        subtitle = Label(card, text="Emotion Analysis", bg="#A39C90", fg="#1C1C1C")
        subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        subtitle.configure(font=("Verdana", 9,"bold"))

        divider = Frame(card, bg="#C4A882", height=1)
        divider.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 28))

        label1 = Label(card, text="Enter Text:", bg="#F2E8D9", fg="#7D6B5D")
        label1.grid(row=5, column=0, columnspan=2, pady=(0, 15), sticky='w')
        label1.configure(font=("Verdana", 14))

        self.emotion_input = Text(card, width=28,height = 5, bg="#D9C5A0", fg="#262525", wrap = WORD)
        self.emotion_input.grid(row=6, column=0, columnspan=2, ipady=28, ipadx=28, pady=(0, 30), sticky="ew")

        emotion_btn = Button(card, text="Proceed", width=28, height=2, bg="#8B7B1E", fg="white", font=("Verdana", 10, "bold"))
        emotion_btn.grid(row=7, column=0, columnspan=2, pady=(0, 20))

        self.emotion_result = Label(card, text="", bg="#F2E8D9", fg="#7D6B5D")
        self.emotion_result.grid(row=8, column=0, columnspan=2, pady=(0, 15))
        self.emotion_result.configure(font=("Verdana", 12))

        back_btn = Button(card, text="BACK", width=15, height=1, bg="#8B2B1E", fg="white", font=("Verdana", 10, "bold"), command =  self.home_gui)
        back_btn.grid(row=11, column=0, columnspan=2, sticky='e')


    def do_language_detection(self):
        text = self.language_input.get("1.0", END).strip()
        result = self.api.language_detection(text)
        txt =''
        for i in result['languages']:
            for j in i:
                #print(j,i[j])
                txt = txt + j + ' -> ' + str(i[j]) + '\n'
            
        self.language_result['text'] = txt


nlp = NLPApp()

