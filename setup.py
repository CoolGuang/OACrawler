from setuptools import setup, find_packages

setup(
    name='OACrawler',
    version='1.0.0',
    description='crawler oa(oi, acm) competition info',
    long_description=open('README.md').read(),
    url='https://github.com/CoolGuang/OACrawler',
    author='CCoolGuang',
    author_email='1836092943@qq.com',
    license='Apache License 2.0',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',   # 更新为 'License :: OSI Approved :: Apache Software License'
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='oi acm crawler library',
    install_requires=['bs4', 'requests', 'lxml'],  # list all dependencies here
)
