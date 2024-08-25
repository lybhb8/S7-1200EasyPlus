pydata_sphinx_theme.utils
=========================

.. py:module:: pydata_sphinx_theme.utils

.. autoapi-nested-parse::

   General helpers for the management of config parameters.

   ..
       !! processed by numpydoc !!


Attributes
----------

.. autoapisummary::

   pydata_sphinx_theme.utils.SPHINX_LOGGER


Functions
---------

.. autoapisummary::

   pydata_sphinx_theme.utils._get_matching_sidebar_items
   pydata_sphinx_theme.utils._has_wildcard
   pydata_sphinx_theme.utils._update_and_remove_templates
   pydata_sphinx_theme.utils.config_provided_by_user
   pydata_sphinx_theme.utils.escape_ansi
   pydata_sphinx_theme.utils.get_theme_options_dict
   pydata_sphinx_theme.utils.maybe_warn
   pydata_sphinx_theme.utils.set_secondary_sidebar_items
   pydata_sphinx_theme.utils.traverse_or_findall


Module Contents
---------------

.. py:function:: _get_matching_sidebar_items(pagename, sidebars)

   
   Get the matching sidebar templates to render for the given pagename.

   If a page matches more than one pattern, a warning is emitted, and the templates for the
   last matching pattern are used.

   This function was adapted from sphinx.builders.html.StandaloneHTMLBuilder.add_sidebars.















   ..
       !! processed by numpydoc !!

.. py:function:: _has_wildcard(pattern)

   
   Check whether the pattern contains a wildcard.

   Taken from sphinx.builders.StandaloneHTMLBuilder.add_sidebars.















   ..
       !! processed by numpydoc !!

.. py:function:: _update_and_remove_templates(app, context, templates, section, templates_skip_empty_check = None)

   
   Update templates to include html suffix if needed; remove templates which render empty.

   :param app: Sphinx application passed to the html page context
   :param context: The html page context; dictionary of values passed to the templating engine
   :param templates: A list of template names, or a string of comma separated template names
   :param section: Name of the template section where the templates are to be rendered. Valid
                   section names include any of the ``sphinx`` or ``html_theme_options`` that take templates
                   or lists of templates as arguments, for example: ``theme_navbar_start``,
                   ``theme_primary_sidebar_end``, ``theme_secondary_sidebar_items``, ``sidebars``, etc. For
                   a complete list of valid section names, see the source for
                   :py:func:`pydata_sphinx_theme.update_and_remove_templates` and
                   :py:func:`pydata_sphinx_theme.utils.set_secondary_sidebar_items`, both of which call
                   this function.
   :param templates_skip_empty_check: Names of any templates which should never be removed from the list
                                      of filtered templates returned by this function. These templates aren't checked if they
                                      render empty, which can save time if the template is slow to render.

   :returns: A list of template names (including '.html' suffix) to render into the section















   ..
       !! processed by numpydoc !!

.. py:function:: config_provided_by_user(app, key)

   
   Check if the user has manually provided the config.
















   ..
       !! processed by numpydoc !!

.. py:function:: escape_ansi(string)

   
   Helper function to remove ansi coloring from sphinx warnings.
















   ..
       !! processed by numpydoc !!

.. py:function:: get_theme_options_dict(app)

   
   Return theme options for the application w/ a fallback if they don't exist.

   The "top-level" mapping (the one we should usually check first, and modify
   if desired) is ``app.builder.theme_options``. It is created by Sphinx as a
   copy of ``app.config.html_theme_options`` (containing user-configs from
   their ``conf.py``); sometimes that copy never occurs though which is why we
   check both.















   ..
       !! processed by numpydoc !!

.. py:function:: maybe_warn(app, msg, *args, **kwargs)

   
   Wraps the Sphinx logger to allow warning suppression.
















   ..
       !! processed by numpydoc !!

.. py:function:: set_secondary_sidebar_items(app, pagename, templatename, context, doctree)

   
   Set the secondary sidebar items to render for the given pagename.
















   ..
       !! processed by numpydoc !!

.. py:function:: traverse_or_findall(node, condition, **kwargs)

   
   Triage node.traverse (docutils <0.18.1) vs node.findall.

   TODO: This check can be removed when the minimum supported docutils version
   for numpydoc is docutils>=0.18.1.















   ..
       !! processed by numpydoc !!

.. py:data:: SPHINX_LOGGER

