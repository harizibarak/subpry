import sublime, sublime_plugin

requirePryStr = "require 'pry'"
bindingPryStr = "binding.pry"

class PryCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, self.view.sel()[0].a, bindingPryStr)
    if self.view.find(requirePryStr, 0).empty():
      self.view.insert(edit, 0, requirePryStr + "\n")

class UnpryCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    views = self.view.window().views()
    for view in views:
      view.run_command('unpry_view')

class UnpryViewCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    region = self.findPryRegion()
    while not region.empty():
      self.view.erase(edit, self.view.full_line(region))
      region = self.findPryRegion()
    if self.view.file_name() != None:
      self.view.run_command('save')

  def findPryRegion(self):
    return self.view.find(bindingPryStr, 0) or self.view.find(requirePryStr, 0)