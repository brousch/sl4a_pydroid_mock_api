from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.4.1'

install_requires = []

dependency_links=[]


setup(name='sl4a_pydroid_mock_api',
    version=version,
    description="Simulates the SL4A Python API for Android",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
                 'Development Status :: 4 - Beta',
                 'Environment :: Console',
                 'Environment :: MacOS X',
                 'Environment :: Win32 (MS Windows)',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Natural Language :: English',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.6',
    ],
    keywords='sl4a android api',
    author='Ben Rousch',
    author_email='brousch@gmail.com',
    url='http://github.com/brousch/sl4a_pydroid_mock_api',
    license='BSD',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    dependency_links=dependency_links,
    entry_points={
        'console_scripts':
            ['android=android:main']
    }
)
