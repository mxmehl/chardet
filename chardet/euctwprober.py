######################## BEGIN LICENSE BLOCK ########################
# The Original Code is mozilla.org code.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
#
# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileCopyrightText: 1998 Netscape Communications Corporation
# SPDX-FileContributor: Mark Pilgim (port to Python)
######################### END LICENSE BLOCK #########################

from .chardistribution import EUCTWDistributionAnalysis
from .codingstatemachine import CodingStateMachine
from .mbcharsetprober import MultiByteCharSetProber
from .mbcssm import EUCTW_SM_MODEL


class EUCTWProber(MultiByteCharSetProber):
    def __init__(self) -> None:
        super().__init__()
        self.coding_sm = CodingStateMachine(EUCTW_SM_MODEL)
        self.distribution_analyzer = EUCTWDistributionAnalysis()
        self.reset()

    @property
    def charset_name(self) -> str:
        return "EUC-TW"

    @property
    def language(self) -> str:
        return "Taiwan"
