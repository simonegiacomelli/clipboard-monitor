import time
from AppKit import NSPasteboard, NSString


def get_clipboard_content():
    pasteboard = NSPasteboard.generalPasteboard()
    types = ['public.html', 'public.utf8-plain-text']

    for type_str in types:
        content = pasteboard.stringForType_(NSString.stringWithString_(type_str))
        if content:
            return content

    return None


def main():
    last_content = None
    while True:
        current_content = get_clipboard_content()
        if current_content != last_content:
            print(f'```{current_content}```')
            last_content = current_content
        time.sleep(1)


if __name__ == '__main__':
    main()
