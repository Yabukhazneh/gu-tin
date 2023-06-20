 

import tkinter as tk



#Creting an instance of class Tk from tkinter library
gui = tk.Tk()
gui.title("USGS Earthquake Historical Data Tool")
gui.iconbitmap("IGI_icon.ico")
gui.configure(bg='#264365')

# Defining the introduction and explanantion presented at the start of the tool
welcome_s ="Welcome to the Earthquake Data Tool!"
intro_s1 = """
This tool will take a given position, P1 (described by latitude and longitude coordinates) and return all past earthquakes that are within a given radius of P1 and above a certain minimum magnitude. In addition, the MMI (Modified Mercalli Intensity) relative to P1 for each of the past earthquakes is calculated. 

To export the results to an Excel File please press the ‘Export to Excel’ button.

To exit the program, please press the ‘Exit’."""
    
#Defining needed widgets for GUI
welcome_label = tk.Label(gui, bg = '#264365', text = welcome_s, anchor = tk.CENTER, 
                            font=("Open Sans", 17, 'bold'), fg = "#ffffff", pady = 5)

info_text = tk.Text(gui, font=("Open Sans", 13), bg = '#264365', fg = "#ffffff", 
                    bd = -2, wrap = tk.WORD, width = 58, padx=30, height=14)
info_text.insert(tk.END, intro_s1)


lat_label = tk.Label(gui, text = "Enter latitude value:", font=("Open Sans", 13, 'bold'), 
                        bg = '#264365', fg = "#ffffff", bd = -2, anchor = tk.W, padx = 2,
                        pady = 8)
lat_entry = tk.Entry(gui, font=("Open Sans", 12, 'bold'), fg = '#264365')


long_label = tk.Label(gui, text = "Enter longitude value:", font=("Open Sans", 13, 'bold'), 
                        bg = '#264365', fg = "#ffffff", bd = -2, anchor = tk.W, padx = 2,
                        pady = 8)
long_entry = tk.Entry(gui, font=("Open Sans", 12, 'bold'), fg = '#264365')


rad_label = tk.Label(gui, text = "Enter radius value (in km):", font=("Open Sans", 13, 'bold'), 
                        bg = '#264365', fg = "#ffffff", bd = -2, anchor = tk.W, padx = 2,
                        pady = 8)
rad_entry = tk.Entry(gui, font=("Open Sans", 12, 'bold'), fg = '#264365')


minmag_label = tk.Label(gui, text = "Enter minimum magnitude value:", font=("Open Sans", 13, 'bold'),
                        bg = '#264365', fg = "#ffffff", bd = -2, anchor = tk.W, padx = 2,
                        pady = 8)
minmag_entry = tk.Entry(gui, font=("Open Sans", 12, 'bold'), fg = '#264365')
    
error_values = tk.Label(gui, font=("Open Sans", 11), bg = '#264365', fg = "#ff1919", 
                        bd = -2, anchor = tk.W, padx = 2, pady = 8)

exportcsv_button = tk.Button(gui, text = "Export to Excel", fg = "#264365", command = query_data,
                                font=("Open Sans", 12, 'bold'), cursor = 'hand2', width =14) 
exitbutton = tk.Button(gui, text = "Exit", command = gui.destroy, fg = "#264365",
                        font=("Open Sans", 12, 'bold'), cursor = 'hand2', width =14)
    
#Placing defined widgets on gui
welcome_label.grid(row = 0, columnspan = 5)
info_text.grid(row = 1, columnspan = 5)

lat_label.grid(row = 2, column = 1, sticky = tk.W)
lat_entry.grid(row = 2, column = 2, sticky = tk.W)

long_label.grid(row = 3, column = 1, sticky = tk.W)
long_entry.grid(row = 3, column = 2, sticky = tk.W)

rad_label.grid(row = 4, column = 1, sticky = tk.W)
rad_entry.grid(row = 4, column = 2, sticky = tk.W)

minmag_label.grid(row = 5, column = 1, sticky = tk.W)
minmag_entry.grid(row = 5, column = 2, sticky = tk.W)

error_values.grid(row = 6, column = 1, sticky = tk.W)

# search_button.grid(row = 7, column =1, columnspan = 2, pady = 9)
exportcsv_button.grid(row = 9, column = 1, columnspan = 2, pady = 9)
# success_export.grid(row = 10, column = 5, sticky = tk.W)
exitbutton.grid(row = 11, column = 1, columnspan = 2, pady = 9)

gui.mainloop()
