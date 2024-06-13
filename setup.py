from setuptools import find_packages, setup

extras_require = {
    "test" : [ # `test` GitHub Action jobs uses this
        "pytest>=6.0",  # Core testing package
        "pytest-xdist",  # Multi-process runner
        "pytest-cov",  # Coverage analyzer plugin
        "pytest-mock",  # For creating and using mocks
        "hypothesis>=6.2.0,<7.0",  # Strategy-based fuzzer
        "pytest-benchmark",  # For performance tests
    ],
    "lint": [
        "black>=24.4.2,<25",  # Auto-formatter and linter
        "mypy>=1.10.0,<2",  # Static type analyzer
        "types-requests",  # Needed for mypy type shed
        "types-setuptools",  # Needed for mypy type shed
        "types-pkg-resources",  # Needed for type checking tests
        "flake8>=7.0.0,<8",  # Style linter
        "isort>=5.13.2,<6",  # Import sorting linter
        "mdformat>=0.7.17",  # Auto-formatter for markdown
        "mdformat-gfm>=0.3.5",  # Needed for formatting GitHub-flavored markdown
        "mdformat-frontmatter>=0.4.1",  # Needed for frontmatters-style headers in issue templates
        "mdformat-pyproject>=0.0.1",  # Allows configuring in pyproject.toml
    ],
    "doc": [
        "Sphinx>=6.1.3,<7",  # Documentation generator
        "sphinx_rtd_theme>=1.2.0,<2",  # Readthedocs.org theme
        "towncrier>=19.2.0, <20",  # Generate release notes
        # Necessary for a16z docs
        "docconvert >= 2.0.0",
        "mkdocs >= 1.4.2",
        "mkdocs-material >= 9.0.5",
        "mkdocstrings >= 0.19.1,<0.24.0",
        "mkdocstrings-python >= 0.8.3,<0.11.0",
        "cairosvg >= 2.6.0",
    ],
    "release": [  # `release` GitHub Action job uses this
        "setuptools",  # Installation tool
        "setuptools-scm",  # Installation tool
        "wheel",  # Packaging tool
        "twine",  # Package upload tool
    ],
    "dev": [
        "commitizen",  # Manage commits and publishing releases
        "pre-commit",  # Ensure that linters are run prior to committing
        "pytest-watch",  # `ptw` test watcher/runner
        "IPython",  # Console for interacting
        "ipdb",  # Debugger (Must use `export PYTHONBREAKPOINT=ipdb.set_trace`)
    ],
}


# NOTE: `pip install -e .'[dev]'` to install package
extras_require["dev"] = (
    extras_require["test"]
    + extras_require["lint"]
    + extras_require["doc"]
    + extras_require["release"]
    + extras_require["dev"]
)

with open("./README.md") as readme:
    long_description = readme.read()

setup(
    name="ape-farcaster",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description = "ape-farcaster is a Python SDK for the Farcaster Protocol"
    long_description=long_description,
    long_description_content_type="text/markdown",
    authors= [
        {name = "Andreessen Horowitz", email = "crypto-engineering@a16z.com"},
        {name = "ApeWorX LTD.", email = "admin@apeworx.io"},
    ],
    maintainers = [
        {name = "ApeWorX LTD.", email = "admin@apeworx.io"},
    ],
    url="https://github.com/ApeWorX/ape-farcaster",
    include_package_data=True,
    install_requires=[
        "eth-ape>=0.8.4,<0.9",
        "bitarray==2.6.2",
        "cached-property==1.5.2",
        "canonicaljson >= 1.6.4,<3.0.0",
        "certifi==2022.12.7",
        "charset-normalizer==3.0.1",
        "cytoolz==0.12.1",
        "eth-abi", # Use same version as eth-ape
        "eth-account", # Use same version as eth-ape
        "eth-hash==0.5.1",
        "eth-keyfile==0.6.0",
        "eth-keys==0.4.0",
        "eth-rlp==0.3.0",
        "eth-typing", # Use same version as eth-ape
        "eth-utils", # Use same version as eth-ape
        "hexbytes", # Use same version as eth-ape
        "idna==3.4",
        "importlib-metadata==4.13.0",
        "parsimonious >= 0.10.0,<0.11.0",
        "pycryptodome==3.16.0",
        "pydantic", # Use same version as eth-ape
        "pyhumps >= 3.7.2",
        "python-dotenv >= 0.21,<1.1",
        "requests", # Use same version as eth-ape
        "rlp==3.0.0",
        "simplejson==3.18.1",
        "six==1.16.0",
        "toolz==0.12.0",
        "typing-extensions==4.4.0",
        "urllib3==1.26.14",
        "zipp==3.11.0",
    ],
    python_requires=">=3.9,<4",
    extras_require=extras_require,
    py_modules=["ape_farcaster"],
    license="Apache-2.0",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"ape_farcaster": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
