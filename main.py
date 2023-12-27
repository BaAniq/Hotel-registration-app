from tkinter import Tk, Canvas, PhotoImage

beige = '#FAF6F0'


# creating a  main window
def create_main_window():
    main_window = Tk()
    main_window.minsize(width=300, height=200)
    main_window.title('Hotel registration')
    main_window.config(bg=beige)

    canvas_hotel_pic = Canvas(width=189, height=266, bg=beige, highlightthickness=0)
    image = PhotoImage(file='hotel.png')
    canvas_hotel_pic.create_image(94, 133, image=image)
    canvas_hotel_pic.grid(column=1, row=1)

    main_window.mainloop()




create_main_window()
