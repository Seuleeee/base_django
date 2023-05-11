from api.constants.base import BaseEnum


class FileTypesEnum(str, BaseEnum):
    IMAGE: str = "image"
    DOCUMENT: str = "document"
    VIDEO: str = "video"


class ImageFileTypesEnum(str, BaseEnum):
    JPG: str = "jpg"
    JPEG: str = "jpeg"
    PNG: str = "png"
    GIF: str = "gif"
    BMP: str = "bmp"


class DocumentFileTypesEnum(str, BaseEnum):
    TXT: str = "txt"
    DOC: str = "doc"
    DOCX: str = "docx"
    PPT: str = "ppt"
    PPTX: str = "pptx"
    PDF: str = "pdf"


class VideoFileTypesEnum(str, BaseEnum):
    MP4: str = "mp4"
    AVI: str = "avi"
    MOV: str = "mov"
    WMV: str = "wmv"
