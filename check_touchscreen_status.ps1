# Recherche du périphérique d'écran tactile
$device = Get-PnpDevice | Where-Object { $_.FriendlyName -match "HID-compliant touch screen" }

if ($device) {
    if ($device.Status -eq "OK") {
        # Si le périphérique est activé
        Write-Output "True"
    } else {
        # Si le périphérique est désactivé
        Write-Output "False"
    }
} else {
    # Si le périphérique n'est pas trouvé
    Write-Output "Périphérique tactile non trouvé."
}
