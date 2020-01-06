from setuptools import setup
import os


def load_version(path):
    with open(path, "rb") as f:
        lines = f.read().decode("utf-8").splitlines()

    for line in lines:
        d = {}
        try:
            exec(line, d)
            return d["__version__"]
        except KeyError:
            continue
        except Exception:
            continue
    raise Exception("__version__ not found in {}".format(path))


this_dir = os.path.dirname(__file__)

version = load_version(path=os.path.join(this_dir, "source", "yc.py"))

with open(os.path.join(this_dir, "README.md"), "rb") as fo:
    long_description = fo.read().decode("utf8")


setup(
    name='yc',
    package_dir={"": "source"},
    py_modules=['yc'],
    version=version,
    description='Plotting yield locus for various test results',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='omkar_salunke',
    author_email='ossalunke@gmail.com',
    url='https://github.com/omkar-salunke/yield_locus/',
    license="MIT",
    download_url=(
        'https://github.com/omkar-salunke/yield_locus/archive/v{}.tar.gz'
        .format(version)
    ),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Material science",
        "Topic :: Research :: Libraries :: Python Modules",
    ],
)
