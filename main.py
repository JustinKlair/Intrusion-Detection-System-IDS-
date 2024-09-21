import customtkinter as ctk

# Initialize the main window
app = ctk.CTk()
app.geometry("900x600")
app.title("IntruGuard")

# Set the theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Configure grid to make elements stretchable
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=0)  # Sidebar
app.grid_columnconfigure(1, weight=1)  # Main content

# Define light mode colors
LIGHT_MODE = {
    'background': '#EAEAEA',
    'text': 'black',
    'button_bg': 'white',
    'border_color': '#324A7C',
    'sidebar_bg': '#2B3A67'
}

# Define dark mode colors
DARK_MODE = {
    'background': '#2B2B2B',
    'text': 'white',
    'button_bg': 'white',
    'border_color': '#474747',
    'sidebar_bg': '#000000'
}

def mainFrame():
    # Main content frame
    main_frame = ctk.CTkFrame(master=app, width=1000, height=800, corner_radius=0, fg_color=LIGHT_MODE['background'])
    main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    # Configure button grid layout
    main_frame.grid_rowconfigure((0, 1), weight=1)
    main_frame.grid_columnconfigure((0, 1), weight=1)

    # Main content buttons
    button1_main = ctk.CTkButton(master=main_frame, width=300, height=200, fg_color=LIGHT_MODE['button_bg'], text="Real-Time Alerts",
                             font=("Arial", 20, "bold"), text_color="#474747",
                             border_color=LIGHT_MODE['border_color'], border_width=2,
                             command=lambda: on_button_click(1))


    button1_main.grid(row=0, column=0, padx=20, pady=20)

    button2_main = ctk.CTkButton(master=main_frame, width=300, height=200, fg_color=LIGHT_MODE['button_bg'],
                                 font=("Arial", 20, "bold"), text_color="#474747",
                                 border_color=LIGHT_MODE['border_color'], border_width=2, text="Network Flow",
                                 command=lambda: on_button_click(2))
    button2_main.grid(row=0, column=1, padx=20, pady=20)

    button3_main = ctk.CTkButton(master=main_frame, width=300, height=200, fg_color=LIGHT_MODE['button_bg'],
                                 font=("Arial", 20, "bold"), text_color="#474747", border_width=2, text="Malicious IPs",
                                 command=lambda: on_button_click(3))
    button3_main.grid(row=1, column=0, padx=20, pady=20)

    button4_main = ctk.CTkButton(master=main_frame, width=300, height=200, fg_color=LIGHT_MODE['button_bg'],
                                 font=("Arial", 20, "bold"), text_color="#474747", border_width=2, text="Packet Monitoring Summary",
                                 command=lambda: on_button_click(4))
    button4_main.grid(row=1, column=1, padx=20, pady=20)

def sidebar():
    # Sidebar frame
    sidebar_frame = ctk.CTkFrame(master=app, width=200, height=800, corner_radius=0, fg_color=LIGHT_MODE['sidebar_bg'])
    sidebar_frame.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

    # Sidebar content
    title_label = ctk.CTkLabel(master=sidebar_frame, text="IntruGuard", fg_color=LIGHT_MODE['border_color'],
                               corner_radius=0, width=180, height=50, font=("Arial", 18, "bold"), text_color="white")
    title_label.grid(row=0, column=0, pady=(20, 10))

    sbutton1 = ctk.CTkButton(master=sidebar_frame, text="Dashboard", width=180, height=60,
                             fg_color="#6D6E71", hover_color="#D3D3D3", border_color="white", border_width=2,
                             command=lambda: on_sidebutton_click(1))
    sbutton1.grid(row=1, column=0, pady=10, padx=10)

    sbutton2 = ctk.CTkButton(master=sidebar_frame, text="Contact Us", width=180, height=60,
                             fg_color="#6D6E71", hover_color="#D3D3D3", border_color="white", border_width=2,
                             command=lambda: on_sidebutton_click(2))
    sbutton2.grid(row=2, column=0, pady=70, padx=10)

    sbutton3 = ctk.CTkButton(master=sidebar_frame, text="Settings", width=180, height=60,
                             fg_color="#6D6E71", hover_color="#D3D3D3", border_color="white", border_width=2,
                             command=lambda: on_sidebutton_click(3))
    sbutton3.grid(row=3, column=0, pady=10, padx=10)

    sbutton4 = ctk.CTkButton(master=sidebar_frame, text="Sign Out", width=180, height=60,
                             fg_color="#6D6E71", hover_color="#D3D3D3", border_color="white", border_width=2,
                             command=lambda: on_sidebutton_click(4))
    sbutton4.grid(row=4, column=0, pady=70, padx=10)

def settings():

       # Main Frame (same size)
    main_frame = ctk.CTkFrame(master=app, width=500, height=400, corner_radius=0, fg_color="#EAEAEA")
    main_frame.grid(row=0, column=1, sticky="nsew")

    # Configure grid layout for the settings content
    main_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

    # Settings Label (adjust padx to move it left)
    settings_label = ctk.CTkLabel(master=main_frame, text="Settings", font=("Arial", 50, "bold"), fg_color="#EAEAEA", text_color="black")
    settings_label.grid(row=0, column=0, padx=(20, 200), pady=20, sticky="w")  # Increase right padding to move left

    # Dark Mode Switch
    switch1 = ctk.CTkSwitch(master=main_frame, text="Dark Mode", command=lambda: on_switch_click(1))
    switch1.grid(row=1, column=0, padx=10, pady=0, sticky="nsew")

    # Basic Switches
    switch2 = ctk.CTkSwitch(master=main_frame, text="Basic Switch", command=lambda: on_switch_click(2))
    switch2.grid(row=2, column=0, padx=10, pady=0, sticky="nsew")

    switch3 = ctk.CTkSwitch(master=main_frame, text="Basic Switch", command=lambda: on_switch_click(3))
    switch3.grid(row=3, column=0, padx=10, pady=0, sticky="nsew")



def submit(name_entry,email_entry,message_entry):
    name = name_entry.get()
    email = email_entry.get()
    message = message_entry.get("1.0", "end")
    print(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        # You can add logic here to handle submission (e.g., sending email)


def contactPage():
    # Main Frame
    main_frame = ctk.CTkFrame(master=app, width=500, height=400, corner_radius=0, fg_color="#EAEAEA")
    main_frame.grid(row=0, column=1, sticky="nsew")

    # Contact Us Label
    contactus_label = ctk.CTkLabel(master=main_frame, text="Contact Us", font=("Arial", 50, "bold"), fg_color="#EAEAEA",
                                  text_color="black")
    contactus_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    # Sidebar frame
    sidebar()
    #Sidebar Content
    sidebar()

    # Name Entry Field
    name_label = ctk.CTkLabel(main_frame, text="Name:")
    name_label.grid(row=1,column=0, sticky="ns", padx=5)
    name_entry = ctk.CTkEntry(main_frame, width=300)
    name_entry.grid(row=2,column=0,pady=5)

    # Email Entry Field
    email_label = ctk.CTkLabel(main_frame, text="Email:")
    email_label.grid(row=3,column=0,sticky="ns", padx=10)
    email_entry = ctk.CTkEntry(main_frame, width=300)
    email_entry.grid(row=4,column=0,padx=20, pady=5)

    # Message Entry Field
    message_label = ctk.CTkLabel(main_frame, text="Message:")
    message_label.grid(row=5,column=0,sticky="ns", padx=10)
    message_entry = ctk.CTkTextbox(main_frame, width=300, height=50)
    message_entry.grid(row=6,column=0,padx=10, pady=5)

    submit_button = ctk.CTkButton(main_frame, text="Submit Now", fg_color="#2B3A67", hover_color="#D3D3D3" , command=lambda : submit(name_entry,email_entry,message_entry))
    submit_button.grid(row=7,column=0,pady=2)


def DarkMode():
     # Clear the current content
    for widget in app.winfo_children():
        widget.destroy()
    #Change into Dark Mode
    # Main content frame
    main_frame = ctk.CTkFrame(master=app, width=500, height=400, corner_radius=0, fg_color="#2B2B2B")  # Dark grey color
    main_frame.grid(row=0, column=1, sticky="nsew")

    # Main content buttons
    button1_main = ctk.CTkButton(master=main_frame, width=150, height=150, fg_color="white", hover_color="#D3D3D3", border_color="#324A7C", border_width=2, text="", command=lambda: on_button_click(1))
    button1_main.grid(row=0, column=0, padx=20, pady=20)

    button2_main = ctk.CTkButton(master=main_frame, width=150, height=150, fg_color="white", hover_color="#D3D3D3", border_color="#324A7C", border_width=2, text="", command=lambda: on_button_click(2))
    button2_main.grid(row=0, column=1, padx=20, pady=20)

    button3_main = ctk.CTkButton(master=main_frame, width=150, height=150, fg_color="white", hover_color="#D3D3D3", border_color="#324A7C", border_width=2, text="", command=lambda: on_button_click(3))
    button3_main.grid(row=1, column=0, padx=20, pady=20)

    button4_main = ctk.CTkButton(master=main_frame, width=150, height=150, fg_color="white", hover_color="#D3D3D3", border_color="#324A7C", border_width=2, text="", command=lambda: on_button_click(4))
    button4_main.grid(row=1, column=1, padx=20, pady=20)

    # Sidebar frame
    sidebar_frame = ctk.CTkFrame(master=app, width=100, height=400, corner_radius=0, fg_color="#000000")  # Black color
    sidebar_frame.grid(row=0, column=0, sticky="ns")

    # Sidebar content
    title_label = ctk.CTkLabel(master=sidebar_frame, text="GuardNet", fg_color="#000000", corner_radius=0, width=100, height=40, font=("Arial", 16, "bold"), text_color="white")
    title_label.grid(row=0, column=0, pady=(10, 0))

    sbutton1 = ctk.CTkButton(master=sidebar_frame, text="", width=50, height=50, fg_color="#474747", hover_color="#D3D3D3", border_color="white", border_width=2, command=lambda: on_sidebutton_click(1))
    sbutton1.grid(row=1, column=0, pady=10, padx=10)

    sbutton2 = ctk.CTkButton(master=sidebar_frame, text="", width=50, height=50, fg_color="#474747", hover_color="#D3D3D3", border_color="white", border_width=2, command=lambda: on_sidebutton_click(2))
    sbutton2.grid(row=2, column=0, pady=10, padx=10)

    sbutton3 = ctk.CTkButton(master=sidebar_frame, text="", width=50, height=50, fg_color="#474747", hover_color="#D3D3D3", border_color="white", border_width=2, command=lambda: on_sidebutton_click(3))
    sbutton3.grid(row=3, column=0, pady=10, padx=10)

def home():
    mainFrame()
    sidebar()

# Button click function
def on_button_click(button_id):
    print(f"Button {button_id} clicked")
    if button_id == 1:
        pass
    # Additional actions for other buttons can be added here

def on_sidebutton_click(sbutton_id):
    print(f"Sidebar Button {sbutton_id} clicked")
    if sbutton_id == 1:
        print("HOME")
        home()
    if sbutton_id == 2:
        print("Contact us")
        contactPage()

    if sbutton_id == 3:
        print("Settings")
        settings()
def on_switch_click(switch_id):
    print(f"Button {switch_id} clicked")
    if switch_id == 1:
        print("CLicked!!!!")
    # Additional actions for other buttons can be added here

# Initialize the main frames
mainFrame()
sidebar()
app.mainloop()

