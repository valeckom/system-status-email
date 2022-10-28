# System Email

This script is for emailing (Debian distro) Linux system information for passive
monitoring. The registered email address will receive a periodic email containing
basic system and storage information. You can see an example email
[here](#email-example).

If there are any issues the debug log is the `system_email.log` inside
`/opt/system_email`.

<!-- TOC -->

* [Script install](#script-install)
    * [Get the files](#get-the-files)
    * [Configure the script](#configure-the-script)
* [Usage](#usage)
    * [Options](#options)
        * [`--dry-run`](#--dry-run)
        * [`-v, --version`](#-v---version)
        * [`-h, --help`](#-h---help)
    * [Commands](#commands)
        * [`install`](#install)
        * [`run`](#run)
        * [`uninstall`](#uninstall)
* [Email example](#email-example)
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

Check that the script works by printing its version.

```shell
/opt/system_email/system_email --version
```

### Configure the script

Run the [`install`](#install) command and answer the prompts to configure the script.
*This must be run with elevated permissions to modify cron system files.*

```shell
sudo /opt/system_email/system_email install
```

#### Install prompts

If you want to change any of these values in the future re-run the
[`install`](#install) command.

1. Enter the email address that will be sending the email
2. Enter the email account password
3. Enter the email address that you want the email to go to
4. How often do you want to send emails? *"Hourly", "Daily", etc...* The default
   is "Weekly".

## Usage

```shell
system_email [OPTIONS] COMMAND
```

### Options

#### `--dry-run`

Run the script without sending an email or creating files.

#### `-v, --version`

Show the version and exit.

#### `-h, --help`

Show the help message and exit.

### Commands

#### `install`

Set up the script and add it to `cron.weekly`.

#### `run`

Read the system information and send an email.

#### `uninstall`

Remove the script's system integration.

## Email example

> <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd"><html lang="en"><head><title>System Status</title><meta content="date=no" name="format-detection"/><meta content="telephone=no" name="format-detection"/><meta content="width=device-width, initial-scale=1" name="viewport"><style type="text/CSS"></style></meta></head><head><title></title><style type="text/css">body {font-family: Roboto, Arial, sans-serif;padding: 1rem;}table {border-collapse: collapse;margin-bottom: 3rem;width: 100%;}tr {border-bottom: 1px solid;}td, th {text-align: left;padding: .5rem;}</style></head><body><h2 style="color: #424242">Workstation's update</h2><div style="color: #424242"><h3>System status</h3><table><tr><th>Hostname</th><td>workstation</td></tr><tr><th>Uptime</th><td>4 hours, 42 minutes</td></tr><tr><th>Pending upgrades</th><td>1</td></tr></table></div><div style="color: #424242"><h3>Drive partition status</h3><table><tr><th>Filesystem</th><td>/dev/sda1</td><td>/dev/sdb1</td></tr><tr><th>Size</th><td>1.6G</td><td>7.8G</td></tr><tr><th>Used</th><td>1.5M</td><td>66M</td></tr><tr><th>Available</th><td>1.6G</td><td>7.8G</td></tr><tr><th>Use%</th><td>1%</td><td>1%</td></tr></table><h3>ZPool status</h3><table><tr><th>Size</th><td>18.1T</td></tr><tr><th>Free space</th><td>3.36T</td></tr><tr><th>Fragmentation</th><td>12%</td></tr><tr><th>Capacity</th><td>81%</td></tr><tr><th>Health</th><td>ONLINE</td></tr></table></div></body></html>

## Future improvements

1. Make a dashboard section for quick information (&check; or &cross; for features)
2. Add S.M.A.R.T. drive info table
