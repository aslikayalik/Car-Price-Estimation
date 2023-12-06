from tkinter import *
from json import dumps
import sahibinden

pencere = Tk()
pencere.geometry("1000x650")

dropdowns = []
entries = []
model = "/otomobil"
bg_color = "#add8e6"
results = []
page=0

frame_ust = Frame(pencere, bg=bg_color)
frame_ust.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

frame_alt_sol = Frame(pencere,bg=bg_color)
frame_alt_sol.place(relx=0.05, rely=0.18, relwidth=0.27, relheight=0.77)

frame_alt_sag = Frame(pencere, bg=bg_color)
frame_alt_sag.place(relx=0.34, rely=0.18, relwidth=0.61, relheight=0.77)

mainHead = Label(frame_ust, bg=bg_color,text="CAR PRICE ESTIMATION APP", font="Verdana 16 bold")
mainHead.pack(padx=10, pady=10)

head1 = Label(frame_alt_sol, bg=bg_color, text="Enter Inputs : ", font="Verdana 12 bold").pack(padx=10, pady=10, anchor=NW)
head2 = Label(frame_alt_sag, bg=bg_color, text=f"Estimation Results: {len(results)} entry", font="Verdana 12 bold")
head2.pack(padx=10, pady=10, anchor=NW)

dropdown_frame = Frame(frame_alt_sol, bg=bg_color)
dropdown_frame.place(relx=0, rely=0, relwidth=1, relheight=0.5)

menu = StringVar()
options_list = sahibinden.get_options()
options = [o[0] for o in options_list]

def reset(): 

    global options_list
    global options
    global entries

    for d in dropdowns: 
        d.pack_forget()

    for e in entries: 
        e.delete(0, "end")

    options_list = sahibinden.get_options()
    options = [o[0] for o in options_list]


def add_new_input(choice):  

    global options_list
    global options
    global model

    for o in options_list: 
        if o[0] == choice: 
            model = o[1]
            options_list = sahibinden.get_options(o[1])
            if len(options_list) == 0: 
                return
            break

    m = StringVar()
    options = [o[0] for o in options_list]
    d = OptionMenu(dropdown_frame, m, *options, command=add_new_input)
    d.config(width=75)
    dropdowns.append(d)
    d.pack(anchor=NW, pady=5, padx=15)

dropdown = OptionMenu(dropdown_frame, menu, command=add_new_input, *options)
dropdown.config(width=75)

menu.set("Marka")
dropdown.pack(anchor=NW, pady=5, padx=15)

reset_button = Button(frame_alt_sol, text="Reset", height=3, width=75, command=reset)
reset_button.pack(anchor=SW, pady=5, padx=15, side=BOTTOM)

entry_year=Entry(frame_alt_sol, width=75)
entry_year.pack(anchor=NW, pady=5, padx=15, side=BOTTOM)
field2 = Label(frame_alt_sol, bg=bg_color,text="Year:", font="Verdana 10")
field2.pack(anchor=NW, pady=5, padx=15, side=BOTTOM)
entries.append(entry_year)


entry_km = Entry(frame_alt_sol, width=75)
entry_km.pack(anchor=NW, pady=5, padx=15, side=BOTTOM)
field4 = Label(frame_alt_sol, bg=bg_color, text="Km:", font="Verdana 10")
field4.pack(anchor=NW, pady=5, padx=15, side=BOTTOM)
entries.append(entry_km)

entry_size = Entry(frame_alt_sol, width=75)
entry_size.insert(0, 50)
entry_size.pack(anchor=NW, pady=5, padx=15, side=BOTTOM)
field4 = Label(frame_alt_sol, bg=bg_color, text="Sample Size:", font="Verdana 10")
field4.pack(anchor=NW, pady=5, padx=15, side=BOTTOM)
entries.append(entry_size)


def next_page():
    global page 
    if (page * 15) >= len(results): 
        return
    page += 1 
    fill_table()

def prev_page(): 
    global page
    if page != 0: 
        page -= 1 
    fill_table()

def show():
    label.config(text=clicked.get())

results_grid = Frame(frame_alt_sag, bg="#dee2e6")

results_grid.columnconfigure((0, ), weight=10)
results_grid.columnconfigure((1, 2, 3), weight=3)
results_grid.rowconfigure((0, ), )
Button(results_grid, text="^", command=prev_page).place(relx=0.97, rely=0.06, relheight=0.05, relwidth=0.03)
Button(results_grid, text="v", command=next_page).place(relx=0.97, rely=0.95, relheight=0.05, relwidth=0.03)

headers = ["TITLE", "YEAR", "KM", "PRICE"]

for i in range(len(headers)): 
    header = Label(results_grid, font="Verdana 10 bold", bg="#ced4da", text=headers[i]).grid(row=0, column=i, sticky="ew")

results_grid.place(relwidth=0.94, relheight=0.75, relx=0.03, rely=0.1)

price_area = Label(frame_alt_sag,text="??? ₺", font="Verdana 20")
price_area.place(relwidth=0.4, relheight=0.075, relx=0.03, rely=0.9)

def fill_table(): 

    for i in range(0, 15):
        r_index = page * 15 + i
        if  r_index == len(results) - 1: 
            break
        values = list(results[r_index].values())
        for j in range(len(values)): 
            cell = Label(results_grid, font="Verdana 10", text=str(values[j])[0:30]).grid(row=i + 1, column=j, sticky="ns")


def get_price_estimation():

    global results 

    year = entry_year.get()
    km = entry_km.get()
    size = int(entry_size.get())

    results = sahibinden.get_results(model, year, km, size)
    price = sahibinden.get_estimated_price(results)

    fill_table()

    price_area.config(text=f"{price:,}₺")
    head2.config(text=f"Estimation Results: {len(results)} entry")
    

def export_data():

    f = open("output.json", "w")
    f.write(dumps(results, indent=4))
    f.close()
    top = Toplevel(pencere)
    top.geometry("250x250")
    top.title("Sucessfully exported")
    Label(top, text="Data succesfully \nexported to \n'output.json'.", font="Verdana 16").place(rely=0.45)


get_prices_button = Button(frame_alt_sag, text="Export Data ", height=3, width=10, command=export_data)
get_prices_button.pack(anchor=SE,pady=5,padx=15,side=RIGHT)

get_prices_button = Button(frame_alt_sag, text="Get Price ", height=3, width=10, command=get_price_estimation)
get_prices_button.pack(anchor=SE,pady=5,padx=15,side=RIGHT)

pencere.mainloop()
