from pathlib import Path


def asset_config(theme):
    return (
        ('JINJA2_CONTEXT', {'theme': theme}),
    )


def path():
    """https://github.com/getpelican/pelican/issues/1564#issuecomment-282136049
    """
    return str(Path(__file__).parent)
