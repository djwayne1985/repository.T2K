import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'T2K'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'https://www.t2k-cloud.co.uk/Kodi/t2k/T2Kautobuilds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE        = 'https://www.t2k-cloud.co.uk/Kodi/mainapk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'YouTube Help Videos'
YOUTUBEFILE    = 'http://'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'https://www.t2k-cloud.co.uk/Kodi/addons2.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'
# Text file for roms and emus
ROMPACK        = 'https://www.t2k-cloud.co.uk/Kodi/t2k/rom-sets.txt'
EMUAPKS        = 'https://www.t2k-cloud.co.uk/Kodi/t2k/emulators.txt'

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
ICONBUILDS     = 'https://www.t2k-cloud.co.uk/Kodi/icons/builds.png'
ICONMAINT      = 'https://www.t2k-cloud.co.uk/Kodi/icons/SEO_Maintenance-512.png'
ICONSPEED      = 'https://www.t2k-cloud.co.uk/Kodi/icons/speedtest.png'
ICONAPK        = 'https://www.t2k-cloud.co.uk/Kodi/icons/71620be831143de5b84ce55e00046028_icon.png'
ICONRETRO      = 'https://www.t2k-cloud.co.uk/Kodi/icons/17bb3b544a5fea0ba7825ce9dbeca6b6_icon.png'
ICONADDONS     = 'https://www.t2k-cloud.co.uk/Kodi/icons/addoninstaller.png'
ICONYOUTUBE    = 'https://www.t2k-cloud.co.uk/Kodi/icons/logo-941916_960_720.png'
ICONSAVE       = 'https://www.t2k-cloud.co.uk/Kodi/icons/538720-disk_512x512.png'
ICONTRAKT      = 'https://www.t2k-cloud.co.uk/Kodi/icons/RvHrUFj.png'
ICONREAL       = 'https://www.t2k-cloud.co.uk/Kodi/icons/realdebridlogo-e1418577058209.png'
ICONLOGIN      = 'https://www.t2k-cloud.co.uk/Kodi/icons/login-system-icon-13.png'
ICONCONTACT    = 'https://www.t2k-cloud.co.uk/Kodi/icons/Contacts-icon.png'
ICONSETTINGS   = 'https://www.t2k-cloud.co.uk/Kodi/icons/iconlicious-misc-settings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'dodgerblue'
COLOR2         = 'white'
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

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing T2K.\r\n\r\nContact us on facebook at https://www.facebook.com/groups/T.2.K.Support/'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'https://www.t2k-cloud.co.uk/Kodi/icons/192x192.png'
CONTACTFANART  = 'http://'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'https://www.t2k-cloud.co.uk/Kodi/t2k/T2Kautobuilds.txt'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.T2K'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://github.com/djwayne1985/repository.T2K/blob/master/zips/addons.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://github.com/djwayne1985/repository.T2K/tree/master/zips/repository.T2K'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'https://www.t2k-cloud.co.uk/Kodi/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'T2K'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = 'https://c1.staticflickr.com/1/368/19491507489_bc92baf89b_b.jpg'
#########################################################