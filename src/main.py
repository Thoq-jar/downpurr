#!/usr/bin/env python3

import os
import sys


def load_template():
    return """#!/bin/sh
WEBKIT_DISABLE_COMPOSITING_MODE=1 python3 - <<END
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.0")
from gi.repository import Gtk, WebKit2
class Browser:
    def __init__(self):
        self.window = Gtk.Window(title="%%{NAME}%%")
        self.window.set_default_size(1280, 720)
        self.webview = WebKit2.WebView()
        self.webview.load_uri("%%{SITE}%%")
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)
        self.window.add(scrolled_window)
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()
Browser()
Gtk.main()
END"""


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: downpurr <website>")
        exit(1)

    website = args[1]
    if not website.startswith("http"):
        print("Invalid website, must start with 'http://' or 'https://'!")
        exit(1)

    name = website.split("/")[-1].split(".")[0].capitalize()

    print(f"Generating app for: {name}")

    raw_template = load_template()

    template = (raw_template.replace("%%{NAME}%%", name).replace("%%{SITE}%%", website))

    with open(name, "w") as f:
        f.write(template)
        f.close()

    os.system(f"chmod +x {name}")
    print(f"Generated: {name} app in current directory!")


if __name__ == '__main__':
    main()
