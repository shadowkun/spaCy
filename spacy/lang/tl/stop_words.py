# encoding: utf8
from __future__ import unicode_literals


# Add stop words
# Documentation: https://spacy.io/docs/usage/adding-languages#stop-words
# To improve readability, words should be ordered alphabetically and separated
# by spaces and newlines. When adding stop words from an online source, always
# include the link in a comment. Make sure to proofread and double-check the
# words – lists available online are often known to contain mistakes.

# data from https://github.com/stopwords-iso/stopwords-tl/blob/master/stopwords-tl.txt

STOP_WORDS = set("""
    akin
    aking
    ako
    alin
    am
    amin
    aming
    ang
    ano
    anumang
    apat
    at
    atin
    ating
    ay
    bababa
    bago
    bakit
    bawat
    bilang
    dahil
    dalawa
    dapat
    din
    dito
    doon
    gagawin
    gayunman
    ginagawa
    ginawa
    ginawang
    gumawa
    gusto
    habang
    hanggang
    hindi
    huwag
    iba
    ibaba
    ibabaw
    ibig
    ikaw
    ilagay
    ilalim
    ilan
    inyong
    isa
    isang
    itaas
    ito
    iyo
    iyon
    iyong
    ka
    kahit
    kailangan
    kailanman
    kami
    kanila
    kanilang
    kanino
    kanya
    kanyang
    kapag
    kapwa
    karamihan
    katiyakan
    katulad
    kaya
    kaysa
    ko
    kong
    kulang
    kumuha
    kung
    laban
    lahat
    lamang
    likod
    lima
    maaari
    maaaring
    maging
    mahusay
    makita
    marami
    marapat
    masyado
    may
    mayroon
    mga
    minsan
    mismo
    mula
    muli
    na
    nabanggit
    naging
    nagkaroon
    nais
    nakita
    namin
    napaka
    narito
    nasaan
    ng
    ngayon
    ni
    nila
    nilang
    nito
    niya
    niyang
    noon
    o
    pa
    paano
    pababa
    paggawa
    pagitan
    pagkakaroon
    pagkatapos
    palabas
    pamamagitan
    panahon
    pangalawa
    para
    paraan
    pareho
    pataas
    pero
    pumunta
    pumupunta
    sa
    saan
    sabi
    sabihin
    sarili
    sila
    sino
    siya
    tatlo
    tayo
    tulad
    tungkol
    una
    walang
""".split())
