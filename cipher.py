import tkinter as tk

def main():
  # Top level window
  root = tk.Tk()
  root.title("Caesar Cipher")
  root.geometry('500x350')
  root.configure(bg="#f0f0f0")  # Light gray background
  root.resizable(True, True)  # Allow resizing
  root.iconbitmap('icon.ico')  # Set window icon

  # Configure grid weights for responsiveness
  root.grid_rowconfigure(0, weight=1)
  root.grid_rowconfigure(1, weight=1)
  root.grid_rowconfigure(2, weight=1)
  root.grid_columnconfigure(0, weight=1)

  # Global variable to store the encryption value
  global encryption_value
  encryption_value = 0

  def encrypt():
    global encryption_value
    try:
      # Retrieve encryption key from the key entry widget
      key = key_entry.get()
      encryption_value = int(key)
      if encryption_value < 1 or encryption_value > 25:
        lbl_result.config(text="Invalid encryption value. Please enter a number between 1 and 25.", fg="red")
        return
    except ValueError:
      lbl_result.config(text="Invalid encryption value. Please enter a number.", fg="red")
      return

    # Get text from input textbox
    unencrypted = inputtxt.get(1.0, "end-1c")
    encrypted = ""

    # Perform Caesar cipher encryption
    for char in unencrypted:
      if char.isalpha():  # Check if the character is a letter
        shift = encryption_value % 26
        if char.islower():
          encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif char.isupper():
          encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
      else:
        encrypted += char  # Non-alphabetic characters remain unchanged

    lbl_result.config(text="Encrypted Text: " + encrypted, fg="#2196F3")

  # Instruction label at the top
  lbl_instructions = tk.Label(root, text="Enter your message below, set the encryption key (1-25), and click Encrypt.",
                               bg="#f0f0f0", font=("Arial", 12, "italic"), fg="#333333", wraplength=480, justify="center")
  lbl_instructions.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="nsew")

  # Frame for input and key settings
  input_frame = tk.Frame(root, bg="#f0f0f0")
  input_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
  input_frame.grid_rowconfigure(0, weight=1)
  input_frame.grid_columnconfigure(0, weight=1)

  # TextBox Creation for the message input
  inputtxt = tk.Text(input_frame, height=6, font=("Arial", 12))
  inputtxt.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

  # Label and Entry for encryption key
  key_frame = tk.Frame(input_frame, bg="#f0f0f0")  # Create a frame to group the label and entry
  key_frame.grid(row=1, column=0, columnspan=2, pady=(5, 10))  # Center the frame using columnspan

  key_label = tk.Label(key_frame, text="Encryption Key:", bg="#f0f0f0", font=("Arial", 10))
  key_label.grid(row=0, column=0, padx=(10, 5), pady=(5, 10))

  key_entry = tk.Entry(key_frame, font=("Arial", 10), width=10)
  key_entry.grid(row=0, column=1, padx=(5, 10), pady=(5, 10))

  # Button Creation Frame for action buttons
  button_frame = tk.Frame(root, bg="#f0f0f0")
  button_frame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

  encryptButton = tk.Button(button_frame, text="Encrypt", command=encrypt,
                            bg="#2196F3", fg="white", font=("Arial", 10), width=15)
  encryptButton.pack(pady=5)

  # Label for results
  lbl_result = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12))
  lbl_result.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

  root.mainloop()

if __name__ == "__main__":
  main()
