from setuptools import setup,find_packages

setup(
    name='tb_wrapper',
    version='0.0.1',    
    description='tb wrapper of the thingsboard library',
    url='https://github.com/GolDandy7/tb_wrapper',
    author='GolDandy7',
    author_email='mail@zoe.com',
    license='BSD 2-clause',
    packages=[find_packages(include=['src'])],
    install_requires=['tb_rest_client',
                      'requests',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: ITC/R&D',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.10',
    ]
)