# meraki-api-pull-logs

Summary:

The Purpose of this script is to pull all logs from all networks within the Organization. Logs will be pulled as far 
back as possible. They will be pulled from three type of devices: appliance, wireless, and switch. Depending on the 
amount of networks and devices in total, this script will take a long time to run. Ensure to run it on a server like 
machine to ensure all logs are successfully saved. Logs will be saved in the same directory where the script is located 
in json format.

Requirements:

1) Interpreter: Python 3.9.0+
2) Python Packages: meraki.
3) API support for the Organization is enabled in Meraki Dashboard. Admins have generated their custom API key.
4) Adequate amount of space, uninterrupted environment, time...

How to run:

1) Open pull_logs.py with your favorite text editor and edit PARAMETERS sections of the script:
    1) Lines 5-6 is mandatory.
    2) Lines 7-8 are optional.
2) Log files will be saved in json format in the same directory from which script was ran.