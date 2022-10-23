# pylint: disable=missing-docstring

from __future__ import annotations

import json
from enum import Enum

import yaml
from google.cloud import storage as gcs

from .._tools.file import SaveLoad
from .._tools.json import StringEncoder
from .._tools.e import UnknowType


class StorageClass(Enum):
    STANDARD = 'STANDARD'
    NEARLINE = 'NEARLINE'
    COLDLINE = 'COLDLINE'
    ARCHIVE = 'ARCHIVE'


class Storage(SaveLoad):
    '''
    Saving & loading files to/from [Google Cloud Storage](https://cloud.google.com/storage).
    '''

    @classmethod
    @property
    def GCSClass(cls) -> StorageClass:  # pylint: disable=invalid-name
        '''
        Enumerator of posible Google Cloud Storage "Storage Classes", such as "standard",
            "archive", etc.

        [Origin documentation](https://cloud.google.com/storage/docs/storage-classes)
        '''

        return StorageClass

    def save_gcs(
        self,
        fullname: str,
        storage_class: StorageClass = StorageClass.STANDARD,
        encoding: str = 'utf8',
        ensure_ascii: bool = True,
        exclude_none: bool = False,
        exclude_unset: bool = True
    ) -> None:
        '''
        Save data to Google Cloud Storage. This method supports:
        - json
        - yaml

        Args:

            fullname: Full file name include bucket name & extension.

            storage_class: Google Storage Class to assign to file.

            encoding: File encodding.

            ensure_ascii: Keep or not non-ASCII characters.

            exclude_none: Keep or pass emplty values. If True, file will be contains "NaN" values.

            exclude_unset: Write or ignore default values. If False default values won't be written.

        Raises:
            NotImplementedError: AVRO does not support now!
            UnknowType: Unknow file type!
        '''

        bucket_name, blob_name = self._prepare_gcs_uri(fullname)
        file_format = self._get_format(fullname)

        bucket = gcs.Client().get_bucket(bucket_name)

        if file_format == 'json':

            data = json.dumps(
                self.dict(exclude_unset=exclude_unset, exclude_none=exclude_none),
                ensure_ascii=ensure_ascii,
                cls=StringEncoder,
                encoding=encoding
            )
            content_type = 'application/json'

        elif file_format == 'yaml':
            data = yaml.dump(
                self.dict(exclude_unset=exclude_unset, exclude_none=exclude_none),
                default_flow_style=False,
                encoding=encoding,
                allow_unicode=not ensure_ascii
            )
            content_type = 'application/yaml'

        elif file_format == 'avro':
            # TODO: Implement a procedure for saving avro file to Google Cloud Storage.
            raise NotImplementedError('AVRO doesn\'t support now!')

        else:
            raise UnknowType(blob_name)

        blob = bucket.blob(blob_name)
        blob.upload_from_string(data, content_type=content_type)
        blob.update_storage_class(storage_class.value)

    @classmethod
    def load_gcs(cls, fullname: str, encoding: str = 'utf8') -> Storage:
        '''
        Load the data from Google Cloud Storage. Function reads JSON & YAML files.

        Args:

            fullname: Full file name include bucket name & extension.

            encoding: File encodding.

        Raises:
            NotImplementedError: AVRO does not support now!
            UnknowType: Unknow file type!

        Returns:
            The instance of this class.
        '''

        bucket_name, blob_name = cls._prepare_gcs_uri(fullname)
        file_format = cls._get_format(fullname)

        bucket = gcs.Client().get_bucket(bucket_name)
        blob = bucket.blob(blob_name)

        if file_format == 'json':
            data = json.loads(blob.download_as_text(encoding=encoding))

        elif file_format == 'yaml':
            data = yaml.safe_load(blob.download_as_text(encoding=encoding))

        elif file_format == 'avro':
            # TODO: Implement a procedure for loadding avro file from Google Cloud Storage.
            raise NotImplementedError('AVRO doesn\'t support now!')

        else:
            raise UnknowType(blob_name)

        cls._validate_schemas(data)

        return cls.parse_obj(data)
