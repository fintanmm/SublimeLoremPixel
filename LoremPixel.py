import sublime
import sublime_plugin

# TODO: Custom sizes
# TODO: Categories
# TODO: Grey photos
# TODO: Dummy text
# TODO: Validate custom_sizes
# TODO: Disable categories
# TODO: Support for less and sass


class LoremPixel(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        syntax = view.settings().get('syntax')
        settings = sublime.load_settings("LoremPixel.sublime-settings")
        pixel_url = 'http://lorempixel.com/'
        sizes = settings.get("custom_sizes")
        categories = settings.get("categories")
        sel = view.sel()[0].a
        attr = view.substr(sublime.Region(sel - 5, sel))
        urls = []

        for x in (u'html', u'css', u'less', u'sass'):
            if syntax.lower().count(x):
                if attr.count('src=') or attr.count('url('):
                    urls = [(pixel_url + s, pixel_url + s) for s in sizes]
            return urls
        return
