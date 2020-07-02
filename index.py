import sublime
import sublime_plugin
from .pinyin import translate

# print(dir(pinyin.pinyin.__name__))
class PinyinFromSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            print('region')
            if not region.empty():
                text = self.view.substr(region)
                print(text)
                pinyinStr = translate.get(text, format="strip", delimiter="")
                print(pinyinStr)
                if pinyinStr is not None:
                    self.view.replace(edit, region, pinyinStr)
class PinyinFromSelectionUnderlineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            print('region')
            if not region.empty():
                text = self.view.substr(region)
                print(text)
                pinyinStr = translate.get(text, format="strip", delimiter="_")
                print(pinyinStr)
                if pinyinStr is not None:
                    self.view.replace(edit, region, pinyinStr)

