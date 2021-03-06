# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2015 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Helper code to get user special chars specific for given language.
"""

from django.utils.translation import ugettext as _, ugettext_lazy

# Hard coded list of special chars
SPECIAL_CHARS = (u'→', u'↵', u'…')

# Names of hardcoded chars
CHAR_NAMES = {
    u'→': ugettext_lazy('Insert tab character'),
    u'↵': ugettext_lazy('Insert new line'),
    u'…': ugettext_lazy('Insert horizontal ellipsis'),
    u'।': ugettext_lazy('Danda'),
    u'॥': ugettext_lazy('Double danda'),
}

# Quotes definition for each language, based on CLDR data
SINGLE_OPEN = {
    'ja': u'『',
    'zh': u'『',
    'ar': u'’',
    'fi': u'’',
    'fo': u'’',
    'lag': u'’',
    'rn': u'’',
    'se': u'’',
    'sn': u'’',
    'sv': u'’',
    'ur': u'’',
    'eo': u'‘',
    'vo': u'‘',
    'ALL': u'‘',
    'agq': u'‚',
    'bs': u'‚',
    'cs': u'‚',
    'de': u'‚',
    'dsb': u'‚',
    'et': u'‚',
    'ff': u'‚',
    'hr': u'‚',
    'hsb': u'‚',
    'is': u'‚',
    'ksh': u'‚',
    'lb': u'‚',
    'luy': u'‚',
    'mk': u'‚',
    'sk': u'‚',
    'sl': u'‚',
    'ast': u'“',
    'bm': u'“',
    'ca': u'“',
    'cy': u'“',
    'dyo': u'“',
    'es': u'“',
    'ewo': u'“',
    'fur': u'“',
    'ia': u'“',
    'it': u'“',
    'kab': u'“',
    'mg': u'“',
    'mua': u'“',
    'nnh': u'“',
    'nr': u'“',
    'nso': u'“',
    'pt': u'“',
    'sg': u'“',
    'sq': u'“',
    'ss': u'“',
    'ti': u'“',
    'tn': u'“',
    'ts': u'“',
    've': u'“',
    'bas': u'„',
    'bg': u'„',
    'ky': u'„',
    'lt': u'„',
    'os': u'„',
    'ru': u'„',
    'shi': u'„',
    'uk': u'„',
    'zgh': u'„',
    'el': u'"',
    'eu': u'"',
    'uz': u'\'',
    'yi': u'\'',
    'hy': u'«',
    'ka': u'«',
    'nmg': u'«',
    'pl': u'«',
    'ro': u'«',
    'yav': u'«',
    'he': u'׳',
    'am': u'‹',
    'az': u'‹',
    'be': u'‹',
    'br': u'‹',
    'fa': u'‹',
    'fr': u'‹',
    'gsw': u'‹',
    'jgo': u'‹',
    'kkj': u'‹',
    'rm': u'‹',
    'wae': u'‹',
    'hu': u'»',
    'kl': u'›',
    'ug': u'›',
}

SINGLE_CLOSE = {
    'ja': u'』',
    'zh': u'』',
    'eo': u'’',
    'vo': u'’',
    'ALL': u'’',
    'ar': u'‘',
    'bs': u'‘',
    'cs': u'‘',
    'de': u'‘',
    'dsb': u'‘',
    'et': u'‘',
    'hr': u'‘',
    'hsb': u'‘',
    'is': u'‘',
    'ksh': u'‘',
    'lb': u'‘',
    'luy': u'‘',
    'mk': u'‘',
    'sk': u'‘',
    'sl': u'‘',
    'sr': u'‘',
    'ur': u'‘',
    'ast': u'”',
    'bm': u'”',
    'ca': u'”',
    'cy': u'”',
    'dyo': u'”',
    'es': u'”',
    'ewo': u'”',
    'fur': u'”',
    'ia': u'”',
    'it': u'”',
    'kab': u'”',
    'mg': u'”',
    'mua': u'”',
    'nnh': u'”',
    'nr': u'”',
    'nso': u'”',
    'pt': u'”',
    'sg': u'”',
    'shi': u'”',
    'sq': u'”',
    'ss': u'”',
    'ti': u'”',
    'tn': u'”',
    'ts': u'”',
    've': u'”',
    'zgh': u'”',
    'bas': u'“',
    'bg': u'“',
    'ky': u'“',
    'lt': u'“',
    'os': u'“',
    'ru': u'“',
    'uk': u'“',
    'el': u'"',
    'eu': u'"',
    'uz': u'\'',
    'yi': u'\'',
    'hu': u'«',
    'he': u'׳',
    'kl': u'‹',
    'ug': u'‹',
    'hy': u'»',
    'ka': u'»',
    'nmg': u'»',
    'pl': u'»',
    'ro': u'»',
    'yav': u'»',
    'am': u'›',
    'az': u'›',
    'be': u'›',
    'br': u'›',
    'fa': u'›',
    'fr': u'›',
    'gsw': u'›',
    'jgo': u'›',
    'kkj': u'›',
    'rm': u'›',
    'wae': u'›',
}

DOUBLE_OPEN = {
    'eu': u'"',
    'uz': u'"',
    'yi': u'"',
    'ja': u'「',
    'zh': u'「',
    'cy': u'‘',
    'fur': u'‘',
    'ia': u'‘',
    'nr': u'‘',
    'nso': u'‘',
    'ss': u'‘',
    'ti': u'‘',
    'tn': u'‘',
    'ts': u'‘',
    've': u'‘',
    'am': u'«',
    'ast': u'«',
    'az': u'«',
    'bas': u'«',
    'be': u'«',
    'bm': u'«',
    'br': u'«',
    'ca': u'«',
    'dua': u'«',
    'dyo': u'«',
    'el': u'«',
    'es': u'«',
    'ewo': u'«',
    'fa': u'«',
    'fr': u'«',
    'gsw': u'«',
    'hy': u'«',
    'it': u'«',
    'jgo': u'«',
    'kab': u'«',
    'kkj': u'«',
    'ksf': u'«',
    'ky': u'«',
    'mg': u'«',
    'mua': u'«',
    'nb': u'«',
    'nn': u'«',
    'nnh': u'«',
    'os': u'«',
    'pt': u'«',
    'rm': u'«',
    'ru': u'«',
    'rw': u'«',
    'sg': u'«',
    'shi': u'«',
    'sq': u'«',
    'uk': u'«',
    'wae': u'«',
    'yav': u'«',
    'zgh': u'«',
    'he': u'״',
    'ar': u'”',
    'fi': u'”',
    'fo': u'”',
    'lag': u'”',
    'rn': u'”',
    'se': u'”',
    'sn': u'”',
    'sv': u'”',
    'ur': u'”',
    'eo': u'“',
    'vo': u'“',
    'ALL': u'“',
    'kl': u'»',
    'ug': u'»',
    'agq': u'„',
    'bg': u'„',
    'bs': u'„',
    'cs': u'„',
    'de': u'„',
    'dsb': u'„',
    'et': u'„',
    'ff': u'„',
    'hr': u'„',
    'hsb': u'„',
    'hu': u'„',
    'is': u'„',
    'ka': u'„',
    'ksh': u'„',
    'lb': u'„',
    'lt': u'„',
    'luy': u'„',
    'mk': u'„',
    'nmg': u'„',
    'pl': u'„',
    'sk': u'„',
    'sl': u'„',
    'sr': u'„',
}

DOUBLE_CLOSE = {
    'eu': u'"',
    'kk': u'"',
    'uz': u'"',
    'yi': u'"',
    'he': u'״',
    'cy': u'’',
    'fur': u'’',
    'ia': u'’',
    'nr': u'’',
    'nso': u'’',
    'ss': u'’',
    'ti': u'’',
    'tn': u'’',
    'ts': u'’',
    've': u'’',
    'ja': u'」',
    'zh': u'」',
    'kl': u'«',
    'ug': u'«',
    'eo': u'”',
    'vo': u'”',
    'ALL': u'”',
    'ar': u'“',
    'bg': u'“',
    'bs': u'“',
    'cs': u'“',
    'de': u'“',
    'dsb': u'“',
    'et': u'“',
    'hr': u'“',
    'hsb': u'“',
    'is': u'“',
    'ka': u'“',
    'ksh': u'“',
    'lb': u'“',
    'lt': u'“',
    'luy': u'“',
    'mk': u'“',
    'sk': u'“',
    'sl': u'“',
    'sr': u'“',
    'ur': u'“',
    'am': u'»',
    'ast': u'»',
    'az': u'»',
    'bas': u'»',
    'be': u'»',
    'bm': u'»',
    'br': u'»',
    'ca': u'»',
    'dua': u'»',
    'dyo': u'»',
    'el': u'»',
    'es': u'»',
    'ewo': u'»',
    'fa': u'»',
    'fr': u'»',
    'gsw': u'»',
    'hy': u'»',
    'it': u'»',
    'jgo': u'»',
    'kab': u'»',
    'kkj': u'»',
    'ksf': u'»',
    'ky': u'»',
    'mg': u'»',
    'mua': u'»',
    'nb': u'»',
    'nn': u'»',
    'nnh': u'»',
    'os': u'»',
    'pt': u'»',
    'rm': u'»',
    'ru': u'»',
    'rw': u'»',
    'sg': u'»',
    'shi': u'»',
    'sq': u'»',
    'uk': u'»',
    'wae': u'»',
    'yav': u'»',
    'zgh': u'»',
}

HYPHEN_LANGS = frozenset((
    'af', 'am', 'ar', 'ast', 'az', 'bg', 'bs', 'ca', 'cs', 'cy', 'da', 'de',
    'dsb', 'dz', 'ee', 'el', 'en', 'eo', 'es', 'fa', 'fi', 'fr', 'fy', 'gd',
    'gl', 'gu', 'he', 'hr', 'hsb', 'id', 'is', 'ja', 'ka', 'kk', 'kn', 'ko',
    'ksh', 'ky', 'lb', 'lkt', 'lt', 'lv', 'mk', 'mn', 'mr', 'nl', 'os', 'pa',
    'pl', 'pt', 'ro', 'ru', 'sk', 'sr', 'sv', 'ta', 'th', 'to', 'tr', 'uz',
    'vi', 'vo', 'yi', 'zh',
))

EN_DASH_LANGS = frozenset((
    'af', 'am', 'ar', 'ast', 'az', 'bg', 'bs', 'ca', 'cs', 'cy', 'da', 'de',
    'dsb', 'dz', 'ee', 'el', 'en', 'eo', 'es', 'fi', 'fr', 'fy', 'gd', 'gl',
    'gu', 'he', 'hr', 'hsb', 'hu', 'id', 'is', 'ka', 'kk', 'kn', 'ksh', 'ky',
    'lb', 'lkt', 'lt', 'lv', 'mk', 'mn', 'mr', 'nb', 'nl', 'os', 'pa', 'pl',
    'pt', 'ro', 'ru', 'sk', 'sr', 'sv', 'ta', 'th', 'to', 'tr', 'uk', 'uz',
    'vi', 'vo', 'yi', 'zh',
))

EM_DASH_LANGS = frozenset((
    'af', 'ar', 'ast', 'az', 'bg', 'bs', 'ca', 'cy', 'de', 'dsb', 'dz', 'ee',
    'el', 'en', 'eo', 'es', 'fr', 'fy', 'gd', 'gl', 'gu', 'he', 'hr', 'hsb',
    'id', 'is', 'it', 'ja', 'ka', 'kk', 'kn', 'ko', 'ksh', 'ky', 'lb', 'lkt',
    'lt', 'lv', 'mk', 'mn', 'mr', 'nl', 'os', 'pa', 'pl', 'pt', 'ro', 'ru',
    'sv', 'ta', 'th', 'to', 'tr', 'uz', 'vi', 'vo', 'yi', 'zh',
))

EXTRA_CHARS = {
    'brx': (u'।', u'॥'),
}


def get_quote(code, data, name):
    """
    Returns special char for quote.
    """
    if code in data:
        return name, data[code]
    return name, data['ALL']


def get_char_description(char):
    """Returns verbose description of a character."""
    if char in CHAR_NAMES:
        return CHAR_NAMES[char]
    else:
        return _('Insert character {0}').format(char)


def get_special_chars(language):
    """
    Returns list of special characters.
    """
    for char in SPECIAL_CHARS:
        yield get_char_description(char), char
    code = language.code.replace('_', '-').split('-')[0]

    if code in EXTRA_CHARS:
        for char in EXTRA_CHARS[code]:
            yield get_char_description(char), char

    yield get_quote(code, DOUBLE_OPEN, _('Opening double quote'))
    yield get_quote(code, DOUBLE_CLOSE, _('Closing double quote'))
    yield get_quote(code, SINGLE_OPEN, _('Opening single quote'))
    yield get_quote(code, SINGLE_CLOSE, _('Closing single quote'))

    if code in HYPHEN_LANGS:
        yield _('Hyphen'), u'-'

    if code in EN_DASH_LANGS:
        yield _('En dash'), u'–'

    if code in EM_DASH_LANGS:
        yield _('Em dash'), u'—'
