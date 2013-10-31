import gedit
import gtksourceview2

class TabWatch:
    """ Monitor the tabs in gedit to find out when new tabs get opened """

    def __init__(self, window):
        self.geditwindow = window
        self._signal = self.geditwindow.connect("tab_added", self.__tab_added)
        

    def __tab_added(self, window, tab):
        """ Once a tab is created find the first *other* tab with an emtpy and 
            untouched file and kill it"""

        if (window.get_state() != gedit.WINDOW_STATE_NORMAL):
            return

        # find the empty tab
        from pprint import pprint
        for document in self.geditwindow.get_documents():
            if document.is_untitled() and document.is_untouched():
                empty_tab = gedit.tab_get_from_document(document)
                if not (empty_tab is tab):
                    # kill it
                    self.geditwindow.close_tab(empty_tab)

                    # once we've closed the annoying empty document, there's no use
                    # in handling the event anymore
                    self.geditwindow.disconnect(self._signal)
                    self._signal = None
                    break



class AutoCloseEmptyFilePlugin(gedit.Plugin):
    def __init__(self):
        gedit.Plugin.__init__(self)
        self._watchers = {}

    def activate(self, window):
        # add a tab watcher for this window
        self._watchers[window] = TabWatch(window)

    def deactivate(self, window):
        del self._watchers[window]

    def update_ui(self, window):
        pass
