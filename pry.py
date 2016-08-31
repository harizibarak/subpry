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
      region = self.findPryRegion(view)
      while not region.empty():
        view.erase(edit, view.full_line(region))
        region = self.findPryRegion(view)
      if view.file_name() != None:
        view.run_command('save')

  def findPryRegion(self, view):
    return view.find(bindingPryStr, 0) or view.find(requirePryStr, 0)