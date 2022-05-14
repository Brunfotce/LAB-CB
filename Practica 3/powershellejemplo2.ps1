function writeMessage {
    [CmdLetBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 1, HelpMessage = "The message to write")]
        [string]$Message
    )

    begin {
        Write-Verbose "INICIANDO SCRIPT"
        if (($null -eq $Message) -or ($Message -eq "")) {
            throw "Message cannot be empty";
        }
    }

    process {
        Write-Host "Message: $message"
    }

    end {
        Write-Host "FIN DEL SCRIPT"
    }
}

writeMessage "Saludos internatuta...o mejor dichoprofe xd" -Verbose