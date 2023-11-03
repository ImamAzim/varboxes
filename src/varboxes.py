#!/usr/bin/env python


import os
import json


import xdg


class VarBox(object):

    """
    allow to store and load variables between session.
    the variables are saved on the disk everytime they are modified
    """

    def __init__(self, project_name=None, app_name=None):
        """check if folder exist else create.
        Load the stored attributes (variables)

        :project_name: str or if None then takes name of virtualenv or varboxes
        :app_name: str or if None then name is 0
        :name:

        """

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

        file_path = os.path.join(directory, f'varbox_{app_name}.json')
        super().__setattr__('_file_path', file_path)

        self._load_last_parameters()

    def __setattr__(self, name: str, value: any):
        """TODO: replace the setattribute. In addition to usual function,
        it store the attribute and its value in a json file.

        :name: attribute name(variable)
        :value: any json serializable value
        :returns: None

        """
        super().__setattr__(name, value)
        pass

        try:
            with open(self._file_path, 'w') as myfile:
                json.dump(self.__dict__, myfile)
        except IOError:
            print('could not access or find last parameter file')
        except TypeError:
            print(
                    'could not save parameters. typeerror.'
                    'probably because one object is not json serializable')

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
                super().__setattr__(key, el)


if __name__ == '__main__':
    pass
