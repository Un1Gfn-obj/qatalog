#!/bin/python3

# https://pygobject.readthedocs.io/en/latest/guide/api/properties.html

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import GLib
from gi.repository import Gtk
import inspect
import pprint

print(ps := Gtk.MessageDialog.list_properties(),"\n")

# help(ps[0])
print(inspect.getmembers(ps[0]),"\n")

d = dict()
for p in ps:
    assert p.blurb == p.__doc__
    d[p.name] = p.blurb
pprint.pprint(d)

