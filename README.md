# qa-automation
A unified automation framework for Aspiration

## Installation and Setup:
Instructions for setting up your local environment and installing necessary tools can be found below:
* https://aspirationpartners.atlassian.net/wiki/spaces/EN/pages/331285242/QA+Automation+Setup

## Common Test Running:
The following steps are the most common way of executing tests:
1. If necessary: `pipenv --three update` to update old dependencies 
2. For all tests being executed the VPC tunnel must be started before execution: 
    * `./scripts/tunnel.sh`
3. Execute the desired tests, by either executing the bash script for the related test or by running the test via command line:
    * Running tests via script: 
        * `./scripts/authenticationtests.sh`
    * Running tests via command line: 
        * `pipenv run pytest -m "authentication" --env alpha --platform chrome:firefox --host local`

## Running Tests locally for Native Mobile Apps:
Additional steps for executing tests which have a `--platform` of either `android` or `ios`
1. Start the Appium Server
2. Start the Android or iOS simulated device
3. Perform "Common Test Running" steps for desired mobile tests
    * Example: `./scripts/tunnel.sh
            pipenv run pytest -m "authentication" --platform android`
4. Execute Step 3 from the Common Test Setup section
    * Adjust the `--platform` flag to target the desired native mobile app
    * Example: `pipenv run pytest -m "authentication" --platform android`

## Additional steps for executing tests which have a `--host` of `saucelabs` (Run on the SauceLabs device farm)
1. Open a terminal and cd into the qa-automation directory
2. Start SauceConnect server: `./scripts/startsauce.sh`
    * This service requires this terminal to remain open. No further actions should take place in this terminal. 
3. Open a new terminal and cd into the qa-automation directory
4. Run tests (Execute Step 3 from the Common Test Running section)
    * Example: `pipenv run pytest -m "authentication" --host saucelabs`

## Common PyTest options
Some common command line options which may be used with pytest:
* `--env "environments"` : Colon-delimited list of environments to run test in. Defaults to `alpha`.
    * Valid values are: `alpha:prod`
* `--platform "platforms"` : Colon-delimited list of platforms to run tests on.  Defaults to `chrome`.
    * Valid values are: `chrome:firefox:ios:android`
* `--layer "layers"` : Colon-delimited list of test layers to restrict on.  Defaults to `ui:api`.
    * Valid values are: `ui:api:data`
        * ui: tests requiring a Web Browser or Mobile App
        * api: tests requiring API calls
        * data: tests requiring only database queries
* `--host "test host"` : Defines where test will run. Defaults to `local`.
    * Valid values are either: `saucelabs` or `local`, but not both
* `-m or --marker "marker"` : Run tests which match "marker"
* `-v`: Verbose, shows each test run results.
* `-q` : Quiet, hides docstring from test results 
* `-s` : Disables all capturing. Shows output, but will not capture
* `--reruns #` : Re-run a tests until they either pass, or fail "#" of times.  # is any 
positive integer. (https://github.com/pytest-dev/pytest-rerunfailures)
* `--workers #` : Increase the "#" of thread workers run in parallel.  # is any positive integer.
It is suggested to keep this number no larger than the number of CPU cores available on the test host.
When not specified; 1 a default of 1 worker will run.
(https://pypi.org/project/pytest-parallel)
* `--tests-per-worker #` : Increase the "#" of tests run concurrently per worker thread. # is any positive integer.
When not specified; 1 a default of 1 test will be run concurrently per worker.
(https://pypi.org/project/pytest-parallel)
* `--collect-only` : Collect a list of which tests would be run, without executing the tests.  
# unified-python-automation
