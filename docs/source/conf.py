"""Configuration file for the Sphinx documentation builder."""

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xiuh'


def _package_metadata():
    """Get package metadata (if possible) using `importlib` module."""
    from importlib.metadata import metadata, PackageNotFoundError

    default = {
        'author': "Medardo Antonio Rodriguez",
        'version': '0.1.0',
        'summary': "Set your project description here",
    }
    try:
        res = metadata(project)
        return {key: res.get(key, default[key]) for key in default}
    except PackageNotFoundError:
        return default


def _copyright_interval(start_year):
    """Calculate the copyright prefix."""
    from datetime import datetime

    current_year = datetime.now().year
    if current_year > start_year:
        return f'{start_year}-{current_year}'
    else:
        return f'{start_year}'


_pkg_info = _package_metadata()

author = _pkg_info['author']
copyright = f'{_copyright_interval(2025)}, {author}'
release = _pkg_info['version']
version = '.'.join(release.split('.')[:2])

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
