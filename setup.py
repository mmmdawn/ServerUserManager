import setuptools

setuptools.setup(
    name="server-user-manager",
    version="0.0.1",
    author="Dawn",
    author_email="congminh292k@gmail.com",
    description="Linux server utilities",
    keywords="linux user-management server",
    license="MIT",
    url="https://github.com/mmmdawn/ServerUserManager",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux"
    ],
    dependencies=[
        "inquirerpy ~= 0.3.4"
    ],
    packages=["usermanager", "usermanager.utils"],
    entry_points={"console_scripts": ["sm=usermanager.__main__:main"]},
    python_requires=">=3.8",
)
