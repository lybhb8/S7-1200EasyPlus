pydata_sphinx_theme.translator
==============================

.. py:module:: pydata_sphinx_theme.translator

.. autoapi-nested-parse::

   A custom Sphinx HTML Translator for Bootstrap layout.

   ..
       !! processed by numpydoc !!


Attributes
----------

.. autoapisummary::

   pydata_sphinx_theme.translator.logger


Classes
-------

.. autoapisummary::

   pydata_sphinx_theme.translator.BootstrapHTML5TranslatorMixin


Functions
---------

.. autoapisummary::

   pydata_sphinx_theme.translator.setup_translators


Module Contents
---------------

.. py:class:: BootstrapHTML5TranslatorMixin(*args, **kwds)

   
   Mixin HTML Translator for a Bootstrap-ified Sphinx layout.

   Only a couple of functions have been overridden to produce valid HTML to be
   directly styled with Bootstrap, and fulfill acessibility best practices.















   ..
       !! processed by numpydoc !!

   .. py:method:: depart_table(node)

      
      Custom depart_table method to close the scrollable div we add in visit_table.
















      ..
          !! processed by numpydoc !!


   .. py:method:: starttag(*args, **kwargs)

      
      Perform small modifications to tags.

      - ensure aria-level is set for any tag with heading role















      ..
          !! processed by numpydoc !!


   .. py:method:: visit_table(node)

      
      Custom visit table method.

      Copy of sphinx source to *not* add 'docutils' and 'align-default' classes but add 'table' class.















      ..
          !! processed by numpydoc !!


   .. py:attribute:: table_style
      :value: 'table'



.. py:function:: setup_translators(app)

   
   Add bootstrap HTML functionality if we are using an HTML translator.

   This re-uses the pre-existing Sphinx translator and adds extra functionality defined
   in ``BootstrapHTML5TranslatorMixin``. This way we can retain the original translator's
   behavior and configuration, and _only_ add the extra bootstrap rules.
   If we don't detect an HTML-based translator, then we do nothing.















   ..
       !! processed by numpydoc !!

.. py:data:: logger

