'''
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2017  Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
'''

from shlex import quote
import sys
import logging
logger = logging.getLogger(__name__)


def build_cpp_extension():
    import subprocess as sp
    import os, sys
    src_loc = os.path.dirname(os.path.realpath(__file__))
    install_loc = os.path.split(os.path.split(src_loc)[0])[0]
    cwd = os.getcwd()
    os.chdir(src_loc)
    logger.info('Building extention modules...')
    build_cmd = "{} setup.py install --install-lib={}"
    ret = sp.check_output(build_cmd.format(quote(sys.executable), quote(install_loc)), shell=True).decode(sys.stdout.encoding)
    logger.debug('Build log:\n{}'.format(ret))
    os.chdir(cwd)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    build_cpp_extension()
