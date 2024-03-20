
This Python application showcases a floating window timer that appears every half-hour (`HH:30`) and hour (`HH:00`), remaining visible for 10 seconds.

Windows:
![Windows](https://github.com/lbyxiafei/floating_time/blob/main/img/overview.png)

Mac:
![Mac](https://github.com/lbyxiafei/floating_time/blob/main/img/overview_mac.jpg)

# Installations

Prerequisites: `python >= 3.9`. Install python packages:

```bash
pip install floatingtime, schedule
```

## Windows

Create a Powershell script, `floatingtime.ps1`:

```ps
python -m floatingtime.main
```

Open Task Scheduler:
- Press `Win + R` to open the "Run" dialog.
- Type `taskschd.msc` and press Enter to open Task Scheduler.
Create a new task:
- In Task Scheduler, click on "Create Task..." in the right-hand Actions pane.
- Click on the "Triggers" tab and then "New".
Actions Tab:
- Click on the "Actions" tab and then "New".
- For the action, select "Start a program".
- In the "Program/script" field, enter `powershell.exe`.
- In the "Add arguments (optional)" field, enter the following:

```ps
-ExecutionPolicy Bypass -WindowStyle Hidden -File "C:\path\to\your\script\myscript.ps1"
```

Replace `"C:\path\to\your\script\myscript.ps1"` with the actual path to your PowerShell script(`floatingtime.ps1`).

Save and restart the computer, all set.

## Mac

Create a py script, `floatingtime_run.py`:

```python
from floatingtime import run_test, run_period

run_period()
```

Create a plist file: `~/Library/LaunchAgents/com.user.floatingtime.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.floatingtime</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/python/bin/python3</string>
        <string>/path/to/py/script/floatingtime_run.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StartInterval</key>
    <integer>10</integer>
    <key>StandardOutPath</key>
    <string>/path/to/log/logfile_stdout.log</string>
    <key>StandardErrorPath</key>
    <string>/path/to/log/logfile_stderr.log</string>
</dict>
</plist>
```

Save, and run following bash command:

```bash
launchctl load ~/Library/LaunchAgents/com.user.floatingtime.plist
```

You are all set.

# Contact

lbyxiafei@gmail.com