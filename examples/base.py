# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import io
import os
import sys
import json
from apiclient.discovery import build
from oauth2client.client import GoogleCredentials

sys.path.insert(0, '.')
import jtsbq
import dpbq


def run(dataset, prefix, source, target):

    # Storage
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.credentials.json'
    credentials = GoogleCredentials.get_application_default()
    service = build('bigquery', 'v2', credentials=credentials)
    project = json.load(io.open('.credentials.json', encoding='utf-8'))['project_id']
    storage = jtsbq.Storage(service, project, dataset, prefix=prefix)

    # Import package
    dpbq.import_package(storage, source)
    print('Imported datapackage from "%s"' % source)

    # Export package
    dpbq.export_package(storage, target)
    print('Exported datapackage to "%s"' % target)
