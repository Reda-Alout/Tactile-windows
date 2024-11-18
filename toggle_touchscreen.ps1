$device = Get-PnpDevice | Where-Object { $_.FriendlyName -match "HID-compliant touch screen" }
if ($device) {
    if ($device.Status -eq "OK") {
        Disable-PnpDevice -InstanceId $device.InstanceId -Confirm:$false
        Write-Output "Écran tactile désactivé."
    } else {
        Enable-PnpDevice -InstanceId $device.InstanceId -Confirm:$false
        Write-Output "Écran tactile activé."
    }
} else {
    Write-Output "Périphérique tactile non trouvé."
}
