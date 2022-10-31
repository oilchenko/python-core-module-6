import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
XLS_DOCUMENTS = []
XLSX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
PPT_DOCUMENTS = []
PPTX_DOCUMENTS = []
MY_OTHER = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []

REGISTERED_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'XLS': XLS_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'PPT': PPT_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES
}

FOLDERS = []

EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTERED_EXTENSIONS[ext]
                container.append(fullname)
                EXTENSIONS.add(ext)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)
    print(f"Scan function has scanned the folder {folder}")


def parser_info():
    print(f'Images jpeg: {JPEG_IMAGES}', "\n")
    print(f'Images jpg: {JPG_IMAGES}', "\n")
    print(f'Images svg: {SVG_IMAGES}', "\n")
    print(f'Images svg: {SVG_IMAGES}', "\n")

    print(f'Audio mp3: {MP3_AUDIO}', "\n")
    print(f'Audio ogg: {OGG_AUDIO}', "\n")
    print(f'Audio wav: {WAV_AUDIO}', "\n")
    print(f'Audio amr: {AMR_AUDIO}', "\n")

    print(f'Video avi: {AVI_VIDEO}', "\n")
    print(f'Video mp4: {MP4_VIDEO}', "\n")
    print(f'Video mov: {MOV_VIDEO}', "\n")
    print(f'Video mkv: {MKV_VIDEO}', "\n")

    print(f'Documents doc: {DOC_DOCUMENTS}', "\n")
    print(f'Documents docx: {DOCX_DOCUMENTS}', "\n")
    print(f'Documents xls: {XLS_DOCUMENTS}', "\n")
    print(f'Documents xlsx: {XLSX_DOCUMENTS}', "\n")
    print(f'Documents txt: {TXT_DOCUMENTS}', "\n")
    print(f'Documents pdf: {PDF_DOCUMENTS}', "\n")
    print(f'Documents ppt: {PPT_DOCUMENTS}', "\n")
    print(f'Documents pptx: {PPTX_DOCUMENTS}', "\n")

    print(f'zip archives: {ZIP_ARCHIVES}', "\n")
    print(f'gz archives: {GZ_ARCHIVES}', "\n")
    print(f'tar archives: {TAR_ARCHIVES}', "\n")

    print(f'My other: {MY_OTHER}', "\n")

    print(f'Types of files in scanned folder: {EXTENSIONS}', "\n")
    print(f'Unknown files of types: {UNKNOWN}', "\n")

    print(f"Folders list: {FOLDERS[::-1]}")