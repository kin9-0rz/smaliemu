from setuptools import setup


if __name__ == "__main__":

    setup(
        name="smaliemu",
        version="0.0.1",
        description=("smaliemu"),

        packages=[
            "smaliemu",
            "smaliemu.objects",
        ],

        keywords="",
        license="GPL V3",
        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Utilities",
        ],

        author="mikusjelly",
        author_email="mikusjelly@gmail.com",
        url="https://github.com/mikusjelly/smaliemu",

    )
