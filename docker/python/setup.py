from pip.req import parse_requirements
from setuptools import find_packages
from setuptools import setup
from subprocess import call
from setuptools.command.install import install as _install


install_requirements = parse_requirements('requirements.txt', session=False)
requirements = [str(ir.req) for ir in install_requirements]


class install(_install):

    def __post_install(self, dir):
        call(['echo "foo"'])

    def run(self):
        _install.run(self)
        self.execute(
            self.__post_install,
            (self.install_lib,),
            msg="installing auto completion"
            )


setup(
    name='example',
    version='0.1.2',
    author=u'example',
    author_email='foo@example.com',
    description='Some description',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    cmdclass={'install': install},
    )
