from dialogs import Gtk, GdkPixbuf, g


class Search(Gtk.Dialog):

    def __init__(self, is_replace):
        Gtk.Dialog.__init__(self, g("Search"), None,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_FIND, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        box = self.get_content_area()

        label = Gtk.Label(g("Insert text you want to search for:"))
        box.add(label)

        self.entry = Gtk.Entry()
        box.add(self.entry)

        if is_replace:
            label1 = Gtk.Label(g("Insert text you want to replace with:"))
            box.add(label1)

            self.replace = Gtk.Entry()
            box.add(self.replace)

        self.show_all()