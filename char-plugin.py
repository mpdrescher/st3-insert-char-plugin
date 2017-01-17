import sublime
import sublime_plugin

class InsSmallerThenCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			self.view.insert(edit, region.end(), "<")

class InsGreaterThenCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			self.view.insert(edit, region.end(), ">")

class InsHorBarCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			self.view.insert(edit, region.end(), "|")