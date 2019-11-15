"""A collection of dictionaries containing environment-specific configurations
  which are not too sensitive to store in vault

  Every other dictionary will be loaded based on the environment requested

  All dictionaries must be named UPPER CASE"""

ALPHA = {
    "env": "alpha",
    "databases": {
        # database configs
    },
    "db_server_config": {
        "host": "",
        "port": "",
        "dialect": "",
        "user": "",
        "password": ""
    },
    'sauce_android_apk': 'sauce-storage:aspiration-alpha-android.apk',
    'sauce_ios_ipa': 'sauce-storage:aspiration-alpha-ios.ipa'
}

PROD = {
    "env": "prod",
    "databases": {
        # database configs
    },
    'sauce_android_apk': 'sauce-storage:aspiration-prod-android.apk',
    'sauce_ios_ipa': 'sauce-storage:aspiration-prod-ios.ipa'
}
