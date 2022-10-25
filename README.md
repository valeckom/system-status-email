# System Email

This script is for emailing (Debian distro) Linux system information for passive
monitoring. The registered email address will receive a weekly email containing
basic system and storage information.

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

Run the `install` command and answer the question to configure the script.

```shell
/opt/system_email/system_email install
```

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
<p>Wed Oct 19 23:17:02 2022</p>

<h3>System status</h3>
<table>
    <tr>
        <th>Hostname</th>
        <td>mainserver</td>
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

1. Uninstall script
2. Update script - load the new version and keep the `.env` file
3. Convert `README.md` to `README.txt` for build bundle
4. Add S.M.A.R.T. drive info table
5. Make tables dynamic based on if data exists (hide tables that do not contain data)
6. Be able to display more than 1 drive in "Drive partition status"
7. Make a dashboard section for quick information (&check; or &cross; for features)