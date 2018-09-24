#!/usr/bin/env python
############################################################################
#                             /T /I                                        #
#                              / |/ | .-~/                                 #
#                          T\ Y  I  |/  /  _                               #
#         /T               | \I  |  I  Y.-~/                               #
#        I l   /I       T\ |  |  l  |  T  /                                #
#     T\ |  \ Y l  /T   | \I  l   \ `  l Y                                 #
# __  | \l   \l  \I l __l  l   \   `  _. |                                 #
# \ ~-l  `\   `\  \  \ ~\  \   `. .-~   |                                  #
#  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |                                 #
#.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./                                 #
# >--.  ~-.   ._  ~>-"    "\   7   7   ]                                   #
#^.___~"--._    ~-{  .-~ .  `\ Y . /    |                                  #
# <__ ~"-.  ~       /_/   \   \I  Y   : |                                  #
#   ^-.__           ~(_/   \   >._:   | l______                            #
#       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.                        #
#              (_/ .  ~(   /'     "~"--,Y   -=b-. _)                       #
#               (_/ .  \  Fire TV Guru/ l      c"~o \                      #
#                \ /    `.    .     .^   \_.-~"~--.  )                     #
#                 (_/ .   `  /     /       !       )/                      #
#                  / / _.   '.   .':      /        '                       #
#                  ~(_/ .   /    _  `  .-<_                                #
#                    /_/ . ' .-~" `.  / \  \          ,z=.                 #
#                    ~( /   '  :   | K   "-.~-.______//                    #
#                      "-,.    l   I/ \_    __{--->._(==.                  #
#                       //(     \  <    ~"~"     //                        #
#                      /' /\     \  \     ,v=.  ((                         #
#                    .^. / /\     "  }__ //===-  `                         #
#                   / / ' '  "-.,__ {---(==-                               #
#                 .^ '       :  T  ~"   ll                                 #
#                / .  .  . : | :!        \                                 #
#               (_/  /   | | j-"          ~^                               #
#                 ~-<_(_.^-~"                                              #
#                                                                          #
#   Copyright (C) 2014-2016 Matt Martz                                     #
#                                                                          #
#                      original speedtest-cli DEV                          #
#            Matt Martz (https://github.com/sivel/speedtest-cli)           #
#                                                                          #
#             Credits to : Josh.5 for the original kodi layout             #
#                                                                          #
#     Updated layout, fixed errors and cleaned up code: Fire TV Guru       #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License"); you may  #
# not use this file except in compliance with the License. You may obtain  #
# a copy of the License at                                                 #
#                                                                          #
#      http://www.apache.org/licenses/LICENSE-2.0                          #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,WITHOUT #
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the #
# License for the specific language governing permissions and limitations  #
# under the License.                                                       #
############################################################################
if 64 - 64: FGGFTFFTFF
import xbmc
import xbmcgui
import xbmcaddon
import os
import re
import sys
import math
import signal
import socket
import timeit
import platform
import threading
import time
import uuid
if 65 - 65: tg / FTFFGTGGTGTTG % tffffffftt - FGTTF
if 73 - 73: TTGGGFFFF
try :
 import xml . etree . cElementTree as ET
 from xml . dom import minidom as DOM
except ImportError :
 try :
  import xml . etree . ElementTree as ET
 except ImportError :
  from xml . dom import minidom as DOM
  if 22 - 22: TGTFFT * tfgtff / tftgtgg . tftfttgg . fgfttfgtgtff / TGFFGGFTFGGF
  ET = None
  if 48 - 48: ftgf / ttffttf / TGGF / TFGT
TFFTTTGGGFT = 'script.T2K'
TFTT = xbmcaddon . Addon ( TFFTTTGGGFT )
__version__ = '0.3.5'
FTGTFGGGGGFTF = None
FGFGTT = None
tgffgttg = socket . socket
TGFGFFTG = ( 'Mozilla/5.0' , '(%s; U; %s; en-us)'
 % ( platform . system ( ) , platform . architecture ( ) [ 0 ] ) ,
 'Python/%s' % platform . python_version ( ) ,
 '(KHTML, like Gecko)' , 'speedtest-cli/%s' % __version__ )
FFTTTTTGFGFT = ' ' . join ( TGFGFFTG )
if 68 - 68: fggfffg / tfggtg
try :
 import xml . etree . cElementTree as ET
 from xml . dom import minidom as DOM
except ImportError :
 try :
  import xml . etree . ElementTree as ET
 except ImportError :
  from xml . dom import minidom as DOM
  if 66 - 66: fgffftftg
  ET = None
  if 21 - 21: TFTFFGTFGTTF / tfggtg . fgfttfgtgtff * fggfffg
try :
 from urllib2 import urlopen , Request , HTTPError , URLError
except ImportError :
 from urllib . request import urlopen , Request , HTTPError , URLError
 if 59 - 59: FTFFGTGGTGTTG
try :
 from httplib import HTTPConnection , HTTPSConnection
except ImportError :
 from http . client import HTTPConnection , HTTPSConnection
 if 31 - 31: tfggtg % FGTTF * FTFFGTGGTGTTG / tfggtg % ftgf + tffffffftt
try :
 from Queue import Queue
except ImportError :
 from queue import Queue
 if 93 - 93: fggfffg * FGGFTFFTFF * TGTFFT % fggfffg * fggfffg * TTGGGFFFF
try :
 from urlparse import urlparse
except ImportError :
 from urllib . parse import urlparse
 if 79 - 79: tfggtg
try :
 from urlparse import parse_qs
except ImportError :
 try :
  from urllib . parse import parse_qs
 except ImportError :
  from cgi import parse_qs
  if 86 - 86: tftfttgg % TGTFFT
try :
 from hashlib import md5
except ImportError :
 from md5 import md5
 if 80 - 80: tffffffftt . TGTFFT
try :
 from argparse import ArgumentParser as ArgParser
except ImportError :
 from optparse import OptionParser as ArgParser
 if 87 - 87: ftgf / TFTFFGTFGTTF + fgffftftg - TFTFFGTFGTTF . TFTFFGTFGTTF / TTGGGFFFF
try :
 import builtins
except ImportError :
 def FFTTTTFGFG ( * args , ** kwargs ) :
  tgtftffggf = kwargs . pop ( 'file' , sys . stdout )
  if tgtftffggf is None :
   return
   if 31 - 31: TTGGGFFFF + tftgtgg . fgffftftg
  def tftfftttt ( data ) :
   if not isinstance ( data , basestring ) :
    data = str ( data )
   tgtftffggf . write ( data )
   if 45 - 45: fgffftftg + TFGT
  FTTGGGFF = False
  FGFTTFG = kwargs . pop ( 'sep' , None )
  if FGFTTFG is not None :
   if isinstance ( FGFTTFG , unicode ) :
    FTTGGGFF = True
   elif not isinstance ( FGFTTFG , str ) :
    raise TypeError ( 'sep must be None or a string' )
  FFGGFTFGT = kwargs . pop ( 'end' , None )
  if FFGGFTFGT is not None :
   if isinstance ( FFGGFTFGT , unicode ) :
    FTTGGGFF = True
   elif not isinstance ( FFGGFTFGT , str ) :
    raise TypeError ( 'end must be None or a string' )
  if kwargs :
   raise TypeError ( 'invalid keyword arguments to print()' )
  if not FTTGGGFF :
   for FTGGGTGGTGTG in args :
    if isinstance ( FTGGGTGGTGTG , unicode ) :
     FTTGGGFF = True
     break
  if FTTGGGFF :
   ttfftgttff = unicode ( '\n' )
   FTFFG = unicode ( ' ' )
  else :
   ttfftgttff = '\n'
   FTFFG = ' '
  if FGFTTFG is None :
   FGFTTFG = FTFFG
  if FFGGFTFGT is None :
   FFGGFTFGT = ttfftgttff
  for ( fttftg , FTGGGTGGTGTG ) in enumerate ( args ) :
   if fttftg :
    tftfftttt ( FGFTTFG )
   tftfftttt ( FTGGGTGGTGTG )
  tftfftttt ( FFGGFTFGT )
else :
 FFTTTTFGFG = getattr ( builtins , 'print' )
 del builtins
 if 59 - 59: TFGT * FGGFTFFTFF + TFGT + TFTFFGTFGTTF * tftgtgg
class tfftftgtf ( Exception ) :
 if 47 - 47: ftgf
 if 3 - 3: FGGFTFFTFF - FTFFGTGGTGTTG - tftfttgg
 if 6 - 6: TGTFFT / tfgtff % TFGT
def ff ( * args , ** kwargs ) :
 if 54 - 54: ttffttf + ttffttf % fgffftftg % FGGFTFFTFF / FTFFGTGGTGTTG . ttffttf
 global FTGTFGGGGGFTF
 fgftgfggff = tgffgttg ( * args , ** kwargs )
 fgftgfggff . bind ( ( FTGTFGGGGGFTF , 0 ) )
 return fgftgfggff
 if 32 - 32: tfgtff * tg % ftgf % TFGT . tfggtg
def fgtttttggfgtg ( origin , destination ) :
 ( fgfgtttgfg , fftttfgffgtg ) = origin
 ( fg , TGGTTGF ) = destination
 TTTTT = 6371
 if 75 - 75: TTGGGFFFF % TTGGGFFFF
 FTG = math . radians ( fg - fgfgtttgfg )
 FGGTFFF = math . radians ( TGGTTGF - fftttfgffgtg )
 FT = math . sin ( FTG / 2 ) * math . sin ( FTG / 2 ) + math . cos ( math . radians ( fgfgtttgfg ) ) * math . cos ( math . radians ( fg ) ) * math . sin ( FGGTFFF / 2 ) * math . sin ( FGGTFFF / 2 )
 if 28 - 28: ttffttf - tfggtg . tfggtg + tftfttgg - tffffffftt + tg
 if 95 - 95: tftgtgg % ftgf . tg
 TGFGT = 2 * math . atan2 ( math . sqrt ( FT ) , math . sqrt ( 1 - FT ) )
 fttggftt = TTTTT * TGFGT
 if 75 - 75: FGTTF / tffffffftt - tg / tftfttgg . TTGGGFFFF - FGTTF
 return fttggftt
 if 71 - 71: ttffttf + TFGT * ttffttf - tftgtgg * fgfttfgtgtff
def tfffgtffggg ( url , data = None , headers = { } ) :
 if url [ 0 ] == ':' :
  ffFFGGT = '%s%s' % ( scheme , url )
 else :
  ffFFGGT = url
 headers [ 'User-Agent' ] = FFTTTTTGFGFT
 return Request ( ffFFGGT , data = data , headers = headers )
 if 96 - 96: TTGGGFFFF % TFGT . ttffttf + tffffffftt * ftgf - tftfttgg
def FGGFG ( request ) :
 try :
  TTTFFGTTGTT = urlopen ( request )
  return TTTFFGTTGTT
 except ( HTTPError , URLError , socket . error ) :
  FGTGFT = sys . exc_info ( ) [ 1 ]
  return ( None , FGTGFT )
  if 93 - 93: FTFFGTGGTGTTG % ftgf * FGTTF
class TFGGTFGT ( threading . Thread ) :
 if 72 - 72: fggfffg / FGTTF * tfgtff - fgffftftg
 def __init__ ( self , url , start ) :
  self . url = url
  self . result = None
  self . starttime = start
  threading . Thread . __init__ ( self )
  if 51 - 51: TTGGGFFFF * tftgtgg % fgfttfgtgtff * TTGGGFFFF % TGFFGGFTFGGF / TFTFFGTFGTTF
 def run ( self ) :
  self . result = [ 0 ]
  try :
   if timeit . default_timer ( ) - self . starttime <= 10 :
    FTTTTFFG = tfffgtffggg ( self . url )
    ffgggttggtf = urlopen ( FTTTTFFG )
    while 1 and not FGFGTT . isSet ( ) :
     self . result . append ( len ( ffgggttggtf . read ( 10240 ) ) )
     if self . result [ - 1 ] == 0 :
      break
    ffgggttggtf . close ( )
  except IOError :
   pass
   if 51 - 51: tfggtg * fgfttfgtgtff + TGGF + tftgtgg
class fgtgtgg ( threading . Thread ) :
 if 86 - 86: TGGF / tfggtg % FGGFTFFTFF
 def __init__ (
 self ,
 url ,
 start ,
 size ,
 ) :
  self . url = url
  TGGTFTGTGGFGF = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  FTGFFGTF = TGGTFTGTGGFGF * int ( round ( int ( size ) / 36.0 ) )
  self . data = ( 'content1=%s' % FTGFFGTF [ 0 : int ( size ) - 9 ] ) . encode ( )
  del FTGFFGTF
  self . result = None
  self . starttime = start
  threading . Thread . __init__ ( self )
  if 92 - 92: tftfttgg
 def run ( self ) :
  try :
   if timeit . default_timer ( ) - self . starttime <= 10 and not FGFGTT . isSet ( ) :
    if 26 - 26: fggfffg . fgffftftg
    FTTTTFFG = tfffgtffggg ( self . url , data = self . data )
    ffgggttggtf = urlopen ( FTTTTFFG )
    ffgggttggtf . read ( 11 )
    ffgggttggtf . close ( )
    self . result = len ( self . data )
   else :
    self . result = 0
  except IOError :
   self . result = 0
   if 68 - 68: tftgtgg
def TTFGFTTFT ( dom , tagName ) :
 tgtft = dom . getElementsByTagName ( tagName ) [ 0 ]
 return dict ( list ( tgtft . attributes . items ( ) ) )
 if 69 - 69: ftgf . fgffftftg + TFGT / tfgtff - ftgf
def ttgtgtfttg ( ) :
 FTTTTFFG = tfffgtffggg ( 'http://www.speedtest.net/speedtest-config.php' )
 if 10 - 10: tffffffftt % FTFFGTGGTGTTG
 TTTFFGTTGTT = FGGFG ( FTTTTFFG )
 if TTTFFGTTGTT is False :
  FFTTTTFGFG ( 'Could not retrieve speedtest.net configuration: %s' % e )
  sys . exit ( 1 )
 tggfgtgg = [ ]
 while 1 :
  tggfgtgg . append ( TTTFFGTTGTT . read ( 10240 ) )
  if len ( tggfgtgg [ - 1 ] ) == 0 :
   break
 if int ( TTTFFGTTGTT . code ) != 200 :
  return None
 TTTFFGTTGTT . close ( )
 try :
  try :
   FFGGGGGGTGFTT = ET . fromstring ( '' . encode ( ) . join ( tggfgtgg ) )
   tggfffgtg = {
 'client' : FFGGGGGGTGFTT . find ( 'client' ) . attrib ,
 'times' : FFGGGGGGTGFTT . find ( 'times' ) . attrib ,
 'download' : FFGGGGGGTGFTT . find ( 'download' ) . attrib ,
 'upload' : FFGGGGGGTGFTT . find ( 'upload' ) . attrib ,
 }
  except Exception :
   if 23 - 23: fggfffg
   if 91 - 91: FTFFGTGGTGTTG + fgffftftg
   if 31 - 31: tfggtg . tftfttgg . ttffttf
   FFGGGGGGTGFTT = DOM . parseString ( '' . join ( tggfgtgg ) )
   tggfffgtg = {
 'client' : TTFGFTTFT ( FFGGGGGGTGFTT , 'client' ) ,
 'times' : TTFGFTTFT ( FFGGGGGGTGFTT , 'times' ) ,
 'download' : TTFGFTTFT ( FFGGGGGGTGFTT , 'download' ) ,
 'upload' : TTFGFTTFT ( FFGGGGGGTGFTT , 'upload' ) ,
 }
 except SyntaxError :
  FFTTTTFGFG ( 'Failed to parse speedtest.net configuration' )
  sys . exit ( 1 )
 del FFGGGGGGTGFTT
 del tggfgtgg
 return tggfffgtg
 if 75 - 75: TGGF + tftgtgg . tftfttgg . TFTFFGTFGTTF + tfgtff . tftgtgg
 if 96 - 96: ttffttf . TFTFFGTFGTTF - tfgtff + FTFFGTGGTGTTG / tftfttgg * ttffttf
def tgFFGFFGFF ( client , all = False ) :
 if 91 - 91: tfggtg
 FFTFF = [
 'https://www.speedtest.net/speedtest-servers-static.php' ,
 'http://c.speedtest.net/speedtest-servers-static.php' ,
 ]
 fffgt = [ ]
 ftftgfggttg = { }
 for FGTGFF in FFTFF :
  try :
   FTTTTFFG = tfffgtffggg ( FGTGFF )
   TTTFFGTTGTT = FGGFG ( FTTTTFFG )
   if TTTFFGTTGTT is False :
    fffgt . append ( '%s' % e )
    raise tfftftgtf
   fttfg = [ ]
   while 1 :
    fttfg . append ( TTTFFGTTGTT . read ( 10240 ) )
    if len ( fttfg [ - 1 ] ) == 0 :
     break
   if int ( TTTFFGTTGTT . code ) != 200 :
    TTTFFGTTGTT . close ( )
    raise tfftftgtf
   TTTFFGTTGTT . close ( )
   try :
    try :
     FFGGGGGGTGFTT = ET . fromstring ( '' . encode ( ) . join ( fttfg ) )
     ffggtggft = FFGGGGGGTGFTT . getiterator ( 'server' )
    except Exception :
     if 23 - 23: tftgtgg + tftgtgg . ttffttf
     if 38 - 38: fgffftftg
     if 7 - 7: tg . fggfffg % TGFFGGFTFGGF - TGTFFT - FTFFGTGGTGTTG
     FFGGGGGGTGFTT = DOM . parseString ( '' . join ( fttfg ) )
     ffggtggft = FFGGGGGGTGFTT . getElementsByTagName ( 'server' )
   except SyntaxError :
    raise tfftftgtf
   for TGGGTTTFTFF in ffggtggft :
    try :
     ftggggttfgg = TGGGTTTFTFF . attrib
    except AttributeError :
     ftggggttfgg = dict ( list ( TGGGTTTFTFF . attributes . items ( ) ) )
    fttggftt = fgtttttggfgtg ( [ float ( client [ 'lat' ] ) , float ( client [ 'lon'
 ] ) ] , [ float ( ftggggttfgg . get ( 'lat' ) ) ,
 float ( ftggggttfgg . get ( 'lon' ) ) ] )
    ftggggttfgg [ 'd' ] = fttggftt
    if fttggftt not in ftftgfggttg :
     ftftgfggttg [ fttggftt ] = [ ftggggttfgg ]
    else :
     ftftgfggttg [ fttggftt ] . append ( ftggggttfgg )
   del FFGGGGGGTGFTT
   del fttfg
   del ffggtggft
  except tfftftgtf :
   continue
  if ftftgfggttg :
   break
 if not ftftgfggttg :
  FFTTTTFGFG ( '''Failed to retrieve list of speedtest.net servers:
%s'''
 % '\n' . join ( fffgt ) )
  sys . exit ( 1 )
 FFTFGTTFTF = [ ]
 for fttggftt in sorted ( ftftgfggttg . keys ( ) ) :
  for fttggtf in ftftgfggttg [ fttggftt ] :
   FFTFGTTFTF . append ( fttggtf )
   if len ( FFTFGTTFTF ) == 5 and not all :
    break
  else :
   continue
  break
 del ftftgfggttg
 return FFTFGTTFTF
 if 6 - 6: ftgf
 if 68 - 68: tftfttgg - tftgtgg
def TTF ( servers ) :
 ffttffffff = { }
 for TGGGTTTFTFF in servers :
  TTGT = [ ]
  FGTGFF = '%s/latency.txt' % os . path . dirname ( TGGGTTTFTFF [ 'url' ] )
  tgFGTTGTFFFGTGG = urlparse ( FGTGFF )
  for fttftg in range ( 0 , 3 ) :
   try :
    if tgFGTTGTFFFGTGG [ 0 ] == 'https' :
     TTTT = HTTPSConnection ( tgFGTTGTFFFGTGG [ 1 ] )
    else :
     TTTT = HTTPConnection ( tgFGTTGTFFFGTGG [ 1 ] )
    FFTFT = { 'User-Agent' : FFTTTTTGFGFT }
    fggffftgtf = timeit . default_timer ( )
    TTTT . request ( 'GET' , tgFGTTGTFFFGTGG [ 2 ] , headers = FFTFT )
    fgtgtttgtff = TTTT . getresponse ( )
    FFTFTTG = timeit . default_timer ( ) - fggffftgtf
   except ( HTTPError , URLError , socket . error ) :
    TTGT . append ( 3600 )
    continue
   tttggtgt = fgtgtttgtff . read ( 9 )
   if int ( fgtgtttgtff . status ) == 200 and tttggtgt == 'test=test' . encode ( ) :
    TTGT . append ( FFTFTTG )
   else :
    TTGT . append ( 3600 )
   TTTT . close ( )
  FFF = round ( sum ( TTGT ) / 6 * 1000 , 3 )
  ffttffffff [ FFF ] = TGGGTTTFTFF
 ftfftttftf = sorted ( ffttffffff . keys ( ) ) [ 0 ]
 FGTFFGFGT = ffttffffff [ ftfftttftf ]
 FGTFFGFGT [ 'latency' ] = ftfftttftf
 return FGTFFGFGT
 if 91 - 91: TGFFGGFTFGGF + TGTFFT . ttffttf * TGFFGGFTFGGF + TGTFFT * tfgtff
class tgggtttttf ( xbmcgui . WindowXMLDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  xbmcgui . WindowXMLDialog . __init__ ( self , * args , ** kwargs )
  self . doModal ( )
  if 22 - 22: FGTTF + tg . FTFFGTGGTGTTG * fggfffg % FGGFTFFTFF * TGTFFT
 def onInit ( self ) :
  self . testRun = False
  if 77 - 77: tfgtff
  self . screenx = 1920
  self . screeny = 1080
  if 17 - 17: fggfffg % tftgtgg . ttffttf + tftgtgg / TTGGGFFFF
  self . image_dir = xbmc . translatePath ( os . path . join ( TFTT . getAddonInfo ( 'path' ) , 'resources' , 'skins' , 'Default' , 'media' ) )
  self . image_background = self . image_dir + '/bg_screen.jpg'
  self . image_shadow = self . image_dir + '/shadowframe.png'
  self . image_progress = self . image_dir + '/ajax-loader-bar.gif'
  self . image_ping = self . image_dir + '/ping_progress_bg.png'
  self . image_ping_glow = self . image_dir + '/ping_progress_glow.png'
  self . image_gauge = self . image_dir + '/gauge_bg.png'
  self . image_gauge_arrow = self . image_dir + '/gauge_ic_arrow.png'
  self . image_button_run = self . image_dir + '/btn_start_bg.png'
  self . image_button_run_glow = self . image_dir + '/btn_start_glow_active.png'
  self . image_speedtestresults = self . image_dir + '/speedtest_results_wtext.png'
  self . image_centertext_testingping = self . image_dir + '/testing_ping.png'
  self . rec_speedpic = self . image_dir + '/recspeed.png'
  self . image_result = self . image_speedtestresults
  if 75 - 75: TGTFFT - tftfttgg % fggfffg
  self . textbox = xbmcgui . ControlTextBox ( 50 , 50 , 880 , 500 , textColor = '0xFFFFFFFF' )
  self . addControl ( self . textbox )
  self . displayButtonRun ( )
  self . displayButtonClose ( )
  self . setFocus ( self . button_run )
  if 37 - 37: tftfttgg * tfgtff / TFTFFGTFGTTF - fggfffg % TTGGGFFFF . ftgf
  if 88 - 88: fggfffg . TTGGGFFFF * TTGGGFFFF % fgffftftg
 def onAction ( self , action ) :
  if action == 10 or action == 92 :
   self . saveClose ( )
   if 15 - 15: FGTTF * TGTFFT + FGGFTFFTFF
 def displayButtonRun ( self , function = "true" ) :
  if ( function == "true" ) :
   TGTF = ( self . screenx / 3 ) - ( 300 / 2 )
   tgffggfgt = ( self . screeny / 3 ) - ( 122 / 2 ) + 50
   if 1 - 1: TTGGGFFFF
   self . button_run_glow = xbmcgui . ControlImage ( TGTF , tgffggfgt , 300 , 122 , '' , aspectRatio = 0 )
   self . addControl ( self . button_run_glow )
   self . button_run_glow . setVisible ( False )
   self . button_run_glow . setImage ( self . image_button_run_glow )
   self . button_run_glow . setAnimations ( [
 ( 'conditional' , 'effect=fade start=0 time=1000 condition=true pulse=true' )
 ] )
   if 84 - 84: fgfttfgtgtff % TTGGGFFFF . FGGFTFFTFF / tftgtgg
   self . button_run = xbmcgui . ControlButton ( TGTF , tgffggfgt , 300 , 122 , "[B]Run Speedtest[/B]" ,
 focusTexture = self . image_button_run ,
 noFocusTexture = self . image_button_run , alignment = 2 | 4 ,
 textColor = '0xFF000000' , focusedColor = '0xFF000000' ,
 shadowColor = '0xFFCCCCCC' , disabledColor = '0xFF000000' )
   self . addControl ( self . button_run )
   self . setFocus ( self . button_run )
   self . button_run . setVisible ( False )
   self . button_run . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self . button_run . getId ( ) )
 ] )
   self . button_run_ID = self . button_run . getId ( )
   if 80 - 80: fgffftftg . FGGFTFFTFF - fgfttfgtgtff
   self . button_run . setEnabled ( True )
   self . button_run . setVisible ( True )
   self . button_run_glow . setEnabled ( True )
   self . button_run_glow . setVisible ( True )
  else :
   self . button_run . setEnabled ( False )
   self . button_run . setVisible ( False )
   self . button_run_glow . setEnabled ( False )
   self . button_run_glow . setVisible ( False )
   if 25 - 25: tftgtgg
   if 62 - 62: ttffttf + tg
 def displayButtonClose ( self , function = "true" ) :
  if ( function == "true" ) :
   if 98 - 98: fgfttfgtgtff
   self . button_close_glow = xbmcgui . ControlImage ( 880 , 418 , 300 , 122 , '' , aspectRatio = 0 )
   self . addControl ( self . button_close_glow )
   self . button_close_glow . setVisible ( False )
   self . button_close_glow . setImage ( self . image_button_run_glow )
   self . button_close_glow . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=0 time=1000 delay=2000 pulse=true condition=Control.IsVisible(%d)' % self . button_close_glow . getId ( ) )
 ] )
   if 51 - 51: tfgtff - ftgf + TTGGGFFFF * TFGT . TGGF + ftgf
   self . button_close = xbmcgui . ControlButton ( 99999 , 99999 , 300 , 122 , "[B]Close[/B]" ,
 focusTexture = self . image_button_run ,
 noFocusTexture = self . image_button_run , alignment = 2 | 4 ,
 textColor = '0xFF000000' , focusedColor = '0xFF000000' ,
 shadowColor = '0xFFCCCCCC' )
   self . addControl ( self . button_close )
   self . button_close . setVisible ( False )
   self . button_close . setPosition ( 880 , 418 )
   self . button_close_ID = self . button_close . getId ( )
   self . button_close . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self . button_close . getId ( ) )
 ] )
  elif ( function == "visible" ) :
   self . button_close . setVisible ( True )
   self . button_close_glow . setVisible ( True )
   self . setFocus ( self . button_close )
  else :
   self . button_close . setVisible ( False )
   self . button_close_glow . setVisible ( False )
   if 78 - 78: FGGFTFFTFF / fggfffg - TFGT / ttffttf + ftgf
   if 82 - 82: TFGT
 def displayPingTest ( self , function = "true" ) :
  if ( function == "true" ) :
   if 46 - 46: tffffffftt . FGGFTFFTFF
   ttfgftggfftgg = ( self . screenx / 3 ) - ( 320 / 2 )
   fttgtggftgtff = ( self . screeny / 3 ) - ( 130 / 2 ) + 50
   self . imgCentertext = xbmcgui . ControlImage ( ttfgftggfftgg , fttgtggftgtff , 320 , 130 , ' ' , aspectRatio = 0 )
   self . addControl ( self . imgCentertext )
   if 67 - 67: tftgtgg - ttffttf
   if 36 - 36: tfggtg
   TGGFT = ( self . screenx / 3 ) - ( 600 / 2 )
   TGFTGFFGTT = ( self . screeny / 3 ) - ( 400 / 2 )
   self . imgPing = xbmcgui . ControlImage ( TGGFT , TGFTGFFGTT , 600 , 400 , '' , aspectRatio = 1 )
   self . imgPing_glow = xbmcgui . ControlImage ( TGGFT , TGFTGFFGTT , 600 , 400 , '' , aspectRatio = 1 )
   self . addControl ( self . imgPing )
   self . addControl ( self . imgPing_glow )
   self . imgPing . setVisible ( False )
   self . imgPing_glow . setVisible ( False )
   self . imgPing . setImage ( self . image_ping )
   self . imgPing_glow . setImage ( self . image_ping_glow )
   self . imgPing . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self . imgPing . getId ( ) ) ,
 ( 'conditional' ,
 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self . imgPing . getId ( ) )
 ] )
   self . imgPing_glow . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=0 time=1000 pulse=true condition=Control.IsEnabled(%d)' % self . imgPing_glow . getId ( ) ) ,
 ( 'conditional' ,
 'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self . imgPing_glow . getId ( ) ) ,
 ( 'conditional' ,
 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self . imgPing_glow . getId ( ) )
 ] )
   self . imgCentertext . setAnimations ( [
 ( 'conditional' , 'effect=fade start=70 time=1000 condition=true pulse=true' )
 ] )
  elif ( function == "visible" ) :
   self . imgPing . setVisible ( True )
   self . imgPing_glow . setVisible ( True )
  else :
   self . imgPing . setVisible ( False )
   self . imgPing_glow . setVisible ( False )
   if 57 - 57: fgffftftg % TFGT + fgfttfgtgtff - tfgtff
   self . imgCentertext . setVisible ( False )
   if 65 - 65: TGGF . tftfttgg
   if 39 - 39: TTGGGFFFF / TFTFFGTFGTTF + fgffftftg / tftfttgg
 def displayGaugeTest ( self , function = "true" ) :
  if ( function == "true" ) :
   if 13 - 13: tfggtg + tg + fggfffg % TGTFFT / fgfttfgtgtff . tfggtg
   ttgtfffgfttgt = ( self . screenx / 3 ) - ( 548 / 2 )
   fggtg = ( self . screeny / 3 ) - ( 400 / 2 )
   if 83 - 83: TFTFFGTFGTTF
   ftggtfgtgf = ( self . screenx / 3 ) - ( 66 / 2 ) - 5
   FFG = ( self . screeny / 3 ) - ( 260 / 2 ) - 60
   self . imgGauge = xbmcgui . ControlImage ( ttgtfffgfttgt , fggtg , 548 , 400 , '' , aspectRatio = 0 )
   self . imgGauge_arrow = xbmcgui . ControlImage ( ftggtfgtgf , FFG , 66 , 260 , '' , aspectRatio = 0 )
   self . addControl ( self . imgGauge )
   self . addControl ( self . imgGauge_arrow )
   self . imgGauge . setVisible ( False )
   self . imgGauge_arrow . setVisible ( False )
   self . imgGauge . setImage ( self . image_gauge )
   self . imgGauge_arrow . setImage ( self . image_gauge_arrow )
   self . imgGauge . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=0 end=100 delay=1000 time=1000 condition=Control.IsVisible(%d)' % self . imgGauge . getId ( ) ) ,
 ( 'conditional' ,
 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self . imgGauge . getId ( ) )
 ] )
   self . imgGauge_arrow . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=0 end=100 time=1000 condition=Control.IsVisible(%d)' % self . imgGauge_arrow . getId ( ) ) ,
 ( 'conditional' ,
 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self . imgGauge_arrow . getId ( ) )
 ] )
   if 35 - 35: fggfffg * ftgf / FTFFGTGGTGTTG - fgfttfgtgtff / tffffffftt - fgffftftg
   TTGTGFFTTT = ( self . screenx / 3 ) - ( 200 / 2 )
   fttfgtggf = ( self . screeny / 3 ) - ( 50 / 2 ) + 170
   self . dlul_prog_textbox = xbmcgui . ControlLabel ( TTGTGFFTTT , fttfgtggf , 200 , 50 , label = '' ,
 textColor = '0xFFFFFFFF' , font = 'font30' , alignment = 2 | 4 )
   self . addControl ( self . dlul_prog_textbox )
  elif ( function == "visible" ) :
   self . imgGauge . setEnabled ( True )
   self . imgGauge . setVisible ( True )
   self . imgGauge_arrow . setEnabled ( True )
   self . imgGauge_arrow . setVisible ( True )
  else :
   self . imgGauge . setEnabled ( False )
   self . imgGauge . setVisible ( False )
   self . imgGauge_arrow . setEnabled ( False )
   self . imgGauge_arrow . setVisible ( False )
   self . dlul_prog_textbox . setLabel ( '' )
   if 8 - 8: tftgtgg
   if 49 - 49: TGTFFT - TGGF
 def displayProgressBar ( self , function = "true" ) :
  if ( function == "true" ) :
   self . imgProgress = xbmcgui . ControlImage ( 340 , 640 , 600 , 20 , '' , aspectRatio = 0 , colorDiffuse = "0xFF00AACC" )
   self . addControl ( self . imgProgress )
   self . imgProgress . setVisible ( False )
   self . imgProgress . setImage ( self . image_progress )
   self . imgProgress . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=0 end=100 time=500 condition=Control.IsVisible(%d)' % self . imgProgress . getId ( ) ) ,
 ( 'conditional' ,
 'effect=fade start=100 end=0 time=300 condition=!Control.IsEnabled(%d)' % self . imgProgress . getId ( ) )
 ] )
   self . imgProgress . setVisible ( True )
   tfttftffffttf = ( self . screenx / 3 ) - ( 200 / 2 )
   ftfgt = ( self . screeny / 3 ) - ( 50 / 2 ) + 270
   self . please_wait_textbox = xbmcgui . ControlLabel ( tfttftffffttf , ftfgt , 200 , 50 ,
 label = 'Please wait...' , textColor = '0xFFFFFFFF' ,
 alignment = 2 | 4 )
   self . addControl ( self . please_wait_textbox )
  elif ( function == "visible" ) :
   self . please_wait_textbox . setVisible ( True )
   self . imgProgress . setEnabled ( True )
   self . imgProgress . setVisible ( True )
  else :
   self . please_wait_textbox . setVisible ( False )
   self . imgProgress . setEnabled ( False )
   self . imgProgress . setVisible ( False )
   if 52 - 52: FGGFTFFTFF / fgfttfgtgtff * TFTFFGTFGTTF
 def displayResults ( self , function = "true" ) :
  if ( function == "true" ) :
   self . imgResults = xbmcgui . ControlImage ( 932 , 40 , 320 , 144 , '' , aspectRatio = 0 )
   self . addControl ( self . imgResults )
   self . imgResults . setVisible ( False )
   self . imgResults . setImage ( self . image_speedtestresults )
   self . imgResults . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=100 end=0 time=300 delay=1000 condition=!Control.IsEnabled(%d)' % self . imgResults . getId ( ) )
 ] )
   self . imgResults . setVisible ( True )
   if 22 - 22: tftfttgg . ttffttf * tftfttgg
   self . ping_textbox = xbmcgui . ControlLabel ( 955 , 133 , 75 , 50 , label = '' , textColor = '0xFFFFFFFF' )
   self . addControl ( self . ping_textbox )
   if 54 - 54: tfggtg + TFGT % tftgtgg + tffffffftt - tg - fgfttfgtgtff
   self . dl_textbox = xbmcgui . ControlLabel ( 1035 , 133 , 75 , 50 , label = '' , textColor = '0xFFFFFFFF' )
   self . addControl ( self . dl_textbox )
   if 77 - 77: ttffttf * FTFFGTGGTGTTG
   self . ul_textbox = xbmcgui . ControlLabel ( 1153 , 133 , 75 , 50 , label = '' , textColor = '0xFFFFFFFF' )
   self . addControl ( self . ul_textbox )
   if 98 - 98: TGTFFT % TFGT * tffffffftt
  elif ( function == "visible" ) :
   self . imgResults . setEnabled ( True )
   self . imgResults . setVisible ( True )
  else :
   self . imgResults . setEnabled ( False )
   self . dl_textbox . setLabel ( '' )
   self . ul_textbox . setLabel ( '' )
   self . ping_textbox . setLabel ( '' )
   if 51 - 51: FTFFGTGGTGTTG . tftfttgg / ftgf + fgfttfgtgtff
   if 33 - 33: TFTFFGTFGTTF . TTGGGFFFF % fggfffg + fgfttfgtgtff
 def showEndResult ( self ) :
  self . imgFinalResults = xbmcgui . ControlImage ( 932 , 40 , 320 , 144 , '' , aspectRatio = 0 )
  self . addControl ( self . imgFinalResults )
  self . imgFinalResults . setVisible ( False )
  self . imgFinalResults . setEnabled ( False )
  if 71 - 71: tfgtff % ttffttf
  self . imgFinalResults . setImage ( image_result )
  self . imgFinalResults . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=0 end=100 time=1000 delay=100 condition=Control.IsVisible(%d)' % self . imgFinalResults . getId ( ) ) ,
 ( 'conditional' ,
 'effect=zoom end=175 start=100 center=%s time=2000 delay=3000 condition=Control.IsVisible(%d)' % (
 "auto" , self . imgFinalResults . getId ( ) ) ) ,
 ( 'conditional' ,
 'effect=slide end=-100,25 time=2000 delay=3000 tween=linear easing=in condition=Control.IsVisible(%d)' % self . imgFinalResults . getId ( ) )
 ] )
  self . imgFinalResults . setVisible ( True )
  self . imgFinalResults . setEnabled ( True )
  if 98 - 98: TGGF % FGGFTFFTFF % TFTFFGTFGTTF + TFGT
 def showEndResultSP ( self ) :
  self . rec_speed = xbmcgui . ControlTextBox ( 325 , 475 , 600 , 300 , textColor = '0xFFFFFFFF' )
  self . addControl ( self . rec_speed )
  self . rec_speed . setVisible ( False )
  self . rec_speed . setEnabled ( False )
  self . rec_speed . setText ( "" . join ( "[B]Recomenended Speeds for Streaming! \n3 to 5 Mb/s for viewing standard definition 480p video \n5 to 10 Mb/s for viewing high-def 720p video \n10+ Mb/s or more for the best  1080p experience \n10+ Mb/s for the best Live TV Streaming experience \n25 to 50+ Mb/s 4K streaming \nAll Speeds are based on the device not what speed you pay for![/B]" ) )
  self . rec_speed . setAnimations ( [
 ( 'conditional' ,
 'effect=fade start=0 end=100 time=1000 delay=100 condition=Control.IsVisible(%d)' % self . rec_speed . getId ( ) ) ,
 ] )
  self . rec_speed . setVisible ( True )
  self . rec_speed . setEnabled ( True )
  if 78 - 78: TGFFGGFTFGGF % ftgf / fggfffg - FTFFGTGGTGTTG
 def onAction ( self , action ) :
  if action == 10 or action == 92 :
   self . saveClose ( )
   if 69 - 69: fgffftftg
 def onClick ( self , control ) :
  if control == self . button_run_ID :
   self . testRun = True
   if 11 - 11: TGTFFT
   self . displayButtonRun ( False )
   self . displayResults ( )
   self . displayProgressBar ( )
   self . displayPingTest ( )
   self . displayGaugeTest ( )
   if 16 - 16: TFGT + tfggtg * tg % FGTTF . TGTFFT
   self . speedtest ( share = True , simple = True )
   if 67 - 67: tffffffftt / TGTFFT * TFGT + TGGF
   self . displayProgressBar ( False )
   self . displayPingTest ( False )
   self . displayGaugeTest ( False )
   self . displayResults ( False )
   self . showEndResult ( )
   self . showEndResultSP ( )
   self . displayButtonClose ( "visible" )
  if control == self . button_close_ID :
   self . saveClose ( )
   if 65 - 65: tffffffftt - TGFFGGFTFGGF / TFTFFGTFGTTF / TTGGGFFFF / FGTTF
   if 71 - 71: fgffftftg + TFGT
 def saveClose ( self ) :
  self . close ( )
  if 28 - 28: ttffttf
  if 38 - 38: TFTFFGTFGTTF % TTGGGFFFF % TGGF / tftgtgg + tftfttgg / FGTTF
 def update_textbox ( self , text ) :
  self . textbox . setText ( "\n" . join ( text ) )
  if 54 - 54: FTFFGTGGTGTTG % TGFFGGFTFGGF - ttffttf / ftgf - tftgtgg . TGGF
  if 11 - 11: TGFFGGFTFGGF . tftgtgg * tfggtg * tffffffftt + TFTFFGTFGTTF
 def error ( self , message ) :
  if 33 - 33: tg * fgfttfgtgtff - fgffftftg % fgffftftg
  self . imgProgress . setImage ( ' ' )
  self . button_close . setVisible ( True )
  self . setFocus ( self . button_close )
  if 18 - 18: fgffftftg / tfgtff * fgffftftg + fgffftftg * FGGFTFFTFF * TGFFGGFTFGGF
  if 11 - 11: TFTFFGTFGTTF / tftfttgg - tfggtg * tffffffftt + tffffffftt . tftfttgg
 def configGauge ( self , speed , last_speed = 0 , time = 1000 ) :
  if last_speed == 0 :
   last_speed = 122
  FGTGFGGGTF = 0
  if speed <= 1 :
   FGTGFGGGTF = 122 - float ( ( float ( speed ) - float ( 0 ) ) ) * float (
 ( float ( 31 ) / float ( 1 ) ) )
  elif speed <= 2 :
   FGTGFGGGTF = 90 - float ( ( float ( speed ) - float ( 1 ) ) ) * float (
 ( float ( 31 ) / float ( 1 ) ) )
  elif speed <= 3 :
   FGTGFGGGTF = 58 - float ( ( float ( speed ) - float ( 2 ) ) ) * float (
 ( float ( 29 ) / float ( 1 ) ) )
  elif speed <= 5 :
   FGTGFGGGTF = 28 - float ( ( float ( speed ) - float ( 3 ) ) ) * float (
 ( float ( 28 ) / float ( 2 ) ) )
  elif speed <= 10 :
   FGTGFGGGTF = float ( ( float ( speed ) - float ( 5 ) ) ) * float (
 ( float ( 28 ) / float ( 5 ) ) )
  elif speed <= 20 :
   FGTGFGGGTF = 29 + float ( ( float ( speed ) - float ( 10 ) ) ) * float (
 ( float ( 29 ) / float ( 10 ) ) )
  elif speed <= 30 :
   FGTGFGGGTF = 59 + float ( ( float ( speed ) - float ( 20 ) ) ) * float (
 ( float ( 31 ) / float ( 10 ) ) )
  elif speed <= 50 :
   FGTGFGGGTF = 91 + float ( ( float ( speed ) - float ( 30 ) ) ) * float (
 ( float ( 31 ) / float ( 20 ) ) )
  elif speed > 50 :
   FGTGFGGGTF = 122
  fff = "%.0f" % float ( FGTGFGGGTF )
  if speed > 5 :
   fff = '-' + str ( fff )
   if 27 - 27: TFTFFGTFGTTF % TGTFFT
  ftggtfgtgf = ( self . screenx / 3 ) - ( 66 / 2 ) + 28
  FFG = ( self . screeny / 3 ) + ( 260 / 2 ) - 88
  self . imgGauge_arrow . setAnimations ( [
 ( 'conditional' , 'effect=rotate start=%d end=%d center=%d,%d condition=Control.IsVisible(%d) time=%d' % (
 int ( last_speed ) , int ( fff ) , ftggtfgtgf , FFG , self . imgGauge . getId ( ) , time ) )
 ] )
  return fff
  if 73 - 73: ttffttf
  if 70 - 70: FTFFGTGGTGTTG
 def downloadSpeed ( self , files , quiet = False ) :
  fggffftgtf = timeit . default_timer ( )
  def FGGFFGFT ( q , files ) :
   for file in files :
    FGT = TFGGTFGT ( file , fggffftgtf )
    FGT . start ( )
    q . put ( FGT , True )
    if 42 - 42: fgfttfgtgtff + FGTTF - TFGT / tfggtg
    if not quiet and not FGFGTT . isSet ( ) :
     sys . stdout . write ( '.' )
     sys . stdout . flush ( )
  FFTFTTTFFT = [ ]
  def FFTGTTTF ( q , total_files ) :
   TTGGTFTFGG = 0
   while len ( FFTFTTTFFT ) < total_files :
    FGT = q . get ( True )
    while FGT . isAlive ( ) :
     FGT . join ( timeout = 0.1 )
    FFTFTTTFFT . append ( sum ( FGT . result ) )
    TT = ( ( sum ( FFTFTTTFFT ) / ( timeit . default_timer ( ) - fggffftgtf ) ) / 1000 / 1000 ) * 8
    TTGGTFTFGG = self . configGauge ( TT , TTGGTFTFGG )
    self . dlul_prog_textbox . setLabel ( '%.02f Mbps ' % TT )
    del FGT
    if 77 - 77: ftgf * TFTFFGTFGTTF + tfggtg + tfgtff * ttffttf
    if 67 - 67: TGTFFT - fgfttfgtgtff / TGGF - FGTTF
  FGTTG = Queue ( 6 )
  FGGFGTFFFFTGFGTFF = threading . Thread ( target = FGGFFGFT , args = ( FGTTG , files ) )
  ffggftgf = threading . Thread ( target = FFTGTTTF , args = ( FGTTG ,
 len ( files ) ) )
  fggffftgtf = timeit . default_timer ( )
  FGGFGTFFFFTGFGTFF . start ( )
  ffggftgf . start ( )
  while FGGFGTFFFFTGFGTFF . isAlive ( ) :
   FGGFGTFFFFTGFGTFF . join ( timeout = 0.1 )
  while ffggftgf . isAlive ( ) :
   ffggftgf . join ( timeout = 0.1 )
  return sum ( FFTFTTTFFT ) / ( timeit . default_timer ( ) - fggffftgtf )
  if 31 - 31: ttffttf
 def uploadSpeed ( self , url , sizes , quiet = False ) :
  if 23 - 23: fgffftftg . tfggtg
  fggffftgtf = timeit . default_timer ( )
  if 92 - 92: tftfttgg + fgffftftg * TFGT % TGTFFT
  if 42 - 42: tfgtff
  def FGGFFGFT ( q , sizes ) :
   for ffgggtgtffft in sizes :
    FGT = fgtgtgg ( url , fggffftgtf , ffgggtgtffft )
    FGT . start ( )
    q . put ( FGT , True )
    if not quiet and not FGFGTT . isSet ( ) :
     sys . stdout . write ( '.' )
     sys . stdout . flush ( )
  FFTFTTTFFT = [ ]
  def FFTGTTTF ( q , total_sizes ) :
   TTGGTFTFGG = 0
   while len ( FFTFTTTFFT ) < total_sizes :
    FGT = q . get ( True )
    while FGT . isAlive ( ) :
     FGT . join ( timeout = 0.1 )
    FFTFTTTFFT . append ( FGT . result )
    TT = ( ( sum ( FFTFTTTFFT ) / ( timeit . default_timer ( ) - fggffftgtf ) ) / 1000 / 1000 ) * 8
    TTGGTFTFGG = self . configGauge ( TT , TTGGTFTFGG )
    self . dlul_prog_textbox . setLabel ( '%.02f Mbps ' % TT )
    del FGT
    if 93 - 93: TGGF . TTGGGFFFF / ftgf % tffffffftt * TGGF % TGFFGGFTFGGF
    if 48 - 48: TFTFFGTFGTTF / fgffftftg . FTFFGTGGTGTTG * tftfttgg * ftgf / FGTTF
  FGTTG = Queue ( 6 )
  FGGFGTFFFFTGFGTFF = threading . Thread ( target = FGGFFGFT , args = ( FGTTG , sizes ) )
  ffggftgf = threading . Thread ( target = FFTGTTTF , args = ( FGTTG ,
 len ( sizes ) ) )
  fggffftgtf = timeit . default_timer ( )
  FGGFGTFFFFTGFGTFF . start ( )
  ffggftgf . start ( )
  while FGGFGTFFFFTGFGTFF . isAlive ( ) :
   FGGFGTFFFFTGFGTFF . join ( timeout = 0.1 )
  while ffggftgf . isAlive ( ) :
   ffggftgf . join ( timeout = 0.1 )
  return sum ( FFTFTTTFFT ) / ( timeit . default_timer ( ) - fggffftgtf )
  if 92 - 92: tfgtff % tfgtff - fgfttfgtgtff / tftfttgg
  if 10 - 10: fggfffg + tfgtff * TGFFGGFTFGGF + FTFFGTGGTGTTG / fgffftftg / TGFFGGFTFGGF
 def speedtest ( self , list = False , mini = None , server = None , share = False , simple = False , src = None , timeout = 10 ,

 units = ( 'bit' , 8 ) , version = False ) :
  self . imgPing . setVisible ( True )
  self . imgPing_glow . setVisible ( True )
  FTGTT = [ 'Executed Speed Test Script' ]
  if 69 - 69: TFTFFGTFGTTF % ftgf
  global FGFGTT , FTGTFGGGGGFTF
  FGFGTT = threading . Event ( )
  if 50 - 50: tffffffftt % TGGF
  socket . setdefaulttimeout ( timeout )
  if 49 - 49: ftgf - FGGFTFFTFF . fgffftftg * TFGT % fggfffg + FGTTF
  if src :
   FTGTFGGGGGFTF = src
   socket . socket = ff
   if 71 - 71: fgfttfgtgtff
  FTGTT . append ( 'Retrieving speedtest.net configuration' )
  self . update_textbox ( FTGTT )
  if not simple :
   FFTTTTFGFG ( 'Retrieving speedtest.net configuration' )
  try :
   tggfffgtg = ttgtgtfttg ( )
  except URLError :
   FFTTTTFGFG ( 'Cannot retrieve speedtest configuration' )
   return False
   if 38 - 38: ftgf % tftfttgg + TGFFGGFTFGGF . FGGFTFFTFF
  FTGTT . append ( 'Retrieving speedtest.net server list' )
  self . update_textbox ( FTGTT )
  self . imgCentertext . setImage ( self . image_centertext_testingping )
  FFTTTTFGFG ( 'Retrieving speedtest.net server list...' )
  if 53 - 53: FGGFTFFTFF * fggfffg
  ftftgfggttg = tgFFGFFGFF ( tggfffgtg [ 'client' ] )
  if 68 - 68: FTFFGTGGTGTTG * FTFFGTGGTGTTG . fgfttfgtgtff / TTGGGFFFF % tfgtff
  FTGTT . append ( 'Testing from %(isp)s (%(ip)s)' % tggfffgtg [ 'client' ] )
  self . update_textbox ( FTGTT )
  FFTTTTFGFG ( 'Testing from %(isp)s (%(ip)s)...' % tggfffgtg [ 'client' ] )
  if 38 - 38: TFTFFGTFGTTF - ttffttf / fggfffg
  FGTFFGFGT = TTF ( ftftgfggttg )
  if 66 - 66: tg % TGFFGGFTFGGF + FGGFTFFTFF . tftfttgg / TFGT + TGFFGGFTFGGF
  try :
   FTGTT . append ( 'Selecting best server based on latency' )
   self . update_textbox ( FTGTT )
   FFTTTTFGFG ( 'Selecting best server based on latency' )
  except : pass
  try :
   FTGTT . append ( 'Hosted by: %(sponsor)s' % FGTFFGFGT )
   self . update_textbox ( FTGTT )
   FFTTTTFGFG ( 'Hosted by %(sponsor)s' % FGTFFGFGT )
  except : pass
  try :
   FTGTT . append ( 'Host Server: %(host)s' % FGTFFGFGT )
   self . update_textbox ( FTGTT )
   FFTTTTFGFG ( 'Host Server: %(host)s' % FGTFFGFGT )
  except : pass
  try :
   FTGTT . append ( 'Country: %(country)s' % FGTFFGFGT )
   self . update_textbox ( FTGTT )
   FFTTTTFGFG ( 'Location: %(country)s' % FGTFFGFGT )
  except : pass
  try :
   FTGTT . append ( 'City , State: %(name)s' % FGTFFGFGT )
   self . update_textbox ( FTGTT )
   FFTTTTFGFG ( 'City , State: %(name)s' % FGTFFGFGT )
  except : pass
  try :
   fffggtff = 0.62
   tfgfgtgg = '%(d)0.2f ' % FGTFFGFGT
   FFGTGFGG = float ( tfgfgtgg )
   tt = FFGTGFGG * fffggtff
   FTGTT . append ( 'Distance: %s mi' % tt )
   self . update_textbox ( FTGTT )
   FFTTTTFGFG ( 'Distance: %s' % tt )
  except : pass
  try :
   FTGTT . append ( 'Ping: %(latency)s ms' % FGTFFGFGT )
   self . update_textbox ( FTGTT )
   self . ping_textbox . setLabel ( "%.0f" % float ( FGTFFGFGT [ 'latency' ] ) )
   FFTTTTFGFG ( 'Ping: %(latency)s ms' % FGTFFGFGT )
  except : pass
  self . imgCentertext . setImage ( ' ' )
  self . imgPing . setEnabled ( False )
  self . imgPing_glow . setEnabled ( False )
  if 84 - 84: TFTFFGTFGTTF % TFGT + FGGFTFFTFF
  TTGTGTF = [ 350 , 500 , 750 , 1000 , 1500 , 2000 , 2500 , 3000 , 3500 , 4000 ]
  FFTFF = [ ]
  for tffgtgffff in TTGTGTF :
   for fttftg in range ( 0 , 4 ) :
    FFTFF . append ( '%s/random%sx%s.jpg' %
 ( os . path . dirname ( FGTFFGFGT [ 'url' ] ) , tffgtgffff , tffgtgffff ) )
  self . imgGauge . setVisible ( True )
  time . sleep ( 1 )
  self . configGauge ( 0 )
  self . imgGauge_arrow . setVisible ( True )
  if 36 - 36: tffffffftt . tftgtgg
  FTGTT . append ( 'Testing download speed' )
  self . update_textbox ( FTGTT )
  if not simple :
   FFTTTTFGFG ( 'Testing download speed' , end = '' )
  ft = self . downloadSpeed ( FFTFF , simple )
  if not simple :
   FFTTTTFGFG ( )
  FTGTT . append ( 'Download: %0.2f M%s/s' % ( ( ft / 1000 / 1000 ) * units [ 1 ] , units [ 0 ] ) )
  self . update_textbox ( FTGTT )
  self . dl_textbox . setLabel ( "%.2f" % float ( ( ft / 1000 / 1000 ) * units [ 1 ] ) )
  FFTTTTFGFG ( 'Download: %0.2f M%s/s' %
 ( ( ft / 1000 / 1000 ) * units [ 1 ] , units [ 0 ] ) )
  self . configGauge ( 0 , ( ft / 1000 / 1000 ) * 8 , time = 3000 )
  time . sleep ( 2 )
  if 10 - 10: tfgtff / tfgtff / fgffftftg . fgffftftg
  ttff = [ int ( .25 * 1000 * 1000 ) , int ( .5 * 1000 * 1000 ) ]
  TTGTGTF = [ ]
  for tffgtgffff in ttff :
   for fttftg in range ( 0 , 25 ) :
    TTGTGTF . append ( tffgtgffff )
    if 50 - 50: tftgtgg
  FTGTT . append ( 'Testing upload speed' )
  self . update_textbox ( FTGTT )
  if not simple :
   FFTTTTFGFG ( 'Testing upload speed' , end = '' )
  FF = self . uploadSpeed ( FGTFFGFGT [ 'url' ] , TTGTGTF , simple )
  if not simple :
   FFTTTTFGFG ( )
  FTGTT . append ( 'Upload: %0.2f M%s/s' % ( ( FF / 1000 / 1000 ) * units [ 1 ] , units [ 0 ] ) )
  self . update_textbox ( FTGTT )
  self . ul_textbox . setLabel ( "%.2f" % float ( ( FF / 1000 / 1000 ) * units [ 1 ] ) )
  FFTTTTFGFG ( 'Upload: %0.2f M%s/s' %
 ( ( FF / 1000 / 1000 ) * units [ 1 ] , units [ 0 ] ) )
  self . configGauge ( 0 , ( FF / 1000 / 1000 ) * 8 , time = 3000 )
  time . sleep ( 2 )
  if 25 - 25: tffffffftt - TGTFFT . TGTFFT * ftgf
  if share :
   fgggff = int ( round ( ( ft / 1000 ) * 8 , 0 ) )
   fggfg = int ( round ( FGTFFGFGT [ 'latency' ] , 0 ) )
   TTGTTTGTGTGTF = int ( round ( ( FF / 1000 ) * 8 , 0 ) )
   if 70 - 70: tftgtgg % ftgf + ttffttf / TFGT % tg
   ftggtg = [
 'download=%s' % fgggff ,
 'ping=%s' % fggfg ,
 'upload=%s' % TTGTTTGTGTGTF ,
 'promo=' ,
 'startmode=%s' % 'pingselect' ,
 'recommendedserverid=%s' % FGTFFGFGT [ 'id' ] ,
 'accuracy=%s' % 1 ,
 'serverid=%s' % FGTFFGFGT [ 'id' ] ,
 'hash=%s' % md5 ( ( '%s-%s-%s-%s' %
 ( fggfg , TTGTTTGTGTGTF , fgggff , '297aae72' ) )
 . encode ( ) ) . hexdigest ( ) ]
   if 36 - 36: ftgf - TFGT . tfgtff - FGGFTFFTFF - ttffttf * tfgtff
   FFTFT = { 'Referer' : 'https://c.speedtest.net/flash/speedtest.swf' }
   FTTTTFFG = tfffgtffggg ( 'https://www.speedtest.net/api/api.php' ,
 data = '&' . join ( ftggtg ) . encode ( ) ,
 headers = FFTFT )
   ffgggttggtf = FGGFG ( FTTTTFFG )
   if ffgggttggtf is False :
    FFTTTTFGFG ( 'Could not submit results to speedtest.net' )
    return False
   tfftttt = ffgggttggtf . read ( )
   FTTTFFTGFGF = ffgggttggtf . code
   ffgggttggtf . close ( )
   if 32 - 32: tftfttgg / tftgtgg + ttffttf
   if int ( FTTTFFTGFGF ) != 200 :
    FFTTTTFGFG ( 'Could not submit results to speedtest.net' )
    return False
    if 32 - 32: FTFFGTGGTGTTG % fggfffg
   tgf = parse_qs ( tfftttt . decode ( ) )
   FGFTFTTF = tgf . get ( 'resultid' )
   if not FGFTFTTF or len ( FGFTFTTF ) != 1 :
    FFTTTTFGFG ( 'Could not submit results to speedtest.net' )
    return False
    if 62 - 62: tfgtff - TGGF
   FFTTTTFGFG ( 'Share results: https://www.speedtest.net/result/%s.png' %
 FGFTFTTF [ 0 ] )
   if 21 - 21: tg % tfggtg . TGTFFT / TTGGGFFFF + tfggtg
   global image_result
   image_result = 'https://www.speedtest.net/result/%s.png' % FGFTFTTF [ 0 ]
   if 53 - 53: ftgf - TGTFFT - ftgf * fggfffg
if __name__ == '__main__' :
 ffffffgtt = tgggtttttf ( "main.xml" , TFTT . getAddonInfo ( 'path' ) , "Default" )
 del ffffffgtt
 if 14 - 14: ftgf / ftgf % TFTFFGTFGTTF
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
