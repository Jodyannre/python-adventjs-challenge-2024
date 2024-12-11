import re
def main():
    print(decode_filename("465465465465_magic_wand-blueprint.jpg.grichbackup"))

def decode_filename(filename: str) -> str:
    return filename[filename.find("_")+1:filename.rfind(".")]


"""
def decode_filename(filename: str) -> str:
    name = filename.find("_")
    ext = filename.rfind(".")
    return filename[name+1:ext] if name > 0 else ""
"""

"""
def decode_filename(filename: str) -> str:
    x = re.findall("_([a-zA-Z|\\-|_]+\\.[a-z]+)", filename)
    return x[0][1:] if len(x) > 0 else ""
"""


if __name__ == '__main__':
    main()