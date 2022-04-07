import setuptools

with open("README.md", "r" , encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
        name = "example-pkg-UCHENNA", 
        version="0.0.1",
        author="Uchenna Ilodigwe",
        description="Assignment1",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="http://github.com/uchennailodigwe/VC/tree/main/Week1",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating Sytem :: OS Independent",
            
            ]
            packages=setuptools.find_packages(),
            python_requires='>=3.6',
            
)            
