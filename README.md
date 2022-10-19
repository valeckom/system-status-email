# System Email

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

1. Installer script
    - add script to cron.weekly...
    - generate .env with user supplied values
2. Script version
3. Add regular drive table
4. Add S.M.A.R.T. dive table
5. Make tables dynamic based on if data exists (hide tables that do not contain data)
6. Make a dashboard section for quick information (&check; or &cross; for features)
7. Add script version/build-time