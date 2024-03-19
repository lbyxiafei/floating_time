
This Python application showcases a floating window timer that appears every half-hour (`HH:30`) and hour (`HH:00`), remaining visible for 10 seconds.

![Overview](https://github.com/lbyxiafei/floating_time/blob/main/img/overview.png)

# Install on Windows

Requirements: `python >= 3.9`. Install application and dependencies:

```bash
pip install schedule floatingtime
```

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

# Install on Mac

> To be added...
