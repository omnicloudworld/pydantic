# pylint: disable=missing-docstring

from __future__ import annotations

import json
from os.path import join
from pathlib import Path

import yaml

from ...tools.file import SaveLoad
from ...tools.json import StringEncoder
from ...tools.e import UnknowType


class File(SaveLoad):
    '''
    Saving/loading data to/from local file with some additional useful feutures such as:

    - making parent directories
    - extended JSON encoder
    '''

    @staticmethod
    def _check_file(path: str) -> None:
        '''
        Method checks if a file exists and extension is allowed.

        Args:
            path: The full path to the file.
        '''

        if not Path(path).is_file():
            raise ValueError(f'Provided path {path} is not a file!')

        SaveLoad._get_sufix(path, only_verify=True)

    def save_local(
        self,
        fullname: str,
        encoding: str = 'utf8',
        ensure_ascii: bool = True,
        exclude_none: bool = False,
        exclude_unset: bool = True
    ):
        '''
        Method saves the data to a local JSON/YAML/AVRO file.

        Before seving the method makes a full filesystem hyerarchy, so you can any path to it.
        Additionly method has extended JSON encoder which deserialize IPv4Address, IPv6Address,
            Enim objects and datetime (in format Y-m-d H:M:S acceptable by BigQuery).

        Args:

            fullname: Full pathname with extension.

            encoding: File encodding.

            ensure_ascii: Keep or not non-ASCII characters.

            exclude_none: Keep or pass emplty values. If True, file will be contains "NaN" values.

            exclude_unset: Write or ignore default values. If False default values won't be written.

        Raises:
            NotImplementedError: AVRO does not support now!
            UnknowType: Unknow file type!
        '''

        parent_path, file_name, file_ext = self._prepare_path(fullname, make_parent=True)
        file_format = self._get_format(fullname)

        if file_format == 'json':
            with open(join(parent_path, f'{file_name}.{file_ext}'), 'w', encoding=encoding) as dump_file:
                dump_file.write(
                    json.dumps(
                        self.dict(exclude_unset=exclude_unset, exclude_none=exclude_none),
                        ensure_ascii=ensure_ascii,
                        cls=StringEncoder
                    )
                )

        elif file_format == 'yaml':
            with open(join(parent_path, f'{file_name}.{file_ext}'), 'w', encoding=encoding) as dump_file:
                yaml.dump(
                    self.dict(exclude_unset=exclude_unset, exclude_none=exclude_none),
                    dump_file,
                    default_flow_style=False
                )

        elif file_format == 'avro':
            # TODO: Implement a procedure for saving avro file to a Local File.
            raise NotImplementedError('avro doesn\'t support now')

        else:
            raise UnknowType(f'{file_name}.{file_ext}')

    @classmethod
    def load_local(cls, fullname: str, encoding: str = 'utf8') -> File:
        '''
        Read JSON/YAML/AVRO file and make class instance.

        Args:

            fullname: Full pathname with extension.

            encoding: File encodding.

        Raises:
            NotImplementedError: AVRO does not support now!
            UnknowType: Unknow file type!

        Returns:
            The instance of skyant.data.entity.file.Local
        '''

        cls._check_file(fullname)
        file_format = cls._get_format(fullname)

        if file_format == 'json':
            return cls.parse_file(fullname, encoding=encoding)

        elif file_format == 'yaml':
            with open(fullname, 'r', encoding=encoding) as src_file:
                return cls.parse_obj(yaml.safe_load(src_file))

        elif file_format == 'avro':
            # TODO: Implement a procedure for loadding avro file from a Local filesystem.
            raise NotImplementedError('avro doesn\'t support now')

        else:
            raise UnknowType(fullname)