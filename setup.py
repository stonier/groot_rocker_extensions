#!/usr/bin/env python3

##############################################################################
# Imports
##############################################################################

import setuptools

##############################################################################
# Requirements
##############################################################################

install_requires = [
    # build
    'setuptools',
    # runtime
    'groot_rocker',
]

tests_require = ['nose']

extras_require = {
    'test': tests_require,
    'docs': [],  # ["Sphinx", "sphinx-argparse", "sphinx_rtd_theme", "sphinx-autodoc-typehints"],
    'debs': ['pyprof2calltree', 'stdeb', 'twine']
}

##############################################################################
# Setup
##############################################################################

d = setuptools.setup(
    name='groot_rocker_extensions',
    version='0.1.0',
    packages=setuptools.find_packages(exclude=['tests*', 'docs*']),
    package_data={'groot_rocker_extensions': ['templates/*.em']},
    install_requires=install_requires,
    extras_require=extras_require,
    author='Daniel Stonier',
    maintainer='Daniel Stonier <d.stonier@gmail.com>',
    url='http://github.com/stonier/groot_rocker_extensions',
    keywords=['docker', 'rocker'],
    zip_safe=True,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
    description="groot_rocker extensions for groot workflows",
    long_description="A few rocker extensiosn for groot workflows.",
    license='BSD',
    test_suite='nose.collector',
    python_requires='>=3.0',
    tests_require=tests_require,
    entry_points={
        'groot_rocker.extensions': [
            'named_prompt = groot_rocker_extensions.named_prompt:NamedPrompt',
            'work_directory = groot_rocker_extensions.work_directory:WorkDirectory',
        ],
    },
)
