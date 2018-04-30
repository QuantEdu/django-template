from .. import commands

def info():
   message = ''
   for c in commands.command_list:
        message += c.keys[0] + ' - ' + c.description + '\n'
   return message, ''

info_command = commands.Command()

info_command.keys = ['помощь', 'помоги', 'help']
info_command.desciption = 'Покажу список команд'
info_command.process = info