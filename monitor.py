import time
from AppKit import NSPasteboard, NSString

def get_clipboard_content():
    pasteboard = NSPasteboard.generalPasteboard()
    content = pasteboard.stringForType_(NSString.stringWithString_("public.utf8-plain-text"))
    return content

def main():
    last_content = None
    while True:
        current_content = get_clipboard_content()
        if current_content != last_content:
            print(f"```{current_content}```")
            last_content = current_content
        time.sleep(1)

if __name__ == "__main__":
    main()
