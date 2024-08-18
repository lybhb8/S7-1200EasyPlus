# 头部添加导入
# import sphinx_book_theme

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'S7-1200 PLC 技术手册 EasyPlus'
copyright = '2024, 宁波双紫信息科技有限公司'
author = 'lybhb8'
release = '4.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os, sys; sys.path.append(os.path.abspath('sphinxext'))

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    #"sphinx_togglebutton",
    #'extname',
]

templates_path = ['_templates']
exclude_patterns = []
language = 'zh_CN'

source_suffix = {
    
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}


#source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'press'
html_theme = 'sphinx_rtd_theme'


html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }


# 添加你自己的 CSS 规则
html_static_path = ['_static']
html_css_files = ["custom.css"]
# 自定义徽标、和网站图标
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"

