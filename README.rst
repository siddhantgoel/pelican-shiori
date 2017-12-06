pelican-shiori
==============

:code:`pelican-shiori` is a port of the Shiori_ theme (originally built for
Jekyll by `Elle Kasai`_) to Pelican_.

Installation
------------

.. code-block:: bash

    $ pip install pelican-shiori

Requirements
------------

- assets_ plugin for Pelican
- working SASS_ compiler

Usage
-----

In your pelican :code:`settings.py`, set the :code:`THEME` and
:code:`ASSET_CONFIG` variables like the following -

.. code-block:: python

    import pelican_shiori

    THEME = pelican_shiori.path()
    ASSET_CONFIG = pelican_shiori.asset_config()

Configuration
-------------

The following configuration variables are supported.

- :code:`SHIORI_THEME`: which color scheme to use (one of :code:`dark`,
  :code:`turquoise`, :code:`green`, :code:`blue`, :code:`purple`,
  :code:`orange`, :code:`red`)
- :code:`SHIORI_HIDE_SIDEBAR`: whether or not to show the sidebar
- :code:`SHIORI_INDEX_ARTICLES_COUNT`: number of articles to show on the index page

Color Schemes
-------------

This theme is available in multiple color schemes (based on `Flat UI Colors`_).
The default value for the color scheme is set to (surprise) :code:`default`. To
change it to one of the supported values, adjust the :code:`SHIORI_THEME` and
:code:`ASSET_CONFIG` variables as follows -

.. code-block:: python

    SHIORI_THEME = 'blue'
    ASSET_CONFIG = pelican_shiori.asset_config(SHIORI_THEME)

Please make sure that the argument given to `pelican_shiori.asset_config` is the
same as `SHIORI_THEME`. `Bad things`_ may happen otherwise.

.. _assets: https://github.com/getpelican/pelican-plugins/tree/master/assets
.. _Bad things: https://www.xkcd.com/292
.. _Elle Kasai: http://ellekasai.com
.. _Flat UI Colors: http://flatuicolors.com
.. _Pelican: https://blog.getpelican.com
.. _SASS: http://sass-lang.com/install
.. _Shiori: https://ellekasai.github.io/shiori
