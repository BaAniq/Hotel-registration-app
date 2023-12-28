from tkinter import *
from tkinter import messagebox
import pandas

beige = '#FAF6F0'
back = "←"
menu_listbox = None
labels_to_delete = None
back_button = None

try:
    csv_guest = pandas.read_csv('Guest_List.csv')
except FileNotFoundError:

    room_list = []
    last_name_list = []
    name_list = []
else:

    room_list = csv_guest['Room'].to_list()
    last_name_list = csv_guest['Last_name'].to_list()
    name_list = csv_guest['Name'].to_list()



# creating a  main window

main_window = Tk()
main_window.minsize(width=300, height=200)
main_window.title('Hotel registration')
main_window.config(bg=beige, padx=10, pady=10)

canvas_bg = Canvas(width=189, height=266, bg=beige, highlightthickness=0)
image = PhotoImage(file='hotel.png')
canvas_bg.create_image(94, 133, image=image)

canvas_bg.grid(column=1, row=1, rowspan=6)


def show_menu():
    global menu_listbox, labels_to_delete
    menu_label = Label(text='MENU', bg=beige, font='bold')
    menu_label.grid(column=2, row=1)
    menu_listbox = Listbox(height=4)
    menu_elements = ["Show the Guest List", "Check in guest", "Check out guest", "Edit data"]
    for element in menu_elements:
        menu_listbox.insert(menu_elements.index(element), element)
    menu_listbox.bind("<<ListboxSelect>>", menu_list_box_used)
    menu_listbox.grid(column=2, row=2)
    labels_to_delete = [menu_listbox, menu_label]


def menu_list_box_used(event):
    global menu_listbox, back_button
    choice = menu_listbox.get(menu_listbox.curselection())
    back_button = Button(text=back, command=move_back, font=5)
    back_button.grid(row=4, column=2)
    if choice == "Show the Guest List":
        show_guest_list()
    elif choice == "Check in guest":
        check_in_guest()


def show_guest_list():
    global labels_to_delete
    destroy_view()
    show_guest_listbox = Listbox(height=10)
    guest_elements = [[row.Room, row.Last_name, row.Name]for (index, row) in csv_guest.iterrows()]
    for element in guest_elements:
        show_guest_listbox.insert(guest_elements.index(element), element)

    show_guest_listbox.grid(column=2, row=2)
    labels_to_delete = [back_button, show_guest_listbox]


def check_in_guest():
    global labels_to_delete
    destroy_view()
    name_label = Label(text='Name', font=('Calibre', 10), bg=beige, padx=3)
    name_label.grid(column=2, row=1)

    name_textbox = Entry(width=12)
    name_textbox.grid(column=3, row=1)

    last_name_label = Label(text='Last name', font=('Calibre', 10), bg=beige, padx=3)
    last_name_label.grid(column=2, row=2)

    last_name_textbox = Entry(width=12)
    last_name_textbox.grid(column=3, row=2)

    room_label = Label(text='Room', font=('Calibre', 10), bg=beige, padx=3)
    room_label.grid(column=2, row=3)

    room_textbox = Entry(width=12)
    room_textbox.grid(column=3, row=3)

    def check_in():
        global csv_guest
        name = name_textbox.get()
        last_name = last_name_textbox.get()
        room = room_textbox.get()
        if len(name) == 0 or len(last_name) == 0 or len(room) == 0:
            messagebox.showinfo(title='Empty fields', message='Please make sure there are no empty fields.')
        else:
            room_list.append(room)
            last_name_list.append(last_name)
            name_list.append(name)
            data_check_in = {
                'Room': room_list,
                'Last_name': last_name_list,
                'Name': name_list,
            }
            csv_guest = pandas.DataFrame(data_check_in)
            csv_guest.to_csv('Guest_List.csv', index=False)
            messagebox.showinfo(title='Check in', message='Check in successfully.')
            name_textbox.delete(0, END)
            last_name_textbox.delete(0, END)
            room_textbox.delete(0, END)
            name_textbox.focus()

    check_in_button = Button(text='Check in', command=check_in)
    check_in_button.grid(column=3, row=4)

    labels_to_delete = [check_in_button, back_button, name_label, name_textbox, last_name_label, last_name_textbox, room_label,
                        room_textbox]




def destroy_view():
    global labels_to_delete
    for label in labels_to_delete:
        label.destroy()


def move_back():
    destroy_view()
    show_menu()

show_menu()

main_window.mainloop()