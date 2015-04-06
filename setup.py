from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='keymaker',
    description="A tool for managing SSH keys",
    version='0.2.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    author='Steven Tsiang',
    author_email='steven@scopely.com',
    url='https://github.com/scopely-devops/keymaker',
    license='MIT',
    install_requires=requirements,
    entry_points= """
        [console_scripts]
        keymaker=keymaker.__main__:keymaker
    """
)
