from setuptools import setup, find_packages, Extension 

setup( 
        name ='hello',     
        version = '1.0', 
        packages = find_packages(),
        description='a description',
        setup_requires=['setuptools','setuptools_scm'],      
        ext_modules=[Extension('myModule', ['src/helloworld.c'])],    
) 