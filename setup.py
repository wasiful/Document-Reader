from setuptools import find_packages, setup

from setup_utils import SetupConfig

setup(
    name="documentreader",
    version=SetupConfig.get_version_from_package(),
    author="Wasiful Alam",
    author_email="mr.data.psycho@gmail.com",
    url="https://github.com/",
    description="CSV, Json, Excel reader for pandas",
    long_description=SetupConfig.read_metadata_from_readme(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=SetupConfig.get_install_requirements(),
    license="MIT",
    license_files=("LICENSE",),
    keywords="Pandas, Excel",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 4 - Beta",
        "Environment :: Linux",
    ],
    zip_safe=False,
    include_package_data=True,
)
