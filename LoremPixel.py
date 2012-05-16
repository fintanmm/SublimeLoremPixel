import sublime
import sublime_plugin

# TODO: Display command
# TODO: Display list of sizes
# TODO: Custom sizes
# TODO: Categories eg sports, animals
# TODO: Autocomplete

# http://lorempixel.com/


class LoremPixelCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
