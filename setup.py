from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='petrodc',
    packages=['petrodc', 'petrodc.npd', 'petrodc.usgs_eros', 'petrodc.ags'],
    version='0.1.7',
    license='LGPL v3',
    description='Petroleum Data Collector',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Juan Camilo Gonzalez Angarita',
    author_email='juan@prowellplan.com',
    keywords='petroleum data collector operations wellbore oil gas',
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                 'Natural Language :: English',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Utilities'],
    install_requires=['pandas', 'requests', 'numpy', 'plotly', 'lasio', 'matplotlib']
)
