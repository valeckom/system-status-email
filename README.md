# System Email

This script is for emailing (Debian distro) Linux system information for passive
monitoring. The regestered email address will receive a weekly email containing
basic system, along with storage, information.

If there are any issues refer to the `system_email.log` inside `/opt/system_email`.

<!-- TOC -->

* [Script install](#script-install)
    * [Get the files](#get-the-files)
    * [Configure the script](#configure-the-script)
    * [Create cron task](#create-cron-task)
* [Future improvements](#future-improvements)

<!-- TOC -->

## Script install

### Get the files

Download the package into the system

```shell
wget <the url for the system_email.tar.gz in git>
```

Unpack the files into `/opt/`.

```shell
sudo tar -xf system_email.tar.gz -C /opt/
```

### Configure the script

Generate the config file.
*This will end in an error telling you to fill out the `.env` file*

```shell
./opt/system_email/system_email
```

Edit the file to be able to send emails.

```shell
sudo nano /opt/system_email/.env
```

### Create cron task

Create a file `system_email` (with no extension) in `/etc/cron.weekly`. Fill it with the lines below.
*Include a blank line at the end.*

```shell
#!/bin/bash

/opt/system_email/system_email > /opt/system_email/system_email.log

```

## Future improvements

1. Add script version/build-time
2. Add regular drive table
3. Installer script
    - add script to cron.weekly...
    - generate .env with user supplied values
4. Convert README.md to README.txt for build bundle
5. Add S.M.A.R.T. drive info table
6. Make tables dynamic based on if data exists (hide tables that do not contain data)
7. Make a dashboard section for quick information (&check; or &cross; for features)