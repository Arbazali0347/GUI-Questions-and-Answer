from tkinter import *
from tkinter import messagebox as mg
import time
money = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
mymoney = 0
qq = 0
 # Start time ko store karne ke liye

# Yeh list globally define ki hai
q = [["Machien learning kare kon si langauge\nuse hoti hai os ka name btao?", "Java", "Python", "PHP", "C++", "Nono", 2],
     ["machine learning le kya konsi\nlangauge sikhni chaye?", "JavaScript", "Python", "PHP", "C++", "Nono", 1],
     ["pakistan key kitne sobay hai\nbtao?", "2", "6", "10", "5", "Nono", 4],
     ["Pakistan kab azade hoa?", "1943", "1940", "1947", "1948", "Nono", 3],
     ["pakistan ko sikne azade karwa?", "Qaize-e-azam", "banzir bhutu", "altaf hussain", "zufiqar", "Nono", 1],
     ["Ai ki Full from kya hai?", "Android", "Apple", "Applicat", "Arti inteligent", "Nono", 4],
     ["data science\nlangauge sikhni chaye?", "Java", "PPK", "PHP", "C++", "Nono", 1],
     ["machine kya konsi\nlangauge sikhni chaye?", "AAC", "Python", "PHP", "C++", "Nono", 2],
     ["free fire kasi hai\nor kon si games hai?", "Noine", "Pyon", "PHP", "C#", "Nono", 3],
     ["paksitan ka wazir-e-azam\nkon hai?", "Java", "Python", "PHP", "Done", "Nono", 1]]
start_time = None 
time_runing = True
def qusestion():
    global qq
    global start_time, time_runing,mymoney
    def update_time():
        global start_time, time_runing,mymoney
        if time_runing:
            elapsed_time = time.time() - start_time
            if elapsed_time > 20:  # Agar 10 seconds se zyada ho jaye
                if mymoney >= 6000:
                    mg.showinfo("Time's Up!", f"Game Over! Time exceeded 20 seconds.\nYour Total Money Rs.{mymoney}")
                else:
                    mymoney = 0
                    mg.showinfo("Time's Up!", f"Game Over! Time exceeded 20 seconds.\nYour Total Money Rs.{mymoney}")
                root.destroy()

            else:
                time_label.config(text=f"Time: {int(elapsed_time)}s")
                root.after(1000, update_time)
    def chack():
        global mymoney, time_runing
        global qq
        time_runing = False
        reselt = choice.get()
        try:
            reselt = int(reselt)
        except Exception:
            mg.showinfo("Ghalat", "Please Enter Your Choice!")
            return
        choice_box.delete(0, END)
        if reselt == q[qq][-1]:
            mymoney += money[qq]
            mg.showinfo("Sahi", f"Sahi jawab!\nAap jeet chuke hain Rs.{money[qq]}")
            qq += 1
            qusestion()
        else:
            if mymoney >= 6000:
                mg.showinfo("Ghalat", f"Ghalat jawab!\nTotal paisay: Rs.{mymoney}")
            else:
                mymoney = 0
                mg.showinfo("Ghalat", f"Ghalat jawab!\nTotal paisay: Rs.{mymoney}")
            root.destroy()
    No1 = Label(root, text="No.1", font=("Times New Roman", 15, "bold"), bg="grey", fg="black")
    No1.place(x=20, y=180, height=20, width=40)
    No2 = Label(root, text="No.2", font=("Times New Roman", 15, "bold"), bg="grey", fg="black")
    No2.place(x=20, y=260, height=20, width=40)
    No3 = Label(root, text="No.3", font=("Times New Roman", 15, "bold"), bg="grey", fg="black")
    No3.place(x=380, y=180, height=20, width=40)
    No4 = Label(root, text="No.4", font=("Times New Roman", 15, "bold"), bg="grey", fg="black")
    No4.place(x=380, y=260, height=20, width=40)

    ans1 = Label(root, text="", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
    ans1.place(x=20, y=200, height=40, width=200)
    ans2 = Label(root, text="", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
    ans2.place(x=20, y=280, height=40, width=200)
    ans3 = Label(root, text="", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
    ans3.place(x=380, y=200, height=40, width=200)
    ans4 = Label(root, text="", font=("Times New Roman", 20, "bold"), bg="white", fg="black")
    ans4.place(x=380, y=280, height=40, width=200)

    time_label = Label(root, text="Time: 0s", font=("Times New Roman", 12, "bold"), bg="grey", fg="black")
    time_label.place(x=500, y=360, height=30, width=100)

    Enter_choice_txt = Label(root, text="Enter Choice (1-4)", font=("Times New Roman", 12, "bold"), bg="grey", fg="black")
    Enter_choice_txt.place(x=225, y=310, height=20, width=150)

    choice = StringVar()
    choice_box = Entry(root, font=("Times New Roman", 15), relief="sunken", bd=4, textvariable=choice)
    choice_box.place(x=180, y=340, height=30, width=130)

    choice_bt = Button(root, text="Ok", font=("Times New Roman", 15), relief=RAISED, fg="black", bg="red", command=chack)
    choice_bt.place(x=330, y=340, height=30, width=130)

    name_user = Label(root,text=name.get(),font=("Times New Roman",12,"bold"),bg="grey",fg="black")
    name_user.place(x=235,y=370,height=30,width=130)


    if qq < len(q):
        qus.config(text=q[qq][0])
        ans1.config(text=q[qq][1])
        ans2.config(text=q[qq][2])
        ans3.config(text=q[qq][3])
        ans4.config(text=q[qq][4])
    else:
        mg.showinfo("Khatam", f"Game Over!\nTotal paisay: Rs.{mymoney}")
        root.destroy()
    start_time = time.time()  # Timer start karo
    time_runing = True
    update_time() 

def game_loop():
    star_bt.destroy()
    Enter_name.destroy()
    text.config(text="Game Start Ho Gayi!")
    name_box.destroy()
    text.destroy()
    qusestion()

root = Tk()
root.geometry("600x400")
root.title("Questons - Answers")
root.config(bg="grey")

label = Label(root, text="MR ARO GAMING", font=("Times New Roman", 30, "bold"), bg="black", fg="white")
label.place(x=0, y=10, height=40, width=600)

qus = Label(root, text="***", font=("Times New Roman", 20, "bold"), bg="black", fg="white")
qus.place(x=0, y=60, height=110, width=600)

Enter_name = Label(root, text=": Enter your Name :", font=("Times New Roman", 15, "bold"), bg="grey", fg="black")
Enter_name.place(x=150, y=180, height=20, width=300)

name = StringVar()
name_box = Entry(root, font=("Times New Roman", 15), relief="sunken", bd=4, textvariable=name)
name_box.place(x=150, y=210, height=30, width=300)

star_bt = Button(root, text="Start", font=("Times New Roman", 20, "bold"), bg="red", fg="black", command=game_loop)
star_bt.place(x=200, y=250, height=35, width=200)

text = Label(root, text="This game is a Questions and answers\ngame. Bohat interesting hai.\nSahi jawab do aur paisay jeeto!", font=("Times New Roman", 15, "bold"), bg="grey", fg="black")
text.place(x=0, y=300, height=90, width=600)


root.mainloop()
