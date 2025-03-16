#!/usr/bin/env python3

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.0")
# noinspection PyUnresolvedReferences
from gi.repository import Gtk, WebKit2


class Browser:
    def __init__(self):
        self.window = Gtk.Window(title="%%{NAME}%%")
        self.window.set_default_size(800, 600)
        self.webview = WebKit2.WebView()
        self.webview.load_uri("%%{SITE}%%")

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)
        self.window.add(scrolled_window)

        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()


Browser()
Gtk.main()
