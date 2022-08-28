from setuptools import setup

setup(
    name='polished',
    version='0.1',
    description='Authentication and User Management for py-shiny',
    url='http://github.com/storborg/funniest',
    author='Andy Merlino',
    author_email='andy.merlino@tychobra.com',
    license='MIT',
    packages=['polished'],
    zip_safe=False,
    exclude_package_data = {'': ['.gitignore', 'examples/*']}
)
