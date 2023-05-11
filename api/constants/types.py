from api.constants.base import BaseEnum


class FileTypesEnum(str, BaseEnum):
    images: str = "image"
    text: str = "text"
    video: str = "video"
