import tkinter
from tkinter import ttk
form = tkinter.Tk()
form.geometry("700x500")

lblh = ttk.Label(form ,text = "labelh")
lbl1 = ttk.Label(form ,text = "label1")
lbl2 = ttk.Label(form ,text = "label2")
lbl3 = ttk.Label(form ,text = "label3")
lbl4 = ttk.Label(form ,text = "label4")
lbl5 = ttk.Label(form ,text = "label5")

lbl1.config(background ="navy",foreground ="lightblue")
lbl1.config(font=("aurial",25),padding=20)

lbl2.config(background ="red",foreground ="pink",padding =20)

lblh.pack()
lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
lbl5.pack()
form.mainloop()
