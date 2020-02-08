from setuptools import setup, find_packages

setup(
    name             = 'data-ko-analysis',
    version          = '0.1',
    description      = '데이타분석 파이썬을 이용한 예제들 ',
    long_description = open('README.md').read(),
    author           = 'duru',
    author_email     = 'enfn2001@gmail.com',
    url              = 'https://...',
    download_url     = 'https://...',
    install_requires = ['requests'],
    packages         = find_packages(exclude = ['docs', 'example']),
    keywords         = ['data', 'study', 'numpy'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
