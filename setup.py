from setuptools import setup

setup(
    name = 'igemwikiscraper',
    version = '0.2.0',
    description = 'CLI+Library webscraper built specifically for iGEM team wiki pages',
    url = 'https://github.com/Virginia-iGEM/igem-wikiscraper',
    author='Dylan Culfogienis',
    author_email='dtc9bb@virginia.edu',
    license='MIT',
    packages=['igemwikiscraper'],
    install_requires = [
        'requests', 
        'beautifulsoup4',
        'lxml'
    ],
    entry_points = {
        'console_scripts': [
            'wikiscraper=igemwikiscraper.__main__:main'
        ]
    }
)
