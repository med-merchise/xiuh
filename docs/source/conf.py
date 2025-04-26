"""Configuration file for the Sphinx documentation builder."""

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xiuh'
copyright = '2025, Medardo Antonio Rodriguez'
author = 'Medardo Antonio Rodriguez'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ["**/_*"]

language = 'en'

# -- Options for markup ------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-markup

default_role = 'code'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_options = {
    'light_css_variables': {
        "font-stack--monospace": '''
        "Roboto Mono",
        "SFMono-Regular",
        Menlo,
        Consolas,
        Monaco,
        "Liberation Mono",
        "Lucida Console",
        monospace
        ''',
    },
}
html_title = project
html_static_path = ['_static']

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}
intersphinx_cache_limit = 365  # Maintain the cache forever.

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# -- MyST-Parser Extensions --------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html

myst_enable_extensions = [
    'attrs_block',
    'attrs_inline',
]

myst_heading_anchors = 3  # auto-generated header anchors
