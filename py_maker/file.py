import json
from datetime import datetime
from py_maker.make_package.package import Package 
from py_maker.config.json_writer import get_dir
from pkg_resources import resource_string as resource_bytes

# TODO: create an author class 
with (get_dir() / "config.json").open('r',encoding='utf-8') as f:
  config_data = json.load(f)

author = config_data["author"]
author_email = config_data["author-email"]


# TODO: Write files here 
# make it so that the arugments are author and projects 
class Files:
  def __init__(self, project):
    self.project = project


  def setup(self, path):
    setup = resource_bytes('py_make.__main__', 'templates/setup_template.txt').decode("utf-8")
    with open(f"{self.project}.name/setup.py", "w") as f:
      f.write()


  #   f"""import setuptools
  # import {self.project.name}
    
  # with open("README.md", "r") as fh:
  #   long_description = fh.read()

  # setuptools.setup(
  #   name="{self.project.name}",
  #   version={self.project}.__version__,
  #   author="{author}",
  #   author_email="{author_email}",
  #   description="TODO:A small example package",
  #   long_description=long_description,
  #   long_description_content_type="text/markdown",
  #   url="TODO: Enter URL",
  #   packages=setuptools.find_packages(),
  #   classifiers=[
  #       "Programming Language :: Python :: 3",
  #       "License :: OSI Approved :: MIT License",
  #       "Operating System :: OS Independent",
  #   ],
  #   python_requires='>=3.6',    
  # )"""



  def license_writer():
    return f"""Copyright (c) {datetime.now().year} {author}

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE."""


  def readme_writer(self):
    return f"""# {self.project.capitalize()}

  :TODO  write a description


  ## Installation

      $ pip install {self.project.name}

  ## Usage
  TODO: write quick tutorial 


  This is a simple example package. You can use
  [Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
  to write your content."""

  def init_writer(self):
      return f"__version__ = '{self.project.version}'"