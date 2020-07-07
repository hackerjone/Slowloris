from distutils.core import setup

setup(
    name="Slowloris",
    py_modules=["slowloris"],
    entry_points={"console_scripts": ["slowloris=slowloris:main"]},
    version="1.0",
    description="Low bandwidth DoS tool. Slowloris rewrite in Python.",
    author="Gokberk Yaltirakli",
    author_email="webdosusb@gmail.com",
    url="https://github.com/hackerjone/Slowloris",
    keywords=["dos", "http", "slowloris"],
    license="MIT",
)
