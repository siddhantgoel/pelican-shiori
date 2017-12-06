# pelican-shiori

`pelican-shiori` is a port of the [Shiori] theme (originally built for Jekyll
by [Elle Kasai]) to [Pelican].

## Installation

```sh
pip install pelican-shiori
```

## Requirements

- [assets] plugin for Pelican
- working [SASS] compiler

## Usage

In your pelican `settings.py`, set the `THEME` and `ASSET_CONFIG` variables like
the following -

```python
import pelican_shiori

THEME = pelican_shiori.path()
ASSET_CONFIG = pelican_shiori.asset_config()
```

## Configuration

The following configuration variables are supported.

- `SHIORI_THEME`: which color scheme to use (one of `dark`, `turquoise`,
  `green`, `blue`, `purple`, `orange`, `red`)
- `SHIORI_HIDE_SIDEBAR`: whether or not to show the sidebar
- `SHIORI_INDEX_ARTICLES_COUNT`: number of articles to show on the index page

## Color Schemes

This theme is available in multiple color schemes (based on [Flat UI Colors]).
The default value for the color scheme is set to (surprise) `default`. To change
it to one of the supported values, adjust the `SHIORI_THEME` and `ASSET_CONFIG`
variables as follows -

```python
SHIORI_THEME = 'blue'
ASSET_CONFIG = pelican_shiori.asset_config(SHIORI_THEME)
```

Please make sure that the argument given to `pelican_shiori.asset_config` is the
same as `SHIORI_THEME`. [Bad things] may happen otherwise.

[assets]: https://github.com/getpelican/pelican-plugins/tree/master/assets
[Bad things]: https://www.xkcd.com/292
[Elle Kasai]: http://ellekasai.com
[Flat UI Colors]: http://flatuicolors.com
[Pelican]: https://blog.getpelican.com
[SASS]: http://sass-lang.com/install
[Shiori]: https://ellekasai.github.io/shiori
