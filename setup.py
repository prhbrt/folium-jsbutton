from setuptools import setup, find_packages

setup(
    name='folium-jsbutton',
    version=__import__('folium_jsbutton').__version__,

    description='',
    long_description='',

    url='https://github.com/prinsherbert/folium-jsbutton',

    author='Herbert Kruitbosch',
    author_email='H.T.Kruitbosch@rug.nl',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Map people',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    # What does your project relate to?
    keywords='',
    packages=['folium_jsbutton'],
    include_package_data=True,

    install_requires=[
        'folium>=0.6.0',
    ],
    zip_safe=True,
)

