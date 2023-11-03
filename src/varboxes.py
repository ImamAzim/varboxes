#!/usr/bin/env python


import os


import xdg


class VarBox(object):

    """
    allow to store and load variables between session.
    the variables are automaticelly saved on the disk everytime they are modified
    """

    def __init__(self, project_name=None, app_name=None):
        """check if folder exist else create. load the stored attributes (variables)

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

        file_path = os.path.join(directory, f'varbox_{app_name}.json'
        super().__setattr__('_file_path', file_path)

        self._load_last_parameters()

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


if __name__ == '__main__':
    pass
