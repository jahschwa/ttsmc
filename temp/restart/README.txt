Files:

  /etc/systemd/system/minecraft.service

    Runs minecraft inside a screen session to allow access to the console.

  /root/cron/minecraft-auto-restart

    Checks for the existence of a flag file, then uses mcstatus to query
    online players, and finally restarts the server via the screen console.

  /root/cron/minecraft-upkeep-restart

    Restart once a week by invoking `minecraft restart` via below file.

  /usr/local/bin/minecraft

    Control script for minecraft, knows hot to execute commands on the
    minecraft console which is running in a screen session.

Crons:

  Add entries from crontab.root

Additional:

  python3 -m pip install mcstatus
  
