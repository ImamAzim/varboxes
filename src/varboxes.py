#!/usr/bin/env python


import os


import xdg


class VarBox(object):

    """
    allow to store and load variables between session.
    the variables are automaticelly saved on the disk everytime they are modified
    """

    def __init__(self, project_name: str, app_name: str, **default_variables):
        """create VarBox object, check if folder exist, make properties and load last values

        :default_vars: dict of default values
        :name:

        """
        self._default_variables = default_variables

        directory = os.path.join(xdg.xdg_data_home(), APP_NAME)
        if not os.path.exists(directory):
            os.makedirs(directory)
        self._file_path = os.path.join(directory, name + '.json')

        def make_prop(name):
            def getter(self):
                return self._parameters[name]

            def setter(self, value):
                self._parameters[name] = value
                self._save_current_parameters()

            return property(getter, setter)

        self._parameters = dict()
        for name, value in default_parameters.items():
            self._parameters[name] = value
            setattr(Parameters,  name, make_prop(name))

        self._load_last_parameters()

    def _save_current_parameters(self):
        """save current parameters in a json file


        """
        try:
            with open(self._file_path, 'w') as myfile:
                json.dump(self._parameters, myfile)
        except IOError:
            print('could not access or find last parameter file')
        except TypeError:
            print(
                    'could not save parameters. TypeError.'
                    'probably because one object is not Json serializable')

    def _load_last_parameters(self):
        """load parameter from last saved file


        """
        try:
            with open(self._file_path, 'r') as myfile:
                last_parameters = json.load(myfile)
        except EOFError:
            print('last parameter file is probably empty..')
        except IOError:
            print('could not access or find last parameter file')
        except json.decoder.JSONDecodeError:
            print('json file is probably corrupted')
        else:
            for key, el in last_parameters.items():
                if key in self._parameters:
                    self._parameters[key] = el

    def restore_default(self):
        """TODO: restore default values


        """
        for name in self._parameters:
            setattr(self, name, self._default_variables[name])

    def get_keys(self):
        """helper to get list of all parameters
        :returns: keys obj of all parameter names

        """
        return self._parameters.keys()

    def to_dict(self):
        """convert to a dictionnary
        :returns: dict

        """
        current_parameters = dict()
        for key in self._default_variables:
            current_parameters[key] = getattr(self, key)
        return current_parameters


if __name__ == '__main__':
    pass
