import sublime
import sublime_plugin
import re

# TODO: Grey photos
# TODO: Dummy text
# TODO: Support for less and sass
# FIXME: Don't show categories when the sizes are not present

lp = re.compile('lorempixel\.com(\/)|(\/g/)\[\d]*\/[\d]*/')


class LoremPixel(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        syntax = view.settings().get('syntax')
        settings = sublime.load_settings("LoremPixel.sublime-settings")
        sizes = settings.get("custom_sizes")
        categories = []

        if settings.get("include_categories"):
            categories = settings.get("categories")

        def posistion(pos):  # TODO: Need a better way to do this
            sel = view.sel()[0].a
            return view.substr(sublime.Region(sel - pos, sel))

        pixel_url = 'http://lorempixel.com/'
        defaults = [(pixel_url, pixel_url)]
        urls = []

        if settings.get("include_grey"):
            defaults.append((pixel_url + 'g/', pixel_url + 'g/'))

        attr = posistion(5)
        lp_attr = posistion(50)

        for x in (u'html', u'css', u'less', u'sass'):
            if syntax.lower().find(x):
                if attr.find('src=') != -1 or attr.find('url(') != -1:
                    urls = defaults + [(pixel_url + s, pixel_url + s) for s in sizes]
                if lp.search(lp_attr):
                    urls = [(c, c) for c in categories]
            return urls
        return
