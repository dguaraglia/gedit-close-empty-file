Autoclose empty file
======================

Something that has always nagged me about gedit is the fact that the empty file that gets created
when you first start gedit will sometimes get replaced by the first file you open, some other
times remain there, wasting valuable tabbar space. Apparently, this happens because some plugins
(like many of the myriad 'quick open file' plugins) don't know how to reuse that empty file.

This plugin tries to fix that.

Installation
------------

Installation is very simple. Just copy the autoclose_empty_file.* files to your
gedit plugins directory (usually found at `~/.gnome2/gedit/plugins`):

    git clone http://github.com/dguaraglia/gedit-autoclose-empty-file
    cd gedit-autoclose-empty-file; cp autoclose_empty_file.* ~/.gnome2/gedit/plugins

then enable the 'Automatically close empty files' plugin in gedit by going to *Edit->Preferences->Plugins*.

