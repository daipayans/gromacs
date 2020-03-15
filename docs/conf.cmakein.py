#
# This file is part of the GROMACS molecular simulation package.
#
# Copyright (c) 2015,2016,2017,2018,2019 by the GROMACS development team.
# Copyright (c) 2020, by the GROMACS development team, led by
# Mark Abraham, David van der Spoel, Berk Hess, and Erik Lindahl,
# and including many others, as listed in the AUTHORS file in the
# top-level source directory and at http://www.gromacs.org.
#
# GROMACS is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation; either version 2.1
# of the License, or (at your option) any later version.
#
# GROMACS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with GROMACS; if not, see
# http://www.gnu.org/licenses, or write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA.
#
# If you want to redistribute modifications to GROMACS, please
# consider that scientific software is very special. Version
# control is crucial - bugs must be traceable. We will be happy to
# consider code for inclusion in the official distribution, but
# derived work must not be called official GROMACS. Details are found
# in the README & COPYING files - if they are missing, get the
# official version at http://www.gromacs.org.
#
# To help us fund GROMACS development, we humbly ask that you cite
# the research papers on the package. Check out http://www.gromacs.org.

# -*- coding: utf-8 -*-
#
# GROMACS documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 13 14:28:44 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import datetime
import os
import sys

# The following definitions are completed via CMake machinery.
gmx_containers_path = '@GMX_ADMIN_DIR@/containers'
gmx_sphinx_extension_path = '@SPHINX_EXTENSION_PATH@'
gmxapi_staging_path = '@GMXAPI_PYTHON_STAGING_DIR@'
releng_path = '@RELENG_PATH@'
gmx_version_string = '@GMX_VERSION_STRING@'
gmx_version_string_full = '@GMX_VERSION_STRING_FULL@'
regressiontest_version = '@REGRESSIONTEST_VERSION@'
gmx_min_sphinx = '@EXPECTED_SPHINX_VERSION@'
gmx_image_convert = '@IMAGE_CONVERT_STRING@'
variables = [
    ('EXPECTED_DOXYGEN_VERSION', '@EXPECTED_DOXYGEN_VERSION@'),
    ('EXPECTED_SPHINX_VERSION', '@EXPECTED_SPHINX_VERSION@'),
    ('CMAKE_MINIMUM_REQUIRED_VERSION', '@CMAKE_MINIMUM_REQUIRED_VERSION@'),
    ('REQUIRED_CUDA_VERSION', '@REQUIRED_CUDA_VERSION@'),
    ('REQUIRED_CUDA_COMPUTE_CAPABILITY', '@REQUIRED_CUDA_COMPUTE_CAPABILITY@'),
    ('REQUIRED_OPENCL_MIN_VERSION', '@REQUIRED_OPENCL_MIN_VERSION@'),
    ('SOURCE_MD5SUM', '@SOURCE_MD5SUM@'),
    ('REGRESSIONTEST_MD5SUM', '@REGRESSIONTEST_MD5SUM_STRING@'),
    ('GMX_TNG_MINIMUM_REQUIRED_VERSION', '@GMX_TNG_MINIMUM_REQUIRED_VERSION@'),
    ('GMX_LMFIT_REQUIRED_VERSION', '@GMX_LMFIT_REQUIRED_VERSION@'),
    ('GMX_MANUAL_DOI_STRING', '@GMX_MANUAL_DOI_STRING@'),
    ('GMX_SOURCE_DOI_STRING', '@GMX_SOURCE_DOI_STRING@')
]
# End of build-time substitutions.

sys.path.append(gmx_containers_path)
sys.path.append(gmx_sphinx_extension_path)
if releng_path and os.path.isdir(releng_path):
    sys.path.append(releng_path)
if gmxapi_staging_path and os.path.isdir(gmxapi_staging_path):
    sys.path.append(gmxapi_staging_path)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# gmx_min_sphinx is set from the expected minimum version of Sphinx
# in CMakeLists.txt
needs_sphinx = gmx_min_sphinx

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'gmxsphinx'
]
extlinks = {'issue': ('https://redmine.gromacs.org/issues/%s',
                      'Issue ')}

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'GROMACS'
copyright = str(datetime.datetime.now().year) + u', GROMACS development team'
thisyear_string = str(datetime.datetime.now().year)
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = gmx_version_string
# The full version, including alpha/beta/rc tags.
release = gmx_version_string_full
# default file extension for plots
plotext = u'.eps'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['fragments']
if not tags.has('do_man'):
    exclude_patterns += ['man']

# Set variable if documentation build can convert images or not
# to selectively include files in reference manual
def setup(app):
    app.add_config_value('gmx_image_convert', 'impossible', 'env')

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = 'any'

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# Configure the values for all the variables that might later configure any of the .rst files.
substitutions = ['.. |{0}| replace:: {1}'.format(*x) for x in variables if x[1]]
substitutions.extend(['.. |{0}| replace:: unknown'.format(x[0]) for x in variables if x[1] == ''])
rst_epilog = "\n".join(substitutions)
rst_epilog += """
.. |Gromacs| replace:: GROMACS
.. _gmx-manual: manual-{gmx_version_string}.pdf
.. _gmx-manual-parent-dir: ../manual-{gmx_version_string}.pdf
.. |gmx-source-package-ftp| replace:: As ftp ftp://ftp.gromacs.org/pub/gromacs/gromacs-{gmx_version_string}.tar.gz
.. |gmx-source-package-http| replace:: As http http://ftp.gromacs.org/pub/gromacs/gromacs-{gmx_version_string}.tar.gz
.. |gmx-regressiontests-package| replace:: http://gerrit.gromacs.org/download/regressiontests-{regressiontest_version}.tar.gz
.. _up-to-date installation instructions: http://manual.gromacs.org/documentation/current/install-guide/index.html
.. _CUDA: http://www.nvidia.com/object/cuda_home_new.html
.. _OpenCL: https://www.khronos.org/opencl/
.. _OpenMPI: http://www.open-mpi.org
.. _MPICH: http://www.mpich.org
.. _LAM-MPI: http://www.lam-mpi.org
.. _OpenMP: http://en.wikipedia.org/wiki/OpenMP
.. _CMake installation page: http://www.cmake.org/install/
.. _Ubuntu toolchain ppa page: https://launchpad.net/~ubuntu-toolchain-r/+archive/ubuntu/test
.. _EPEL page: https://fedoraproject.org/wiki/EPEL
.. _running CMake: http://www.cmake.org/runningcmake/
.. _CMake environment variables: http://cmake.org/Wiki/CMake_Useful_Variables#Environment_Variables
.. _FFTW: http://www.fftw.org
.. _FFTW installation guide: http://www.fftw.org/doc/Installation-and-Customization.html#Installation-and-Customization
.. _MKL: https://software.intel.com/en-us/intel-mkl
.. _VMD: http://www.ks.uiuc.edu/Research/vmd/
.. _PyMOL: http://www.pymol.org
.. _continuous integration server used by GROMACS: http://jenkins.gromacs.org
.. _Jenkins: http://jenkins-ci.org
.. _webpage: http://www.gromacs.org
.. _ftp site: ftp://ftp.gromacs.org/pub/gromacs/
.. _tutorials: http://www.gromacs.org/Documentation/Tutorials
.. _redmine: http://redmine.gromacs.org
.. _gerrit: http://gerrit.gromacs.org
.. _download: ../download.html
.. |thisyear| replace:: {thisyear_string}
""".format(gmx_version_string=gmx_version_string, regressiontest_version=regressiontest_version, thisyear_string=thisyear_string)

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'classic'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = u'GROMACS ' + release + ' documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = u'GROMACS ' + version

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Gromacsdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'a4paper',


# The font size ('10pt', '11pt' or '12pt').
'pointsize': '11',

# Additional stuff for the LaTeX preamble.
# The tocdepth setting is needed to overwrite the default value set by Sphinx
# to get a more detailed toctree in the pdf version of the manual.
    'preamble': r'''
    \usepackage{here}
    \usepackage{picins}
    \usepackage{underscore}
    \usepackage{tabularx}
    \usepackage{multicol}
    \usepackage{dcolumn}
    \usepackage{makeidx}
    \usepackage{times}
    \usepackage{ifthen}
    \usepackage{enumitem}
    \usepackage{longtable}
    \usepackage{pdflscape}
    \pagenumbering{roman}
    \usepackage{array}
    \setcounter{tocdepth}{2}
    ''',
# Format output to avoid empty pages
  'classoptions': ',openany,oneside'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'gromacs.tex', u'GROMACS Documentation',
   u'GROMACS development team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'reference-manual/plots/peregrine.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
if tags.has('do_man'):
    exec(open('conf-man.py').read())

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'GROMACS', u'GROMACS Documentation',
   u'GROMACS development team', 'GROMACS', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# Make it possible to use numbered labels for figures and tables
numfig = True

# -- Options for intersphinx extension ------------------------------------

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
intersphinx_cache_limit = -1
intersphinx_timeout = 10
