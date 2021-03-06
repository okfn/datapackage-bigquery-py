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
prefix = 'finance_vix_%s_%s_' % (sys.version_info.major, sys.version_info.minor)
source = 'examples/packages/finance-vix/datapackage.json'
target = 'tmp/packages/finance-vix/datapackage.json'


# Execution
if __name__ == '__main__':
    run(dataset, prefix, source, target)
