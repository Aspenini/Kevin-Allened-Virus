; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Gun Game"
#define MyAppVersion "69.69.69"
#define MyAppPublisher "69240 Industries"
#define MyAppURL "www.microsoft.com"
#define MyAppExeName "kevin_apocalypse.exe"
#define MyAppAssocName "KEVIN SAYS TASTEY"
#define MyAppAssocExt ".png .jpg"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{FD302C24-0CFA-49E9-B73C-3EFEE21A42AE}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName=Windows\{#MyAppName}
DisableDirPage=yes
UninstallDisplayIcon={app}\{#MyAppExeName}
; "ArchitecturesAllowed=x64compatible" specifies that Setup cannot run
; on anything but x64 and Windows 11 on Arm.
ArchitecturesAllowed=x64compatible
; "ArchitecturesInstallIn64BitMode=x64compatible" requests that the
; install be done in "64-bit mode" on x64 or Windows 11 on Arm,
; meaning it should use the native 64-bit Program Files directory and
; the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64compatible
ChangesAssociations=yes
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only).
;PrivilegesRequired=lowest
OutputBaseFilename=Gun Game
SetupIconFile=F:\Projects\Kevin-Allened-Virus\icon.ico
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "arabic"; MessagesFile: "compiler:Languages\Arabic.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "F:\Projects\Kevin-Allened-Virus\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\Projects\Kevin-Allened-Virus\alarms.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\Projects\Kevin-Allened-Virus\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\Projects\Kevin-Allened-Virus\kevin_allen.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\Projects\Kevin-Allened-Virus\kevin_apocalypse.pyw"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\Projects\Kevin-Allened-Virus\kevin_supersonic.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\Projects\Kevin-Allened-Virus\kevin_supersonic_with_alarm.mp3"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\Projects\Kevin-Allened-Virus\kevin_theme_compressed.mp3"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

