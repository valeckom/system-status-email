# System Email

This script is for emailing (Debian distro) Linux system information for passive
monitoring. The registered email address will receive a weekly email containing
basic system, along with storage, information.

If there are any issues refer to the `system_email.log` inside `/opt/system_email`.

<!-- TOC -->

* [Script install](#script-install)
    * [Get the files](#get-the-files)
    * [Configure the script](#configure-the-script)
        * [Example .env file](#example-env-file)
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

#### Example .env file

The file will look like the following when done *but with your values*.

```text
EMAIL_FROM_ADDRESS=myaddress@provider.com
EMAIL_PASSWORD=dbabdszdkxvpfkdc
EMAIL_TO_ADDRESS=youraddress@provider.com
```

### Create cron task

Create a file `system_email` (with no extension) in `/etc/cron.weekly`.

```shell
sudo nano /etc/cron.weekly/system_email
```

Fill it with the lines below. This will run the script and log any print
statements or errors to the log `system_email.log` in the installation dir
`/opt/system_email`.
*Include a blank line at the end of the file.*

```shell
#!/bin/bash

/opt/system_email/system_email > /opt/system_email/system_email.log

```

Make it executable.

```shell
sudo chmod +x /etc/cron.weekly/system_email
```

## Future improvements

1. Add script version/build-time/build-number
2. Add regular drive table
3. Installer script
    - add script to `/etc/cron.weekly`
    - generate `.env` with user supplied values
4. Convert `README.md` to `README.txt` for build bundle
5. Add S.M.A.R.T. drive info table
6. Make tables dynamic based on if data exists (hide tables that do not contain data)
7. Make a dashboard section for quick information (&check; or &cross; for features)