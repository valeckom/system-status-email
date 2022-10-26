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

<body>
<h3>Main Server's update</h3>

<h3>System status</h3>
<table>
    <tr>
        <th>Hostname</th>
        <td>main server</td>
    </tr>
    <tr>
        <th>Uptime</th>
        <td>6 hours, 8 minutes</td>
    </tr>
    <tr>
        <th>Pending updates</th>
        <td>0</td>
    </tr>
</table>


<h3>Drive partition status</h3>
<table>
    <tr>
        <th>Filesystem</th>
        <td>/dev/sda1</td>
    </tr>
    <tr>
        <th>Size</th>
        <td>457G</td>
    </tr>
    <tr>
        <th>Used</th>
        <td>70G</td>
    </tr>
    <tr>
        <th>Available</th>
        <td>364G</td>
    </tr>
    <tr>
        <th>Use%</th>
        <td>17%</td>
    </tr>
</table>


<h3>ZPool status</h3>
<table>
    <tr>
        <th>Size</th>
        <td>18.1T</td>
    </tr>
    <tr>
        <th>Free space</th>
        <td>3.36T</td>
    </tr>
    <tr>
        <th>Fragmentation</th>
        <td>12%</td>
    </tr>
    <tr>
        <th>Capacity</th>
        <td>81%</td>
    </tr>
    <tr>
        <th>Health</th>
        <td>ONLINE</td>
    </tr>
</table>
</body>

<hr/>

## Future improvements

1. Be able to display more than 1 drive in "Drive partition status"
2. Make a dashboard section for quick information (&check; or &cross; for features)
3. Add S.M.A.R.T. drive info table
