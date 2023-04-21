#!/bin/python3

# https://pygobject.readthedocs.io/en/latest/index.html
# https://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html
# https://lazka.github.io/pgi-docs/Gtk-3.0/
# https://docs.gtk.org/gtk3/#classes

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gdk
from emoji import emojize as j

BODY = """\
kaccounts-integration\
"""


def left(b):

    li = b.get_children()
    assert len(li) == 1
    lb = li[0]
    assert type(lb) == Gtk.Label
    assert lb.get_halign() == Gtk.Align.FILL
    lb.set_halign(Gtk.Align.START)
    return b


class MainWindow(Gtk.Window):

    def __init__(self):

        super().__init__(title="catalog")
        self.connect("destroy", Gtk.main_quit)
        self.connect('key-press-event', lambda _, ev: Gtk.main_quit() if Gdk.KEY_Escape == ev.keyval else None)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        left(pkgdict := Gtk.Button.new_with_label(j(":books: pkgdict")))
        pkgdict.connect("clicked", self.pkgdict)
        vbox.pack_start(pkgdict, False, False, 0)

        left(idea := Gtk.Button.new_with_label(j(":light_bulb:")))
        idea.connect("clicked", self.idea)
        vbox.pack_start(idea, False, False, 0)

        left(q := Gtk.Button.new_with_label(j(":cross_mark: quit")))
        q.connect("clicked", Gtk.main_quit)
        vbox.pack_start(q, False, False, 0)

        self.add(vbox)

        self.show_all()
        pkgdict.grab_focus()

    def pkgdict(self, _):
        from pkgdict import PkgdictWindow
        self.hide()
        subw = PkgdictWindow(parent=self)

    def idea(self, _):
        dialog = Gtk.MessageDialog(
            # ~/pygobject/property.py
            # transient_for=self,
            # https://docs.gtk.org/gtk3/ctor.MessageDialog.new.html
            # flags=0,
            # https://docs.gtk.org/gtk3/class.MessageDialog.html#properties
            buttons=Gtk.ButtonsType.CLOSE,
            message_type=Gtk.MessageType.INFO,
            secondary_text=BODY,
            secondary_use_markup=False,
            text=j(":light_bulb:"),
            use_markup=False,
        )
        dialog.run()
        dialog.destroy()


def main():

    GLib.set_prgname("floating")
    GLib.set_application_name("lsjhdpm8")
    # w = MainWindow()
    MainWindow()
    Gtk.main()


if __name__ == "__main__":
    main()
