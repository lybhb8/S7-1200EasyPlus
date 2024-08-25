pydata_sphinx_theme.toctree
===========================

.. py:module:: pydata_sphinx_theme.toctree

.. autoapi-nested-parse::

   Methods to build the toctree used in the html pages.

   ..
       !! processed by numpydoc !!


Classes
-------

.. autoapisummary::

   pydata_sphinx_theme.toctree.LinkInfo


Functions
---------

.. autoapisummary::

   pydata_sphinx_theme.toctree._get_ancestor_pagename
   pydata_sphinx_theme.toctree.add_collapse_checkboxes
   pydata_sphinx_theme.toctree.add_inline_math
   pydata_sphinx_theme.toctree.add_toctree_functions
   pydata_sphinx_theme.toctree.get_nonroot_toctree


Module Contents
---------------

.. py:class:: LinkInfo

   
   Dataclass to generate toctree data.
















   ..
       !! processed by numpydoc !!

   .. py:attribute:: href
      :type:  str


   .. py:attribute:: is_current
      :type:  bool


   .. py:attribute:: is_external
      :type:  bool


   .. py:attribute:: title
      :type:  str


.. py:function:: _get_ancestor_pagename(app, pagename, startdepth)

   
   Get the name of `pagename`'s ancestor that is rooted `startdepth` levels below the global root.
















   ..
       !! processed by numpydoc !!

.. py:function:: add_collapse_checkboxes(soup)

   
   Add checkboxes to collapse children in a toctree.
















   ..
       !! processed by numpydoc !!

.. py:function:: add_inline_math(node)

   
   Render a node with HTML tags that activate MathJax processing.

   This is meant for use with rendering section titles with math in them, because
   math outputs are ignored by pydata-sphinx-theme's header.

   related to the behaviour of a normal math node from:
   https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/mathjax.py#L28















   ..
       !! processed by numpydoc !!

.. py:function:: add_toctree_functions(app, pagename, templatename, context, doctree)

   
   Add functions so Jinja templates can add toctree objects.
















   ..
       !! processed by numpydoc !!

.. py:function:: get_nonroot_toctree(app, pagename, ancestorname, toctree, **kwargs)

   
   Get the partial TocTree (rooted at `ancestorname`) that dominates `pagename`.

   Parameters:
   app : Sphinx app.
   pagename : Name of the current page (as Sphinx knows it; i.e., its relative path
   from the documentation root).
   ancestorname : Name of a page that dominates `pagename` and that will serve as the
   root of the TocTree fragment.
   toctree : A Sphinx TocTree object. Since this is always needed when finding the
   ancestorname (see _get_ancestor_pagename), it's more efficient to pass it here to
   re-use it.
   kwargs : passed to the Sphinx `toctree` template function.

   This is similar to `context["toctree"](**kwargs)` (AKA `toctree(**kwargs)` within a
   Jinja template), or `TocTree.get_toctree_for()`, which always uses the "root"
   doctree (i.e., `doctree = self.env.get_doctree(self.env.config.root_doc)`).















   ..
       !! processed by numpydoc !!

