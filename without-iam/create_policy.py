#!/usr/bin/env python3

import sys
import yaml
import json
import logging
from pprint import pprint

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
console_logging = logging.StreamHandler()
console_logging.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(console_logging)

files = sys.argv[1:]
documents = []

for file in files:
    with open(file, 'r') as f:
        d = yaml.safe_load(f)

        try:
            annotations = d.get('metadata').get('annotations')
            if 'release.openshift.io/feature-set' in annotations.keys():
                if annotations['release.openshift.io/feature-set'] == 'TechPreviewNoUpgrade':
                    logger.warning(f'not including {file} due to presence of TechPreviewNoUpgrade')
        except AttributeError as e:
            logger.error(f'unable to parse {file} trying to get .metadata.annotations')
            continue
        documents.append(d)

policy_document = {
    "Version": "2012-10-17",
    "Statement": []
}

for document in documents:
    statements = []
    name = document['metadata']['name']
    for i, entry in enumerate(document['spec']['providerSpec']['statementEntries']):
        statement = {
            "Sid": f"{name.replace('-','')}{i}",
            "Effect": entry['effect'],
            "Resource": entry['resource'],
            "Action": entry['action']
        }
        if entry.get('policyCondition', None) is not None:
            statement['Condition'] = entry['policyCondition']
        statements.append(statement)
    policy_document['Statement'] = policy_document['Statement'] + statements

print(json.dumps(policy_document, indent=2))
