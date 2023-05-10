import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
long_description = "My Description"

setuptools.setup(
    name='translator',
    version='0.0.3',
    author='Hunter',
    author_email='hunter@hotmail.com',
    description='Hunter Installation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mike-huls/toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    },
    license='MIT',
    packages=['translator'],
    install_requires=['requests'],
)