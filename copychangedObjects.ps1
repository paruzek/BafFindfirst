$changedName = git log -1 --name-only
cls
foreach ($file in $changedName){

if ($file.Length -gt 7) {
    if ($file.Substring(0,7) -eq "objects") {
    
        $pref = $file.Substring(8,3)
        $sp = $file.Split("/")
        $dfile = $pref , $sp[2] -join ""
        $dfile = "tomerge", $dfile -join "\"
        
        Copy-Item  $file -Destination $dfile

    }
}

}

#Get-Content *.txt | Set-Content newfile