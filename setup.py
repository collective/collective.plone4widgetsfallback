from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.plone4widgetsfallback',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='simahawk',
      author_email='simahawk@gmail.com',
      url='http://github.com/collective/collective.plone4widgetsfallback',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.z3cform.widgets',
          'plone.app.dexterity',
          'plone.app.z3cform',
          'z3c.form',
          'zope.component',
          'zope.interface',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
