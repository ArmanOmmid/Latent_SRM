
import sys
import os

repository_root = '/'.join(__file__.split('/')[:__file__.split('/').index('src')])
sys.path.append(repository_root)

from .dsc import dsc_arch, dsc_prototype, dsc_complete
