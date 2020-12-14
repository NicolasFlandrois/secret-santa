#!/usr/bin/python3

# Thu 20 Dec 2018 03:04:22 PM CET
# Author: Nicolas Flandrois
# Description: Christmas countdown, according to a choosen year.
# NB: This script is not UTC/Timezone aware.
# Time is set as naive, using your local (computer) timezone as default.

import time
import datetime
import os
import platform
import sys

def clean():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

try:
    Year = int(input("Xmas of which year? "))
except:
    print("Oops! ",sys.exc_info()[0],
        """ occured. That was no valid number.  Try again...
choose a year, in positive number, format YYYY.""")

r = range(1, 9999)
if Year not in r:
    print("""Oops!  That was no valid number.
REMINDER: choose a positive year number between 1 and 9999.
Try again...""")

xd = datetime.datetime(Year, 12, 25, 0, 0, 1)

clean()

while True:
    td = datetime.datetime.now()
    delta = xd - td
    cd_Y = int(delta.days / 365)
    cd_W = int(abs(delta.days - (cd_Y * 365)) / 7)
    cd_D = int(abs(delta.days - ((cd_Y * 365)+ (cd_W * 7))))
    cd_h = int(delta.seconds / 3600)
    cd_m = int(abs(delta.seconds - (cd_h * 3600))/60)
    cd_s = int(abs(delta.seconds - ( cd_h*3600 + cd_m*60 )))

    print("#     #")
    print(" #   #     #    #   ##    #### ")
    print("  # #      ##  ##  #  #  #     ")
    print("   #       # ## # #    #  #### ")
    print("  # #      #    # ######      #")
    print(" #   #     #    # #    # #    #")
    print("#     #    #    # #    #  #### ")
    print("")
    print(" ####   ####  #    # #    # ##### #####   ####  #    # #    #")
    print("#    # #    # #    # ##   #   #   #    # #    # #    # ##   #")
    print("#      #    # #    # # #  #   #   #    # #    # #    # # #  #")
    print("#      #    # #    # #  # #   #   #    # #    # # ## # #  # #")
    print("#    # #    # #    # #   ##   #   #    # #    # ##  ## #   ##")
    print(" ####   ####   ####  #    #   #   #####   ####  #    # #    #")
    print("")
    print("Countdown until christmas of: ", xd.strftime("%A, %d of %B %Y"))
    print("")
    print("Total days left: ", delta.days)
    print("")
    print("or more precisely, time left: ")
    print(cd_Y, "Years", cd_W, "Weeks", cd_D, "Days - ", "%02d" % cd_h, ":",
        "%02d" % cd_m, ":", "%02d" % cd_s, "; Local Time.")
    print("")

    time.sleep(1)
    clean()

##############################################################################
#                                .:xxxxxxxx:.
#                             .xxxxxxxxxxxxxxxx.
#                            :xxxxxxxxxxxxxxxxxxx:.
#                           .xxxxxxxxxxxxxxxxxxxxxxx:
#                          :xxxxxxxxxxxxxxxxxxxxxxxxx:
#                          xxxxxxxxxxxxxxxxxxxxxxxxxxX:
#                          xxx:::xxxxxxxx::::xxxxxxxxx:
#                         .xx:   ::xxxxx:     :xxxxxxxx
#                         :xx  x.  xxxx:  xx.  xxxxxxxx
#                         :xx xxx  xxxx: xxxx  :xxxxxxx
#                         'xx 'xx  xxxx:. xx'  xxxxxxxx
#                          xx ::::::xx:::::.   xxxxxxxx
#                          xx:::::.::::.:::::::xxxxxxxx
#                          :x'::::'::::':::::':xxxxxxxxx.
#                          :xx.::::::::::::'   xxxxxxxxxx
#                          :xx: '::::::::'     :xxxxxxxxxx.
#                         .xx     '::::'        'xxxxxxxxxx.
#                       .xxxx                     'xxxxxxxxx.
#                     .xxxx                         'xxxxxxxxx.
#                   .xxxxx:                          xxxxxxxxxx.
#                  .xxxxx:'                          xxxxxxxxxxx.
#                 .xxxxxx:::.           .       ..:::_xxxxxxxxxxx:.
#                .xxxxxxx''      ':::''            ''::xxxxxxxxxxxx.
#                xxxxxx            :                  '::xxxxxxxxxxxx
#               :xxxx:'            :                    'xxxxxxxxxxxx:
#              .xxxxx              :                     ::xxxxxxxxxxxx
#              xxxx:'                                    ::xxxxxxxxxxxx
#              xxxx               .                      ::xxxxxxxxxxxx.
#          .:xxxxxx               :                      ::xxxxxxxxxxxx::
#          xxxxxxxx               :                      ::xxxxxxxxxxxxx:
#          xxxxxxxx               :                      ::xxxxxxxxxxxxx:
#          ':xxxxxx               '                      ::xxxxxxxxxxxx:'
#            .:. xx:.                                   .:xxxxxxxxxxxxx'
#          ::::::.'xx:.            :                  .:: xxxxxxxxxxx':
#  .:::::::::::::::.'xxxx.                            ::::'xxxxxxxx':::.
#  ::::::::::::::::::.'xxxxx                          :::::.'.xx.'::::::.
#  ::::::::::::::::::::.'xxxx:.                       :::::::.'':::::::::
#  ':::::::::::::::::::::.'xx:'                     .'::::::::::::::::::::..
#    :::::::::::::::::::::.'xx                    .:: :::::::::::::::::::::::
#  .:::::::::::::::::::::::. xx               .::xxxx :::::::::::::::::::::::
#  :::::::::::::::::::::::::.'xxx..        .::xxxxxxx ::::::::::::::::::::'
#  '::::::::::::::::::::::::: xxxxxxxxxxxxxxxxxxxxxxx :::::::::::::::::'
#    '::::::::::::::::::::::: xxxxxxxxxxxxxxxxxxxxxxx :::::::::::::::'
#        ':::::::::::::::::::_xxxxxx::'''::xxxxxxxxxx '::::::::::::'
#             '':.::::::::::'                        `._'::::::''
#
#                                   ,wmmmmmmmp
#                                   KP ]bbKKKKK
#                                   KKKKKKKKKKK
#                              a#KKKKKKKKKKKKKK PPhw
#                             #bbbbbbbbbbbKKKKK ||||h
#                             bbbbbbKMMMMMMMM*,$|||||
#                             bbbbbM,$|LLLL||||||||||
#                             Tbbbb LLLLL|||||||||||L
#                              `fff LLLLL*"""""""""`
#                                   LLLLL||P"!|
#                                   *|LLL||hw|*
#                                      `````
#                                    y  jM
#                       .m**m  m  :p #M jN~~m  m**w .m**m
#                       :N  jm:N  jM ]  jC  ] ]L  ]MjC  ]
#                       :N,,#^ N,,/M 1p jC  ] `N,,A jC  $
#                       :N        ]L
#                        '      `"
##############################################################################
