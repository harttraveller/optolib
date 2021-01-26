from setuptools import setup 

setup(
    name='optolib',
    version='0.1.0',
    description='A Python package to model options strategy payoffs',
    url='https://github.com/harttraveller/optolib',
    author='Hart Traveller',
    author_email='hartktraveller@gmail.com',
    license='MIT License',
    packages=['optolib'],
    install_requires=['robin-stocks','plotly','matplotlib','seaborn','pandas','numpy','yahoofinancials']
)