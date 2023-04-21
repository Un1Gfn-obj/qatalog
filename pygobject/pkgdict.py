#!/dev/null

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk
from emoji import emojize as j
# import random
import pyalpm

DBS = None


def alpminit():

    global DBS
    assert 6 <= len(pyalpm.alpmversion())
    # assert "13.0.1" == pyalpm.alpmversion()
    h = pyalpm.Handle("/", "/var/lib/pacman")
    for i in ["core", "extra", "community", "multilib"]:
        h.register_syncdb(i, pyalpm.SIG_DATABASE_MARGINAL_OK)  # https://www.gnupg.org/gph/en/manual/x334.html#AEN345
    DBS = h.get_syncdbs()


def alpmlookup(pkgname):

    global DBS
    for d in DBS:
        if p := d.get_pkg(pkgname):  # walrus
            return p.desc
            # return "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    return "< package not found >"


class PkgdictWindow(Gtk.Window):

    def __init__(self, parent):

        # random.seed(a=None)

        super().__init__(title="pkgdict")
        self.set_border_width(10)
        self.parent = parent

        # self.connect("destroy", Gtk.main_quit)
        self.connect("destroy", lambda _: self.parent.show())

        # /usr/include/gtk-3.0/gdk/gdkkeysyms.h
        # print(Gdk.keyval_name(ev.keyval))
        self.connect('key-press-event', lambda _, ev: self.destroy() if Gdk.KEY_Escape == ev.keyval else None)  # self.emit('destroy')

        # self.b = Gtk.Button.new_with_label(j(":magnifying_glass_tilted_right: :magnifying_glass_tilted_left:"))
        self.b = Gtk.Button.new_with_label(j(":magnifying_glass_tilted_right:"))
        alpminit()
        self.b.connect('clicked', self.lookup)

        # https://stackoverflow.com/questions/1655372/
        # pacman -Qq | wc -L
        # pacman -Qq | awk '{print length, $0}' | sort -n
        self.e = Gtk.Entry()
        self.e.set_max_length(64)
        # self.e.set_text("I want to look up ...")
        self.e.connect('key-press-event', lambda _, ev: self.b.emit('clicked') if Gdk.KEY_Return == ev.keyval else None)  # self.b.emit('activate')

        self.v = Gtk.TextView()
        self.v.set_editable(False)  # self.v.set_property("editable", False)
        self.v.set_cursor_visible(False)
        self.v.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        # s = Gtk.ScrolledWindow()
        # s.add(self.v)

        # https://docs.gtk.org/gtk3/method.Box.pack_start.html
        inner = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        inner.pack_start(self.b, False, False, 0)
        inner.pack_start(self.e, True, True, 0)

        outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        outer.pack_start(inner, False, False, 0)
        outer.pack_start(self.v, True, True, 0)
        self.add(outer)

        self.b.set_focus_on_click(False)
        self.b.set_can_focus(False)
        self.show_all()
        # self.e.emit("grab-focus")
        self.e.grab_focus()

    def lookup(self, _):

        # self.v.textbuffer.set_text(str(random.randint(0,255)))
        # self.v.buffer.set_text(str(random.randint(0,255)))
        # self.v.get_textbuffer().set_text(str(random.randint(0,255)))
        # self.v.get_buffer().set_text(str(random.randint(0,255)))
        self.v.get_buffer().set_text(alpmlookup(self.e.get_text()))


# if __name__ == "__main__":

#     alpminit()
#     alpmlookup("0ad-data")
