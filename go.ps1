clear
$rep = 'D:\SAUV_D_2\_OneDrive\'
$rep = 'D:\SAUV_D_2\_OneDrive\.*'
$files =  gci -File -Path $rep -Recurse -Force #List only files

$i = 1
$m=0
foreach ($file in $files) {
	$l=$file.DirectoryName.Length + $file.name.Length
	if($m -lt $l ) {$m = $l}
	Write-Host "$($i)  $($m)  $($l)   $($file.name)"
	# Write-Host "$($i)  $($m)  $($l)  $($file.DirectoryName)\$($file.name)"
	$i++

};
Write-Host "files.Length == $($files.Length)"
