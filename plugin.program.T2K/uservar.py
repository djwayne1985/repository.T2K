import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'T2K'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'https://'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE        = 'https://'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = '[COLORaqua]YouTube Help & Build Videos[/COLOR]'
YOUTUBEFILE    = 'https://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'https://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'https://'
# Text file for roms and emus
ROMPACK        = 'https://'
EMUAPKS        = 'https://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://'
ICONMAINT      = 'https://'
ICONSPEED      = 'https://'
ICONAPK        = 'https://'
ICONRETRO      = 'https://'
ICONADDONS     = 'https://'
ICONYOUTUBE    = 'https://'
ICONSAVE       = 'https://'
ICONTRAKT      = 'https://'
ICONREAL       = 'https://'
ICONLOGIN      = 'https://'
ICONCONTACT    = 'https://'
ICONSETTINGS   = 'https://'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'dodgerblue'
COLOR2         = 'white'
COLOR3         = 'snow'
COLOR4         = 'orange'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']T2K[/COLOR])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+'][B]Current Build:[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+'][B]Current Theme:[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Advanced Settings    / %s is the menu item and is required
THEME6         = '[COLOR '+COLOR3+'][B]%s[/COLOR][/B]'
# Advanced Settings    / %s is the menu item and is required
THEME7         = '[COLOR '+COLOR5+'][B]%s[/COLOR][/B]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing T2K.\r\n\r\nContact us on facebook at https://www.facebook.com/groups/T.2.K.Support/'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://'
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'https://'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.T2K'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://'
# Url to folder zip is located in
REPOZIPURL     = 'https://'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'T2K'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = 'https://'
#########################################################