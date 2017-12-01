from pathlib import Path


# https://github.com/getpelican/pelican/issues/1564#issuecomment-282136049
def get_path():
    return str(Path(__file__).parent)
