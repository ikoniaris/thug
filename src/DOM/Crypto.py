#!/usr/bin/env python
#
# Crypto.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA


class Crypto(object):
    def __init__(self):
        pass

    @property
    def enableSmartCardEvents(self):
        return False

    @property
    def version(self):
        return "2.4"

    def disableRightClick(self):
        pass

    def importUserCertificates(self, nickname, cmmfResponse, forceToBackUp):
        return ""

    def logout(self):
        pass


