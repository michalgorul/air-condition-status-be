# Air condition status

## Setup Virtualenv on Windows

```console
deactivate
rmdir venv
py -3.10 -m pip install --upgrade pip
py -3.10 -m pip install virtualenv
py -3.10 -m virtualenv venv
.\venv\Scripts\activate
.\venv\Scripts\python.exe -m pip install -r .\requirements.txt
```

If any problem with activating venv try: 

```
For Windows 11, Windows 10, Windows 7, Windows 8, Windows Server 2008 R2 or Windows Server 2012, run the following commands as Administrator:

x86 (32 bit)
Open C:\Windows\SysWOW64\cmd.exe
Run the command: powershell Set-ExecutionPolicy RemoteSigned

x64 (64 bit)
Open C:\Windows\system32\cmd.exe
Run the command: powershell Set-ExecutionPolicy RemoteSigned
```

