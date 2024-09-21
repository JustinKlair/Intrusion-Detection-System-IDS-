import customtkinter as ctk

# Initialize the main window
app = ctk.CTk()
app.geometry("900x600")
app.title("IntruGuard Sign In")

# Set the theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Define your custom blue color
CUSTOM_BLUE = '#324A7C'

# Define light mode colors
LIGHT_MODE = {
    'background': '#EAEAEA',
    'text': 'black',
    'button_bg': 'white',
    'border_color': CUSTOM_BLUE,
    'entry_bg': '#FFFFFF',
    'entry_border': '#D3D3D3',
}

# Sign-In Frame Design
def sign_in_page():
    sign_in_frame = ctk.CTkFrame(master=app, width=700, height=500, corner_radius=10, fg_color=LIGHT_MODE['background'])
    sign_in_frame.pack(padx=20, pady=40, fill="both", expand=True)

    # Title
    title_label = ctk.CTkLabel(sign_in_frame, text="IntruGuard", font=("Arial", 32, "bold"), text_color=CUSTOM_BLUE)
    title_label.pack(pady=(30, 10))

    # Subtitle
    subtitle_label = ctk.CTkLabel(sign_in_frame, text="Sign in to continue", font=("Arial", 18), text_color=LIGHT_MODE['text'])
    subtitle_label.pack(pady=(0, 30))

    # Username Entry
    username_entry = ctk.CTkEntry(sign_in_frame, width=320, fg_color=LIGHT_MODE['entry_bg'], text_color=LIGHT_MODE['text'],
                                   border_color=LIGHT_MODE['entry_border'], border_width=2, corner_radius=8)
    username_entry.pack(pady=(30, 10))
    username_entry.insert(0, "Username")  # Placeholder for username

    # Password Entry
    password_entry = ctk.CTkEntry(sign_in_frame, width=320, fg_color=LIGHT_MODE['entry_bg'], text_color=LIGHT_MODE['text'],
                                   border_color=LIGHT_MODE['entry_border'], border_width=2, corner_radius=8, show="*")
    password_entry.pack(pady=(10, 10))
    password_entry.insert(0, "Password")  # Placeholder for password

    # "Remember Me" Checkbox
    remember_me_var = ctk.BooleanVar()
    remember_me_checkbox = ctk.CTkCheckBox(sign_in_frame, text="Remember Me", variable=remember_me_var, text_color=LIGHT_MODE['text'])
    remember_me_checkbox.pack(pady=(5, 5))

    # Forgot Password Label
    forgot_password_label = ctk.CTkLabel(sign_in_frame, text="Forgot Password?", font=("Arial", 12), text_color=CUSTOM_BLUE)
    forgot_password_label.pack(pady=(5, 20))

    # Sign In Button
    sign_in_button = ctk.CTkButton(sign_in_frame, text="Sign In", width=320, height=50, font=("Arial", 16),
                                   fg_color=CUSTOM_BLUE, text_color="white", corner_radius=8)
    sign_in_button.pack(pady=(20, 10))

    # Sign Out Button (same size as Sign In)
    sign_out_button = ctk.CTkButton(sign_in_frame, text="Sign Out", width=320, height=50, font=("Arial", 16),
                                    fg_color="gray", text_color="white", corner_radius=8)
    sign_out_button.pack(pady=(10, 20))

# Load the Sign-In Page
sign_in_page()

# Start the app loop
app.mainloop()
