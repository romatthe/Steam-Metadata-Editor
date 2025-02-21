#!/usr/bin/env python3
#
# A Metadata Editor for Steam Applications
# Copyright (C) 2023  Tomás Ralph
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
##################################
#                                #
#       Created by tralph3       #
#   https://github.com/tralph3   #
#                                #
##################################
import os
from hashlib import sha1

from appinfo import IncompatibleVDFError, Appinfo


def main():
    path = os.path.join(
        "/home/romatthe/Source/sme-rs/", "appinfo_duplicated.vdf"
    )
    appinfo = Appinfo(
        path, False, None
    )

    app = appinfo.parsedAppInfo[1325200]
    formatted = appinfo.dict_to_text_vdf(app["sections"])
    print(list(app['checksum_text']))
    print(app['checksum_text'].hex())
    print(list(sha1(formatted).digest()))
    print(sha1(formatted).hexdigest())
    print(formatted.decode())


if __name__ == "__main__":
    main()
