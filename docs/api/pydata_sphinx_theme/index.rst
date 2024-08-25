pydata_sphinx_theme
===================

.. py:module:: pydata_sphinx_theme

.. autoapi-nested-parse::

   
   Bootstrap-based sphinx theme from the PyData community.
















   ..
       !! processed by numpydoc !!


Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/pydata_sphinx_theme/edit_this_page/index
   /api/pydata_sphinx_theme/logo/index
   /api/pydata_sphinx_theme/pygments/index
   /api/pydata_sphinx_theme/short_link/index
   /api/pydata_sphinx_theme/toctree/index
   /api/pydata_sphinx_theme/translator/index
   /api/pydata_sphinx_theme/utils/index


Attributes
----------

.. autoapisummary::

   pydata_sphinx_theme.__version__


Functions
---------

.. autoapisummary::

   pydata_sphinx_theme._fix_canonical_url
   pydata_sphinx_theme.setup
   pydata_sphinx_theme.update_and_remove_templates
   pydata_sphinx_theme.update_config


Package Contents
----------------

.. py:function:: _fix_canonical_url(app, pagename, templatename, context, doctree)

   
   Fix the canonical URL when using the dirhtml builder.

   Sphinx builds a canonical URL if ``html_baseurl`` config is set. However,
   it builds a URL ending with ".html" when using the dirhtml builder, which is
   incorrect. Detect this and generate the correct URL for each page.

   Workaround for https://github.com/sphinx-doc/sphinx/issues/9730; can be removed
   when that is fixed, released, and available in our minimum supported Sphinx version.















   ..
       !! processed by numpydoc !!

.. py:function:: setup(app)

   
   Setup the Sphinx application.
















   ..
       !! processed by numpydoc !!

.. py:function:: update_and_remove_templates(app, pagename, templatename, context, doctree)

   
   Update template names and assets for page build.
















   ..
       !! processed by numpydoc !!

.. py:function:: update_config(app)

   
   Update config with new default values and handle deprecated keys.
















   ..
       !! processed by numpydoc !!

.. py:data:: __version__
   :value: '0.15.4dev0'


