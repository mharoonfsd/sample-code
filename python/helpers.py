"""helper functions for base execution(exec_top)."""

import sys
import os
import re

from copy import copy

from .errors import InvalidArgumentError, InvalidValueError
from .constants import (VALID_KWARGS_PATTERNS, VALID_SKWARGS_PATTERNS,
                        VALID_ARGS, VALID_SWITCHES,
                        DEFAULT_VALUES, ARGS_LIST)


def parse_cli_args():
    """Parse arguments, switches and keyword arguments and returns them in dictionary."""
    # set start of pair to 0
    pair_start = 0

    # check if the first argument is the filename and decide where to start parsing arguments
    if sys.argv and os.path.isfile(sys.argv[0]):
        pair_start = 1

    # match the keyword arguments and make pairs
    kwargs = dict([(i[0][2:].lower(), i[1].lower())
                   for i in zip(sys.argv[pair_start::2], sys.argv[pair_start+1::2])
                   if (re.match(r'^--[a-zA-Z0-9_][a-zA-Z0-9_]+$', i[0])
                       and re.match(r'^\w+.*?\w+$', i[1]))
                  ])

    # match the short keyword arguments and make pairs
    skwargs = dict([(i[0][1:], i[1].lower())
                    for i in zip(sys.argv[pair_start::2], sys.argv[pair_start+1::2])
                    if (re.match(r'^-[a-zA-Z]$', i[0])
                        and re.match(r'^\w+.*?\w+$', i[1]))
                   ])

    # match the arguments and make list
    args = sorted(list(set(re.findall(r'\w\w+', ' '.join([i[2:].lower()
                                                          for i in sys.argv
                                                          if (re.match(r'^--[a-zA-Z][a-zA-Z]+$', i)
                                                              and i[2:] not in kwargs.keys())
                                                         ]))
                          )))

    # match the switches and make list
    switches = sorted(list(set(re.findall(r'\w', ' '.join([i for i in sys.argv
                                                           if (re.match(r'^-[a-zA-Z]$', i)
                                                               and i[1:] not in skwargs.keys())
                                                          ]))
                              )))

    # match direct value arguments
    vargs = [v for v in [val for val in sys.argv[pair_start:]
                         if [patt for patt in VALID_KWARGS_PATTERNS.values()
                             if re.match(patt, val)]]
             if v not in kwargs.values()]

    # return arguments and keyword arguments
    return {
        'kwargs': kwargs,
        'skwargs': skwargs,
        'args': args,
        'switches': switches,
        'vargs': vargs
    }

def validate_cli_args(arguments=None):
    """
    Validate arguments, switches and keyword arguments and returns them in dictionary.

        :param arguments={}:
    """
    # default value for arguments
    arguments = parse_cli_args() if not arguments else {}

    # values for arguments
    kwargs_dict = {} if arguments.get('kwargs') is None else arguments.get('kwargs')
    skwargs_dict = {} if arguments.get('skwargs') is None else arguments.get('skwargs')
    args_list = [] if arguments.get('args') is None else arguments.get('args')
    switches_list = [] if arguments.get('switches') is None else arguments.get('switches')

    # validate arguments
    validate_kwargs(kwargs_dict)
    validate_skwargs(skwargs_dict)
    validate_args(args_list)
    validate_switches(switches_list)
    validate_vargs(arguments)

def validate_kwargs(kwargs_dict):
    """
    Validate keyword arguments passed on execution.

        :param kwargs_dict={}:
    """
    # valid keys of arguments
    valid_keys = VALID_KWARGS_PATTERNS.keys()

    # check for invalid key in valid keys
    for key in kwargs_dict.keys():
        if key not in valid_keys:
            raise InvalidArgumentError
        else:
            valid_pattern = VALID_KWARGS_PATTERNS.get(key)
            # check for invalid values in valid patterns
            if not re.match(valid_pattern, kwargs_dict.get(key)):
                raise InvalidValueError
            else:
                pass


def validate_skwargs(skwargs_dict):
    """
    Validate short keyword arguments passed on execution.

        :param skwargs_dict={}:
    """
    # valid keys of arguments
    valid_keys = VALID_SKWARGS_PATTERNS.keys()

    # check for invalid key in valid keys
    for key in skwargs_dict.keys():
        if key not in valid_keys:
            raise InvalidArgumentError
        else:
            valid_pattern = VALID_SKWARGS_PATTERNS.get(key)
            if not re.match(valid_pattern, skwargs_dict.get(key)):
                raise InvalidValueError
            else:
                pass

def validate_args(args_list):
    """
    Validate arguments passed on execution.

        :param args_list=[]:
    """
    # check for invalid argument in valid arguments
    for arg in args_list:
        if arg not in VALID_ARGS:
            raise InvalidArgumentError

def validate_switches(switches_list):
    """
    Validate switches passed on execution.

        :param arguments=[]:
    """
    # check for invalid switch in valid switches
    for switch in switches_list:
        if switch not in VALID_SWITCHES:
            raise InvalidArgumentError

def validate_vargs(arguments):
    """
    Validate direct value arguments passed on execution.

        :param arguments={}:
    """
    kwargs_dict = arguments.get('kwargs') if arguments.get('kwargs') else {}
    args_list = arguments.get('args') if arguments.get('args') else []
    vargs_list = arguments.get('vargs') if arguments.get('vargs') else []

    matched_patterns_of = []
    expired_patterns_of = []
    current_index = 0
    return_dict = {}

    # get types of values
    for val in vargs_list:
        matched_patterns_length = len(matched_patterns_of)
        patts = copy(VALID_KWARGS_PATTERNS)

        # remove already expired patterns
        expired_patterns = (expired_patterns_of + list(kwargs_dict.keys()) +
                            args_list)
        for pop in expired_patterns:
            patts.pop(pop)

        # check which values were matched
        for patt in patts.items():
            if re.match(patt[1], val):
                expired_patterns_of.append(patt[0])
                matched_patterns_of.append(patt[0])
                return_dict.update({patt[0]: val})
            else:
                expired_patterns_of.append(patt[0])
                continue
        current_index += 1
        expired_patterns_of = expired_patterns_of[:current_index]

        if matched_patterns_length == len(matched_patterns_of):
            raise InvalidValueError

    return return_dict

    # filter out invalid values
    # invalid_patterns_of = [val for val in expired_patterns_of if val not in matched_patterns_of]

    # raise invalid sequence error if sequence does not match
    # if tuple(matched_patterns_of) not in VALID_ARGUMENT_COMBINARTIONS:
    #     raise InvalidValueArgsSequenceError


def consolidate_cli_args(arguments):
    """Consolidates similar valid arguments and returns final arguments."""
    # values for arguments
    kwargs_dict = {} if arguments.get('kwargs') is None else arguments.get('kwargs')
    skwargs_dict = {} if arguments.get('skwargs') is None else arguments.get('skwargs')
    args_list = [] if arguments.get('args') is None else arguments.get('args')
    switches_list = [] if arguments.get('switches') is None else arguments.get('switches')

    # copy ARGS_LIST so original object does not get modified
    args_list_copy = copy(ARGS_LIST)

    # return dictionary holding consolidated arguments
    return_dict = {}

    # get arguments from kwargs
    for kwarg in kwargs_dict.items():
        argument_filter = [arg_obj for arg_obj in args_list_copy
                           if arg_obj.get('kwarg') == kwarg[0]
                          ]
        argument_object = argument_filter[0] if argument_filter else None
        if argument_object:
            return_dict.update({argument_object['kwarg']: kwarg[1]})
            args_list_copy.pop(args_list_copy.index(argument_object))

    # get arguments from skwargs
    for skwarg in skwargs_dict.items():
        argument_filter = [arg_obj for arg_obj in args_list_copy
                           if arg_obj.get('skwarg') == skwarg[0]
                          ]
        argument_object = argument_filter[0] if argument_filter else None
        if argument_object:
            return_dict.update({argument_object['kwarg']: skwarg[1]})
            args_list_copy.pop(args_list_copy.index(argument_object))

    # get arguments from args
    for arg in args_list:
        argument_filter = [arg_obj for arg_obj in args_list_copy
                           if [a for a in arg_obj.get('args') if a == arg]
                          ]
        argument_object = argument_filter[0] if argument_filter else None
        if argument_object:
            return_dict.update({argument_object['kwarg']: arg})
            args_list_copy.pop(args_list_copy.index(argument_object))

    # get arguments from args
    for switch in switches_list:
        argument_filter = [arg_obj for arg_obj in args_list_copy
                           if [a for a in arg_obj.get('args') if a == switch]
                          ]
        argument_object = argument_filter[0] if argument_filter else None
        if argument_object:
            return_dict.update({argument_object['kwarg']: switch})
            args_list_copy.pop(args_list_copy.index(argument_object))

    # get arguments from direct values
    # get direct values matched
    valid_values_of = validate_vargs(arguments)

    # append if not in return dict
    for item in valid_values_of.items():
        if item[0] not in return_dict.keys():
            return_dict.update({item[0]: item[1]})

    # set default values for arguments
    for item in DEFAULT_VALUES.items():
        if item[0] not in return_dict.keys():
            return_dict.update({item[0]: item[1]})

    return return_dict


def update_env_vars(arguments):
    """
    Update the environment variables of os.

        :param arguments={}:
    """
    # convert arguments to strings
    arguments = dict((k, str(arguments[k])) for k in arguments.keys())

    # update environment variables
    os.environ.update(arguments)
