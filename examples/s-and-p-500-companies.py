# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
from pprint import pprint

sys.path.insert(0, '.')
from examples.base import run


# Fixtures
dataset = 'datapackage'
prefix = 's_and_p_500_companies_%s_%s_' % (sys.version_info.major, sys.version_info.minor)
source = 'examples/packages/s-and-p-500-companies/datapackage.json'
target = 'tmp/packages/s-and-p-500-companies/datapackage.json'


# Execution
if __name__ == '__main__':
    run(dataset, prefix, source, target)
