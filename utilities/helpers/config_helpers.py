"""Helpers to manage our configuration dictionaries"""

import configuration.environments as environments
import configuration.a_b_tests as a_b_test_settings
import argparse
import urllib.parse

SUPPORTED_ENVIRONMENTS = {'alpha', 'prod'}
DEFAULT_ENVIRONMENT = 'alpha'
SUPPORTED_LAYERS = {'ui', 'api', 'data'}
DEFAULT_LAYER = 'ui:api'


def define_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--marker', action='store',
                        help='Run tests which match marker',
                        required=False)
    parser.add_argument('--markers', action='count',
                        help='List which markers are valid',
                        required=False)
    parser.add_argument('-v', action='store_true',
                        help='Verbose, shows each test run results',
                        required=False)
    parser.add_argument('-s', action='store_true', help='Disable all capturing',
                        required=False)
    parser.add_argument('-q', action='store_true',
                        help= 'Hides docstring from test results',
                        required=False)
    parser.add_argument('--platform', action='store',
                        help='Colon-delimited list of UI platforms to run tests on',
                        required=False)
    parser.add_argument('--workers', action='store', help='Run parallel tests',
                        required=False)
    parser.add_argument('--tests-per-worker', action='store',
                        help='Number of tests per worker',
                        required=False)
    parser.add_argument('--reruns', action='store',
                        help='Number of times to rerun failed tests',
                        required=False)
    parser.add_argument('--env', action='store',
                        help='Colon-delimited list of environments to run tests on',
                        required=False)
    parser.add_argument('--host', action='store',
                        help='Defines which host tests will run on',
                        required=False)
    parser.add_argument('--layer', action='store',
                        help='Colon-delimited list of layers to restrict tests upon',
                        required=False)
    parser.add_argument('--collect-only', action='store_true',
                        help='Collects test names and how many times it runs',
                        required=False)
    parser.add_argument('files', nargs='*',
                        help='Allows for file paths to be passed via command line')
    return parser.parse_args()


def requested_environments():
    """ Returns environments from the --env flag set on command line
        If no environment is requested, return the default environment
        Verifies that the requested environment is supported
        This is returned as a tuple so it can be parametrized by pytest fixtures
    """                                            
    
    args = define_arguments()
    if args.env:
        environments_requested = args.env.split(':')
    else:
        environments_requested = [DEFAULT_ENVIRONMENT]
    for environment in environments_requested:
        if environment not in SUPPORTED_ENVIRONMENTS:
            raise ValueError(f"--env argument '{environment}' not within supported: '{SUPPORTED_ENVIRONMENTS}'")
    return environments_requested


def get_environment_config(environment):
    """Returns a dictionary of environment-specific variables from the environments file"""
    current_env_config = {}
    if hasattr(environments, environment.upper()):
        current_env_config.update(getattr(environments, environment.upper()))
    else:
        raise ValueError(f"Test environment '{environment}' is not found in the environments.py file")
    return current_env_config


def construct_a_b_test_control_url(base_url, ab_settings=a_b_test_settings):
    """
    Re-constructs a URL so it forces the control path of an A/B tests
    The URL is constructed with all of the A/B test dictionaries nested within the ab_settings dictionary parameter
    :param base_url: URL like "https//:www.alpha.aspiration.com"
    :param ab_settings: A dictionary of AB test settings which matches this pattern:
            AB_CONTROL_SETTINGS = {
                'PersonalInfoWeb': {
                    'Namespace': 'PersonalInfoWeb',
                    'Experiment': 'SSNSplitOPT212',
                    'Bucket': 'Control'
                }
            }
    :return: constructed url with the a/b test parameters supplied
    """
    url_override = '?'
    for (test, params) in ab_settings.AB_CONTROL_SETTINGS.items():
        for (key, value) in params.items():
            value = urllib.parse.quote(value)
            if key is 'Namespace':
                if len(url_override) > 1:  url_override = url_override + "&"
                url_override = (url_override + 'AB_OVERRIDE={k}:{v};'.format(k=key, v=value))
            else:
                url_override = (url_override + '{k}:{v};'.format(k=key, v=value))
    url = base_url + url_override
    return url
