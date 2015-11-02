import sublime
import sublime_plugin
from translate import Translator

translator = Translator(to_lang="vi")

class CheckUrlsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
    	view = self.view
        sel = view.sel()
        region1 = sel[0]
        selectionText = view.substr(region1)
        # print(selectionText)
        # trans = _trans.translate(selectionText, 'vi')
        trans = translator.translate(selectionText)
        sublime.message_dialog(trans)
