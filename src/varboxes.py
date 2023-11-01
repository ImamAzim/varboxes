#!/usr/bin/env python


import os


import xdg


class VarBox(object):

    """
    allow to store and load variables between session.
    the variables are automaticelly saved on the disk everytime they are modified
    """

    def __init__(self, project_name=None, app_name=None, **default_variables):
        """check if folder exist, make properties and load last values

        :project_name: str or if None then takes name of virtualenv or varboxes
        :app_name: str or if None then name is 0
        :default_varables: dict of default values
        :name:

        """
        self._default_variables = default_variables

        if project_name is None:
            venv_path = os.environ.get('VIRTUAL_ENV')
            try:
                project_name = os.path.basename(venv_path)
            except TypeError:
                project_name = 'varboxes'

        if app_name is None:
            app_name = '0'

        directory = os.path.join(xdg.xdg_data_home(), project_name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        self._file_path = os.path.join(directory, f'varbox_{app_name}.json')


        def make_prop(name):
            def getter(self):
                return self._variables[name]

            def setter(self, value):
                self._variables[name] = value
                self._save_current_parameters()

            return property(getter, setter)

        self._variables = dict()
        for name, value in default_variables.items():
            self._variables[name] = value
            setattr(VarBox,  name, make_prop(name))

        # self._load_last_parameters()

    # def _save_current_parameters(self):
        # """save current parameters in a json file


        # """
        # try:
            # with open(self._file_path, 'w') as myfile:
                # json.dump(self._variables, myfile)
        # except IOError:
            # print('could not access or find last parameter file')
        # except TypeError:
            # print(
                    # 'could not save parameters. TypeError.'
                    # 'probably because one object is not Json serializable')

    # def _load_last_parameters(self):
        # """load parameter from last saved file


        # """
        # try:
            # with open(self._file_path, 'r') as myfile:
                # last_parameters = json.load(myfile)
        # except EOFError:
            # print('last parameter file is probably empty..')
        # except IOError:
            # print('could not access or find last parameter file')
        # except json.decoder.JSONDecodeError:
            # print('json file is probably corrupted')
        # else:
            # for key, el in last_parameters.items():
                # if key in self._variables:
                    # self._variables[key] = el

    # def restore_default(self):
        # """TODO: restore default values


        # """
        # for name in self._variables:
            # setattr(self, name, self._default_variables[name])

    # def get_keys(self):
        # """helper to get list of all parameters
        # :returns: keys obj of all parameter names

        # """
        # return self._variables.keys()

    # def to_dict(self):
        # """convert to a dictionnary
        # :returns: dict

        # """
        # current_parameters = dict()
        # for key in self._default_variables:
            # current_parameters[key] = getattr(self, key)
        # return current_parameters


if __name__ == '__main__':
    pass
