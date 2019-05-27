import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='gcache',  
     version='0.1',
     scripts=['gcache.py'] ,
     author="Luis A. Trutie Ravelo",
     author_email="truravel88@gmail.com",
     description="GCache Client Package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/truravel/gcache-python",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GPL-3",
         "Operating System :: OS Independent",
     ],
 )