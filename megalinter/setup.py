from setuptools import setup

setup(
    name="megalinter",
    version="0.1",
    description="Mega-Linter",
    url="http://github.com/nvuillam/mega-linter",
    author="Nicolas Vuillamy",
    author_email="nicolas.vuillamy@gmail.com",
    license="MIT",
    packages=["megalinter", "megalinter.linters", "megalinter.reporters"],
    install_requires=[
        "gitpython",
        "jsonschema",
        "jsonpickle",
        "multiprocessing_logging",
        "pychalk",
        "pygithub",
        "pytablewriter",
        "pytest-cov",
        "pytest-timeout",
        "pyyaml",
        "requests==2.24.0",
        "terminaltables",
        "webpreview",
        "yq",
        "importlib-metadata>=3.10",
        "mkdocs-material",
        "mdx_truly_sane_lists",
        "beautifulsoup4",
        "giturlparse",
    ],
    entry_points={
        'console_scripts': [
            'mega-linter = megalinter.run',
        ],
    },
    zip_safe=False,
)
