from setuptools import setup, find_packages
setup(
    name="sapt",
    version="0.0.",
    description="aptコマンド支援ツール",
    author="sonyakun",
    packages=find_packages(),
    install_requires="requests",
    entry_points={
        "console_scripts": [
            "sapt-purge=aptUtil:purge",
            "sapt-install=aptUtil:install"
            "sapt-purge=aptUtil:purge"
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.',
    ]
)
