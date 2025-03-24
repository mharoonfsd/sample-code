"""constants used during base execution."""

import os
import re

# can also use marshal but using json because the dataset is not very large
from json import load
from itertools import combinations, chain
from collections import OrderedDict


# project root dir
ROOT_DIR = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')

# arguments and regexp patterns
ARGS_LIST = load(open('./args.json', 'r'))

# valid keyword arguments and regexp patterns
VALID_KWARGS_PATTERNS = OrderedDict([(item['kwarg'], item['pattern'])
                                     for item in ARGS_LIST
                                    ])

# join all keywords to generate available short keyword arguments
AVAILABLE_SKWARG_KEYS = (list(set(re.findall(r'\w', ''.join(VALID_KWARGS_PATTERNS.keys())))) +
                         list(set(re.findall(r'\w', ''.join(VALID_KWARGS_PATTERNS.keys()).upper())))
                        )

# associate short keyword arguments with appropriate argument object
for arg_obj in ARGS_LIST:
    possible_skwarg = chain.from_iterable(
        [[w.lower(), w.upper()] for w in re.findall(r'\w', arg_obj['kwarg'])]
    )
    for skwarg in possible_skwarg:
        if skwarg in AVAILABLE_SKWARG_KEYS:
            arg_obj['skwarg'] = skwarg
            AVAILABLE_SKWARG_KEYS.pop(AVAILABLE_SKWARG_KEYS.index(skwarg))
            break

# valid short keyword arguments and regexp patterns
VALID_SKWARGS_PATTERNS = OrderedDict([(item['skwarg'], item['pattern'])
                                      for item in ARGS_LIST
                                     ])

# valid arguments
VALID_ARGS = list(set(chain.from_iterable([item['args'] for item in ARGS_LIST])))

# join all arguments to generate available short arguments/switches
AVAILABLE_SWITCHES = (list(set(re.findall(r'\w', ''.join(VALID_ARGS)))) +
                      list(set(re.findall(r'\w', ''.join(VALID_ARGS).upper())))
                     )

# associate switch arguments with appropriate argument object
for arg_obj in ARGS_LIST:
    switches = []
    for arg in arg_obj['args']:
        possible_switches = list(chain.from_iterable(
            [[w.lower(), w.upper()] for w in re.findall(r'\w', arg)]
        ))
        for switch in possible_switches:
            if switch in AVAILABLE_SWITCHES:
                switches.append(switch)
                AVAILABLE_SWITCHES.pop(AVAILABLE_SWITCHES.index(switch))
                break
    arg_obj['switches'] = switches

# valid switches
VALID_SWITCHES = list(set(chain.from_iterable([item['switches'] for item in ARGS_LIST])))

# default values for arguments
DEFAULT_VALUES = OrderedDict([(item['kwarg'], item['default'])
                              for item in ARGS_LIST if item.get('default')
                             ])

# create all possible combinations of keyword arguments
VALID_ARGUMENT_COMBINARTIONS = list(chain.from_iterable(
    [list(j) for j in [combinations(VALID_KWARGS_PATTERNS.keys(), i)
                       for i in range(1, len(VALID_KWARGS_PATTERNS) + 1)]]
))
