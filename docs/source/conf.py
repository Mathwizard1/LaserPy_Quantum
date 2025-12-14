# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'LaserPy_Quantum'
copyright = '2025, Anshurup Gupta'
author = 'Anshurup Gupta'
release = '0.0.9'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',           # Google/NumPy docstrings (built-in!)
    'sphinx.ext.viewcode',
    #'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Intersphinx (cross-references) ------------------------------------------
# intersphinx_mapping = {
#     'python': ('https://docs.python.org/3', None),
#     'numpy': ('https://numpy.org/doc/stable/', None),
#     'matplotlib': ('https://matplotlib.org/stable/', None),
# }

# Napoleon settings (for Google/NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_use_ivar = True

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'undoc-members': True,
    'exclude-members': '__weakref__',
}

add_module_names = False

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'      # Beautiful Read the Docs theme
html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_static_path = ['_static']
#html_logo = '_static/logo.png'       # Add your logo here later
#html_favicon = '_static/favicon.ico' # Add favicon later

html_context = {
    'display_github': False,
    'github_user': 'Mathwizard1',
    'github_repo': 'LaserPy_Quantum',
}
