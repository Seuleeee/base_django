import os
import traceback

from api.constants.types import (
    FileTypesEnum,
    ImageFileTypesEnum,
    DocumentFileTypesEnum,
    VideoFileTypesEnum,
)


def get_file_extension(file_name: str) -> str:
    """
    file name을 받으면, 확장자를 return 하는 메서드
    """
    try:
        extension = os.path.splitext(file_name)[1].lower()[1:]
        return extension
    except Exception as e:
        # Handle the exception here, for example:
        print(traceback.format_exc())
        return ''


def get_file_type(file_name: str) -> str:
    """
    File 확장자를 활용해 Type을 지정하는 method
    """
    extension: str = get_file_extension(file_name)
    if extension in ImageFileTypesEnum.get_all_values():
        return FileTypesEnum.IMAGE

    elif extension in DocumentFileTypesEnum.get_all_values():
        return FileTypesEnum.DOCUMENT

    elif extension in VideoFileTypesEnum.get_all_values():
        return FileTypesEnum.VIDEO

    else:
        raise ValueError("허용 하지 않는 파일 확장자 입니다.")


