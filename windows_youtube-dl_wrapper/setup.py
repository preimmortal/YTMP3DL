from distutils.core import setup
import py2exe

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

setup(console=['ytdl_wrapper.py'])