# -*- coding: utf-8 -*-
#
## This file is part of Invenio.
## Copyright (C) 2012, 2013, 2014 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from invenio.config import CFG_SITE_NAME
from fixture import DataSet


class CollectionData(DataSet):

    class siteCollection:
        id = 1
        name = CFG_SITE_NAME
        dbquery = None

    class annotationDemo:
        id = 2
        name = 'Annotation Demo'
        dbquery = '980:"ANNOTATIONDEMO"'
        names = {
            ('en', 'ln'): u'Annotation Demo',
        }

    class Collection_34:
        id = 34
        dbquery = u'collection:AUTHORITY'
        names = {
            ('en', 'ln'): u'Authority Records',
            ('fr', 'ln'): u'Notices d\'autorité',
            ('pl', 'ln'): u'Rekordy kontrolne',
        }
        name = u'Authority Records'

    class Collection_35:
        id = 35
        dbquery = u'collection:AUTHOR'
        names = {
            ('en', 'ln'): u'Authors',
            ('fr', 'ln'): u'Auteurs',
            ('pl', 'ln'): u'Autorzy',
        }
        name = u'Authority Author'

    class Collection_36:
        id = 36
        dbquery = u'collection:INSTITUTION'
        names = {
            ('en', 'ln'): u'Institutions',
            ('fr', 'ln'): u'Institutions',
            ('pl', 'ln'): u'Instytucje',
        }
        name = u'Authority Institution'

    class Collection_37:
        id = 37
        dbquery = u'collection:JOURNAL'
        names = {
            ('en', 'ln'): u'Journals',
            ('fr', 'ln'): u'Journals',
            ('pl', 'ln'): u'Czasopisma',
        }
        name = u'Authority Journal'

    class Collection_38:
        id = 38
        dbquery = u'collection:SUBJECT'
        names = {
            ('en', 'ln'): u'Subjects',
            ('fr', 'ln'): u'Sujets',
            ('pl', 'ln'): u'Tematy',
        }
        name = u'Authority Subject'


class CollectionCollectionData(DataSet):

    class siteCollection_articlesPreprints:
        dad = CollectionData.siteCollection
        son = CollectionData.annotationDemo
        score = 0
        type = 'r'


class PortalboxData(DataSet):

    class Portalbox_1:
        body = u'Welcome to the demo site of the Invenio, a free document server software coming from CERN.  Please feel free to explore all the features of this demo site to the full.'
        id = 1
        title = u'ABOUT THIS SITE'

    class Portalbox_2:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 2
        title = u'SEE ALSO'

    class Portalbox_3:
        body = u'The Articles collection contains all the papers published in scientific journals by our staff.  The collection starts from 1998.'
        id = 3
        title = u'ABOUT ARTICLES'

    class Portalbox_4:
        body = u'<a href="http://arXiv.org/">arXiv.org</a><br /><a href="http://cds.cern.ch/">CDS</a><br /><a href="www.chemweb.com">ChemWeb</a><br /><a href="http://www.ams.org/mathscinet">MathSciNet</a>'
        id = 4
        title = u'SEE ALSO'

    class Portalbox_5:
        body = u'The Preprints collection contains not-yet-published papers and research results obtained at the institute.  The collection starts from 2001.'
        id = 5
        title = u'ABOUT PREPRINTS'

    class Portalbox_6:
        body = u'<a href="http://arXiv.org/">arXiv.org</a><br /><a href="http://cds.cern.ch/">CDS</a>'
        id = 6
        title = u'SEE ALSO'

    class Portalbox_7:
        body = u'The Books collection contains monographs published by institute staff as well as pointers to interesting online e-books available in fulltext.'
        id = 7
        title = u'ABOUT BOOKS'

    class Portalbox_8:
        body = u'<a href="http://etext.lib.virginia.edu/ebooks/ebooklist.html">UV e-Books</a><br /><a href="http://www.gutenberg.org/">Project Gutenberg</a>'
        id = 8
        title = u'SEE ALSO'

    class Portalbox_9:
        body = u"The Theses collection contains all students' theses defended at the institute.  The collection starts from 1950."
        id = 9
        title = u'ABOUT THESES'

    class Portalbox_10:
        body = u'<a href="http://www.theses.org/">NDLTD Theses</a><br /><a href="http://www.thesis.de/">Thesis.DE</a>'
        id = 10
        title = u'SEE ALSO'

    class Portalbox_11:
        body = u'The Reports collection contains miscellaneous technical reports, unpublished elsewhere.  The collection starts from 1950.'
        id = 11
        title = u'ABOUT REPORTS'

    class Portalbox_12:
        body = u'this is a test portal box'
        id = 12
        title = u'TEST portal box'

    class Portalbox_13:
        body = u'this is a test portal box'
        id = 13
        title = u'test'

    class Portalbox_14:
        body = u'The Pictures collection contains selected photographs and illustrations.  Please note that photographs are copyrighted.  The collection includes historical archive that starts from 1950.'
        id = 14
        title = u'ABOUT PICTURES'

    class Portalbox_15:
        body = u'These virtual collections present a specific point of view on the database content from CERN Divisions persective.'
        id = 15
        title = u'ABOUT CERN DIVISIONS'

    class Portalbox_16:
        body = u'These virtual collections present a specific point of view on the database content from CERN Experiments persective.'
        id = 16
        title = u'ABOUT CERN EXPERIMENTS'

    class Portalbox_17:
        body = u'This virtual collection groups together all the documents written by authors from CERN TH Division.'
        id = 17
        title = u'ABOUT TH'

    class Portalbox_18:
        body = u'This virtual collection groups together all the documents written by authors from CERN EP Division.'
        id = 18
        title = u'ABOUT EP'

    class Portalbox_19:
        body = u'This virtual collection groups together all the documents about ISOLDE CERN experiment.'
        id = 19
        title = u'ABOUT ISOLDE'

    class Portalbox_20:
        body = u'This virtual collection groups together all the documents about ALEPH CERN experiment.'
        id = 20
        title = u'ABOUT ALEPH'

    class Portalbox_21:
        body = u'This collection groups together all published and non-published articles, many of which in electronic fulltext form.'
        id = 21
        title = u'ABOUT ARTICLES AND PREPRINTS'

    class Portalbox_22:
        body = u'This collection groups together all monograph-like publications, be they books, theses, reports, book chapters, proceedings, and so on.'
        id = 22
        title = u'ABOUT BOOKS AND REPORTS'

    class Portalbox_23:
        body = u'This collection groups together all multimedia- and outreach- oriented material.'
        id = 23
        title = u'ABOUT MULTIMEDIA & OUTREACH'

    class Portalbox_24:
        body = u'This collection presents poetry excerpts, mainly to demonstrate and test the treatment of various languages.<p>Vitrum edere possum; mihi non nocet.<br />\u039c\u03c0\u03bf\u03c1\u03ce \u03bd\u03b1 \u03c6\u03ac\u03c9 \u03c3\u03c0\u03b1\u03c3\u03bc\u03ad\u03bd\u03b1 \u03b3\u03c5\u03b1\u03bb\u03b9\u03ac \u03c7\u03c9\u03c1\u03af\u03c2 \u03bd\u03b1 \u03c0\u03ac\u03b8\u03c9 \u03c4\u03af\u03c0\u03bf\u03c4\u03b1.<br />P\xf2di manjar de veire, me nafrari\xe1 pas.<br />\xc9g get eti\xf0 gler \xe1n \xfeess a\xf0 mei\xf0a mig.<br />Ic m\xe6g gl\xe6s eotan ond hit ne hearmia\xf0 me.<br />\u16c1\u16b3\u16eb\u16d7\u16a8\u16b7\u16eb\u16b7\u16da\u16a8\u16cb\u16eb\u16d6\u16a9\u16cf\u16aa\u16be\u16eb\u16a9\u16be\u16de\u16eb\u16bb\u16c1\u16cf\u16eb\u16be\u16d6\u16eb\u16bb\u16d6\u16aa\u16b1\u16d7\u16c1\u16aa\u16a7\u16eb\u16d7\u16d6\u16ec<br />\u280a\u2800\u2809\u2801\u281d\u2800\u2811\u2801\u281e\u2800\u281b\u2807\u2801\u280e\u280e\u2800\u2801\u281d\u2819\u2800\u280a\u281e\u2800\u2819\u2815\u2811\u280e\u281d\u281e\u2800\u2813\u2825\u2817\u281e\u2800\u280d\u2811<br />Pot s\u0103 m\u0103n\xe2nc sticl\u0103 \u0219i ea nu m\u0103 r\u0103ne\u0219te.<br />Meg tudom enni az \xfcveget, nem lesz t\u0151le bajom.<br />M\xf4\u017eem jes\u0165 sklo. Nezran\xed ma.<br /><span dir="rtl" lang="he">\u05d0\u05e0\u05d9 \u05d9\u05db\u05d5\u05dc \u05dc\u05d0\u05db\u05d5\u05dc \u05d6\u05db\u05d5\u05db\u05d9\u05ea \u05d5\u05d6\u05d4 \u05dc\u05d0 \u05de\u05d6\u05d9\u05e7 \u05dc\u05d9.</span><br /><span dir="rtl" lang="ji">\u05d0\u05d9\u05da \u05e7\u05e2\u05df \u05e2\u05e1\u05df \u05d2\u05dc\u05d0\u05b8\u05d6 \u05d0\u05d5\u05df \u05e2\u05e1 \u05d8\u05d5\u05d8 \u05de\u05d9\u05e8 \u05e0\u05d9\u05e9\u05d8 \u05f0\u05f2.</span><br /><span dir="RTL" lang=AR>\u0623\u0646\u0627 \u0642\u0627\u062f\u0631 \u0639\u0644\u0649 \u0623\u0643\u0644 \u0627\u0644\u0632\u062c\u0627\u062c \u0648 \u0647\u0630\u0627 \u0644\u0627 \u064a\u0624\u0644\u0645\u0646\u064a.</span><br />\u042f \u043c\u043e\u0433\u0443 \u0435\u0441\u0442\u044c \u0441\u0442\u0435\u043a\u043b\u043e, \u043e\u043d\u043e \u043c\u043d\u0435 \u043d\u0435 \u0432\u0440\u0435\u0434\u0438\u0442.<br />\u10db\u10d8\u10dc\u10d0\u10e1 \u10d5\u10ed\u10d0\u10db \u10d3\u10d0 \u10d0\u10e0\u10d0 \u10db\u10e2\u10d9\u10d8\u10d5\u10d0.<br />\u053f\u0580\u0576\u0561\u0574 \u0561\u057a\u0561\u056f\u056b \u0578\u0582\u057f\u0565\u056c \u0587 \u056b\u0576\u056e\u056b \u0561\u0576\u0570\u0561\u0576\u0563\u056b\u057d\u057f \u0579\u0568\u0576\u0565\u0580\u0589<br />\u092e\u0948\u0902 \u0915\u093e\u0901\u091a \u0916\u093e \u0938\u0915\u0924\u093e \u0939\u0942\u0901, \u092e\u0941\u091d\u0947 \u0909\u0938 \u0938\u0947 \u0915\u094b\u0908 \u092a\u0940\u0921\u093e \u0928\u0939\u0940\u0902 \u0939\u094b\u0924\u0940.<br />\u0915\u093e\u091a\u0902 \u0936\u0915\u094d\u0928\u094b\u092e\u094d\u092f\u0924\u094d\u0924\u0941\u092e\u094d \u0964 \u0928\u094b\u092a\u0939\u093f\u0928\u0938\u094d\u0924\u093f \u092e\u093e\u092e\u094d \u0965<br />\u0e09\u0e31\u0e19\u0e01\u0e34\u0e19\u0e01\u0e23\u0e30\u0e08\u0e01\u0e44\u0e14\u0e49 \u0e41\u0e15\u0e48\u0e21\u0e31\u0e19\u0e44\u0e21\u0e48\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e09\u0e31\u0e19\u0e40\u0e08\u0e47\u0e1a<br />T\xf4i c\xf3 th\u1ec3 \u0103n th\u1ee7y tinh m\xe0 kh\xf4ng h\u1ea1i g\xec.<br /><span lang="zh">\u6211\u80fd\u541e\u4e0b\u73bb\u7483\u800c\u4e0d\u4f24\u8eab\u4f53\u3002</span><br /><span lang=ja>\u79c1\u306f\u30ac\u30e9\u30b9\u3092\u98df\u3079\u3089\u308c\u307e\u3059\u3002\u305d\u308c\u306f\u79c1\u3092\u50b7\u3064\u3051\u307e\u305b\u3093\u3002</span><br /><span lang=ko>\ub098\ub294 \uc720\ub9ac\ub97c \uba39\uc744 \uc218 \uc788\uc5b4\uc694. \uadf8\ub798\ub3c4 \uc544\ud504\uc9c0 \uc54a\uc544\uc694</span><br />(<a href="http://www.columbia.edu/kermit/utf8.html">http://www.columbia.edu/kermit/utf8.html</a>)'
        id = 24
        title = u'ABOUT POETRY'

    class Portalbox_25:
        body = u'Bienvenue sur le site de d\xe9monstration de Invenio, un logiciel libre pour des serveurs des documents, venant du CERN.  Veuillez explorer les possibilit\xe9s de ce site de d\xe9monstration de tous ses c\xf4t\xe9s.'
        id = 25
        title = u'\xc0 PROPOS DE CE SITE'

    class Portalbox_26:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 26
        title = u'VOIR AUSSI'

    class Portalbox_27:
        body = u'Vitajte na demon\u0161tra\u010dn\xfdch str\xe1nkach Invenio, vo\u013ene dostupn\xe9ho softwaru pre dokumentov\xe9 servery, poch\xe1dzaj\xfaceho z CERNu.  Prehliadnite si mo\u017enosti na\u0161eho demon\u0161tra\u010dn\xe9ho serveru podla \u013eubov\xf4le.'
        id = 27
        title = u'O T\xddCHTO STR\xc1NKACH'

    class Portalbox_28:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 28
        title = u'VI\u010e TIE\u017d'

    class Portalbox_29:
        body = u'V\xedtejte na demonstra\u010dn\xedch str\xe1nk\xe1ch Invenio, voln\u011b dostupn\xe9ho softwaru pro dokumentov\xe9 servery, poch\xe1zej\xedc\xedho z CERNu.  Prohl\xe9dn\u011bte si mo\u017enosti na\u0161eho demonstra\u010dn\xedho serveru podle libosti.'
        id = 29
        title = u'O T\u011aCHTO STR\xc1NK\xc1CH'

    class Portalbox_30:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 30
        title = u'VIZ T\xc9\u017d'

    class Portalbox_31:
        body = u'Willkommen Sie bei der Demo-Seite des Invenio, des Dokument Management Systems Software aus CERN. Hier k\xf6nnen Sie den System gleich und frei ausprobieren.'
        id = 31
        title = u'\xdcBER DIESEN SEITEN'

    class Portalbox_32:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 32
        title = u'SEHEN SIE AUCH'

    class Portalbox_33:
        body = u'Bienvenidos a las p\xe1ginas de demostraci\xf3n de Invenio, un software gratuito desarrollado por el CERN que permite crear un servidor de documentos. Le invitamos a explorar a fondo todas las funcionalidades ofrecidas por estas p\xe1ginas de demostraci\xf3n.'
        id = 33
        title = u'ACERCA DE ESTAS P\xc1GINAS'

    class Portalbox_34:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 34
        title = u'VEA TAMBI\xc9N'

    class Portalbox_35:
        body = u'Benvenuti nel sito demo di Invenio, un software libero per server di documenti sviluppato al CERN. Vi invitiamo ad esplorare a fondo tutte le caratteristiche di questo sito demo.'
        id = 35
        title = u'A PROPOSITO DI QUESTO SITO'

    class Portalbox_36:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 36
        title = u'VEDI ANCHE'

    class Portalbox_37:
        body = u'Velkommen til demosiden for Invenio, en gratis dokumentserver fra CERN. Vennligst f\xf8l deg fri til \xe5 utforske alle mulighetene i denne demoen til det fulle.'
        id = 37
        title = u'OM DENNE SIDEN'

    class Portalbox_38:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 38
        title = u'SE OGS\xc5'

    class Portalbox_39:
        body = u'Bem vindo ao site de demonstra\xe7\xe3o do Invenio, um servidor de documentos livre desenvolvido pelo CERN. Sinta-se \xe0 vontade para explorar plenamente todos os recursos deste site demonstra\xe7\xe3o.'
        id = 39
        title = u'SOBRE ESTE SITE'

    class Portalbox_40:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 40
        title = u'VEJA TAMB\xc9M'

    class Portalbox_41:
        body = u'\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u043d\u0430 \u043d\u0430\u0448 \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0441\u0430\u0439\u0442 Invenio. Invenio -- \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0434\u043b\u044f \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u0432 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432, \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u0430\u044f \u0432 CERN\u0435.  \u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430 \u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435\u0441\u044c \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u043e \u044d\u0442\u0438\u043c \u0441\u0430\u0439\u0442\u043e\u043c.'
        id = 41
        title = u'\u041e\u0411 \u042d\u0422\u041e\u041c \u0421\u0410\u0419\u0422\u0415'

    class Portalbox_42:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 42
        title = u'\u0421\u041c\u041e\u0422\u0420\u0418\u0422\u0415 \u0422\u0410\u041a\u0416\u0415'

    class Portalbox_43:
        body = u'V\xe4lkommen till demoinstallationen av Invenio, en fri programvara f\xf6r hantering av dokument, fr\xe5n CERN. V\xe4lkommen att unders\xf6ka alla funktioner i denna installation.'
        id = 43
        title = u'OM DENNA WEBBPLATS'

    class Portalbox_44:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 44
        title = u'SE \xc4VEN'

    class Portalbox_45:
        body = u'<a href="/submit?doctype=TEXT">Submit a new preprint</a>'
        id = 45
        title = u'SUBMIT PREPRINT'

    class Portalbox_46:
        body = u'<a href="/submit?doctype=TEXT">Submit a new book</a>'
        id = 46
        title = u'SUBMIT BOOK'

    class Portalbox_47:
        body = u'<a href="/submit?doctype=TEXT">Submit a new thesis</a>'
        id = 47
        title = u'SUBMIT THESIS'

    class Portalbox_48:
        body = u'<a href="/submit?doctype=TEXT">Submit a new report</a>'
        id = 48
        title = u'SUBMIT REPORT'

    class Portalbox_49:
        body = u'<a href="/submit?doctype=TEXT">Submit a new article</a>'
        id = 49
        title = u'SUBMIT ARTICLE'

    class Portalbox_50:
        body = u'<a href="/submit?doctype=DEMOPIC">Submit a new picture</a>'
        id = 50
        title = u'SUBMIT PICTURE'

    class Portalbox_51:
        body = u'<a href="/submit?doctype=TEXT">Submit a new article</a><br /><a href="/submit?doctype=TEXT">Submit a new preprint</a>'
        id = 51
        title = u'SUBMIT NEW DOCUMENT'

    class Portalbox_52:
        body = u'<a href="/submit?doctype=TEXT">Submit a new book</a><br /><a href="/submit?doctype=TEXT">Submit a new thesis</a><br /><a href="/submit?doctype=TEXT">Submit a new report</a>'
        id = 52
        title = u'SUBMIT NEW DOCUMENT'

    class Portalbox_53:
        body = u'<a href="/submit?doctype=DEMOPIC">Submit a new picture</a>'
        id = 53
        title = u'SUBMIT NEW DOCUMENT'

    class Portalbox_54:
        body = u'\u039a\u03b1\u03bb\u03c9\u03c2 \u03ae\u03bb\u03b8\u03b1\u03c4\u03b5 \u03c3\u03c4\u03bf\u03bd \u03b4\u03b9\u03ba\u03c4\u03c5\u03b1\u03ba\u03cc \u03c4\u03cc\u03c0\u03bf \u03c4\u03bf\u03c5 Invenio, \u03b5\u03bd\u03cc\u03c2 \u03b4\u03c9\u03c1\u03b5\u03ac\u03bd \u03b5\u03be\u03c5\u03c0\u03b7\u03c1\u03b5\u03c4\u03b7\u03c4\u03ae \u03b3\u03b9\u03b1 \u03ad\u03b3\u03b3\u03c1\u03b1\u03c6\u03b1 \u03c0\u03c1\u03bf\u03b5\u03c1\u03c7\u03cc\u03bc\u03b5\u03bd\u03bf \u03b1\u03c0\u03bf \u03c4\u03bf CERN. \u0395\u03af\u03c3\u03c4\u03b5 \u03b5\u03c5\u03c0\u03c1\u03cc\u03c3\u03b4\u03b5\u03ba\u03c4\u03bf\u03b9 \u03bd\u03b1 \u03b5\u03be\u03b5\u03c1\u03b5\u03c5\u03bd\u03ae\u03c3\u03b5\u03c4\u03b5 \u03c3\u03b5 \u03b2\u03ac\u03b8\u03bf\u03c2 \u03c4\u03b9\u03c2 \u03b4\u03c5\u03bd\u03b1\u03c4\u03cc\u03c4\u03b7\u03c4\u03b5\u03c2 \u03c0\u03bf\u03c5 \u03c3\u03b1\u03c2 \u03c0\u03b1\u03c1\u03ad\u03c7\u03b5\u03b9 \u03bf \u03b4\u03b9\u03ba\u03c4\u03c5\u03b1\u03ba\u03cc\u03c2 \u03b1\u03c5\u03c4\u03cc\u03c2 \u03c4\u03cc\u03c0\u03bf\u03c2.'
        id = 54
        title = u'\u03a3\u03a7\u0395\u03a4\u0399\u039a\u0391 \u039c\u0395 \u03a4\u0397\u039d \u03a3\u0395\u039b\u0399\u0394\u0391'

    class Portalbox_55:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 55
        title = u'\u0394\u0395\u0399\u03a4\u0395 \u0395\u03a0\u0399\u03a3\u0397\u03a3'

    class Portalbox_56:
        body = u'\u041b\u0430\u0441\u043a\u0430\u0432\u043e \u043f\u0440\u043e\u0441\u0438\u043c\u043e \u0434\u043e \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0456\u0439\u043d\u043e\u0433\u043e \u0441\u0430\u0439\u0442\u0443 Invenio, \u0432\u0456\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043d\u043e\u0433\u043e \u0437\u0430\u0431\u0435\u0437\u043f\u0435\u0447\u0435\u043d\u043d\u044f, \u0440\u043e\u0437\u0440\u043e\u0431\u043b\u0435\u043d\u043e\u0433\u043e CERN. \u0412\u0438\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0432\u0441\u0456 \u043c\u043e\u0436\u043b\u0438\u0432\u043e\u0441\u0442\u0456 \u0446\u044c\u043e\u0433\u043e \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0456\u0439\u043d\u043e\u0433\u043e \u0441\u0430\u0439\u0442\u0443 \u0432 \u043f\u043e\u0432\u043d\u043e\u043c\u0443 \u043e\u0431\u0441\u044f\u0437\u0456.'
        id = 56
        title = u'\u041f\u0420\u041e \u0426\u0415\u0419 \u0421\u0410\u0419\u0422'

    class Portalbox_57:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 57
        title = u'\u0414\u0418\u0412\u0418\u0421\u042c \u0422\u0410\u041a\u041e\u0416'

    class Portalbox_58:
        body = u'Benvinguts al lloc de demo de Invenio, un servidor de documents lliure originat al CERN. Us convidem a explorar a fons totes les funcionalitats ofertes en aquestes p\xe0gines de demostraci\xf3.'
        id = 58
        title = u'SOBRE AQUEST LLOC'

    class Portalbox_59:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 59
        title = u'VEGEU TAMB\xc9'

    class Portalbox_60:
        body = u'Invenio\u30c7\u30e2\u30f3\u30b9\u30c8\u30ec\u30fc\u30b7\u30e7\u30f3\u306e\u5834\u6240\u3078\u306e\u6b53\u8fce, CERN \u304b\u3089\u6765\u308b\u81ea\u7531\u306a\u6587\u66f8\u306e\u30b5\u30fc\u30d0\u30fc\u30bd\u30d5\u30c8\u30a6\u30a7\u30a2,    \u3053\u306e\u30c7\u30e2\u30f3\u30b9\u30c8\u30ec\u30fc\u30b7\u30e7\u30f3\u306e\u5834\u6240\u306e\u7279\u5fb4\u3059\u3079\u3066\u3092\u63a2\u691c\u3059\u308b\u81ea\u7531\u306e\u611f\u3058'
        id = 60
        title = u'\u3053\u306e\u5834\u6240\u306b\u3064\u3044\u3066'

    class Portalbox_61:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 61
        title = u'\u307e\u305f\u898b\u306a\u3055\u3044'

    class Portalbox_62:
        body = u'Witamy w wersji demo systemu Invenio, darmowego oprogramowania do obs\u0142ugi serwera dokument\xf3w, stworzonego w CERN. Zach\u0119camy do odkrywania wszelkich funkcjonalno\u015bci oferowanych przez t\u0119 stron\u0119.'
        id = 62
        title = u'O TEJ STRONIE'

    class Portalbox_63:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 63
        title = u'ZOBACZ TAK\u017bE'

    class Portalbox_64:
        body = u'\u0414\u043e\u0431\u0440\u0435 \u0434\u043e\u0448\u043b\u0438 \u043d\u0430 \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u0438\u044f \u0441\u0430\u0439\u0442 \u043d\u0430 Invenio, \u0441\u0432\u043e\u0431\u043e\u0434\u0435\u043d \u0441\u043e\u0444\u0442\u0443\u0435\u0440 \u0437\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043d\u0438 \u0441\u044a\u0440\u0432\u044a\u0440\u0438 \u0438\u0437\u0440\u0430\u0431\u043e\u0442\u0435\u043d \u0432 \u0426\u0415\u0420\u041d. \u0427\u0443\u0432\u0441\u0442\u0432\u0430\u0439\u0442\u0435 \u0441\u0435 \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u0438 \u0434\u0430 \u0438\u0437\u0441\u043b\u0435\u0434\u0432\u0430\u0442\u0435 \u0432\u0441\u044f\u043a\u0430 \u0435\u0434\u043d\u0430 \u043e\u0442 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438\u0442\u0435 \u043d\u0430 \u0441\u0430\u0439\u0442\u0430.'
        id = 64
        title = u'\u0417\u0410 \u0421\u0410\u0419\u0422\u0410'

    class Portalbox_65:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 65
        title = u'\u0412\u0418\u0416 \u0421\u042a\u0429\u041e'

    class Portalbox_66:
        body = u'Dobrodo\u0161li na Invenio demo site. Invenio je slobodno dostupan poslu\u017eitelj dokumenata razvijen na CERN-u. Slobodno istra\u017eite sve mogu\u0107nosti ove aplikacije.'
        id = 66
        title = u'O OVOM SITE-u'

    class Portalbox_67:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 67
        title = u'TAKO\u0110ER POGLEDAJTE'

    class Portalbox_68:
        body = u'\u6b22\u8fce\u6765\u5230Invenio \u7684\u793a\u8303\u7f51\u7ad9\uff01Invenio\u662f\u4e00\u4e2a\u7531CERN\u5f00\u53d1\u7684\u514d\u8d39\u6587\u4ef6\u670d\u52a1\u5668\u8f6f\u4ef6\u3002 \u8981\u4e86\u89e3\u8fd9\u7f51\u7ad9\u6240\u63d0\u4f9b\u7684\u5404\u9879\u7279\u70b9, \u8bf7\u7acb\u523b\u884c\u52a8\uff0c\u5c3d\u60c5\u63a2\u7d22\u3002'
        id = 68
        title = u'\u5173\u4e8e\u8fd9\u4e2a\u7f51\u7ad9'

    class Portalbox_69:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 69
        title = u'\u53c2\u89c1'

    class Portalbox_70:
        body = u'\u6b61\u8fce\u4f86\u5230Invenio \u7684\u793a\u7bc4\u7db2\u7ad9\uff01Invenio\u662f\u4e00\u500b\u7531CERN\u958b\u767c\u7684\u514d\u8cbb\u6587\u4ef6\u4f3a\u670d\u5668\u8edf\u9ad4\u3002 \u8981\u77ad\u89e3\u9019\u7db2\u7ad9\u6240\u63d0\u4f9b\u7684\u5404\u9805\u7279\u9ede, \u8acb\u7acb\u523b\u884c\u52d5\uff0c\u76e1\u60c5\u63a2\u7d22\u3002'
        id = 70
        title = u'\u95dc\u65bc\u9019\u500b\u7db2\u7ad9'

    class Portalbox_71:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 71
        title = u'\u53c3\u898b'

    class Portalbox_72:
        body = u'\xdcdv\xf6z\xf6lj\xfck a Invenio bemutat\xf3oldalain! Ezt a szabad dokumentumkezel\u0151 szoftvert a CERN-ben fejlesztett\xe9k. Fedezze fel b\xe1tran a tesztrendszer ny\xfajtotta szolg\xe1ltat\xe1sokat!'
        id = 72
        title = u'IMPRESSZUM'

    class Portalbox_73:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 73
        title = u'L\xc1SD M\xc9G'

    class Portalbox_74:
        body = u'Welkom by die demo tuiste van Invenio, gratis dokument bediener sagteware wat deur CERN geskryf is. Voel vry om al die eienskappe van die demo te deursoek.'
        id = 74
        title = u'OMTRENT HIERDIE TUISTE'

    class Portalbox_75:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 75
        title = u'SIEN OOK'

    class Portalbox_76:
        body = u'Benvido \xf3 sitio de demostraci\xf3n do Invenio, un software de servidor de documentos do CERN. Por favor s\xedntete libre de explorar todas as caracter\xedsticas deste sitio de demostraci\xf3n.'
        id = 76
        title = u'ACERCA DESTE SITIO'

    class Portalbox_77:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 77
        title = u'VEXA TAM\xc9N'

    class Portalbox_78:
        body = u'The "Atlantis Times" collections contain the articles from the <a href="/journal/atlantistimes/">Atlantis Times</a> journal.'
        id = 78
        title = u'ABOUT ATLANTIS TIMES'

    class Portalbox_79:
        body = u'Bine a\u0163i venit pe site-ul demo al Invenio, un software gratuit pentru servere de documente, creat de CERN. Nu ezita\u0163i s\u0103 explora\u0163i din plin toate caracteristicile acestui site demo.'
        id = 79
        title = u'DESPRE ACEST SITE'

    class Portalbox_80:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 80
        title = u'ALTE RESURSE'

    class Portalbox_81:
        body = u"Murakzaneza kuri web ya Invenio, iyi ni koranabuhanga y'ubuntu ya kozwe na CERN. Bitimuntu afite uburenganzira bwo kuyigerageza no kuyikoresha."
        id = 81
        title = u"IBYEREKERANYE N'IYI WEB"

    class Portalbox_82:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 82
        title = u"REBA N'IBI"

    class Portalbox_83:
        body = u'\u10d9\u10d4\u10d7\u10d8\u10da\u10d8 \u10d8\u10e7\u10dd\u10e1 \u10d7\u10e5\u10d5\u10d4\u10dc\u10d8 \u10db\u10dd\u10d1\u10e0\u10eb\u10d0\u10dc\u10d4\u10d1\u10d0 Invenio -\u10d8\u10e1 \u10e1\u10d0\u10d3\u10d4\u10db\u10dd\u10dc\u10e1\u10e2\u10e0\u10d0\u10ea\u10d8\u10dd \u10e1\u10d0\u10d8\u10e2\u10d6\u10d4, \u10d7\u10d0\u10d5\u10d8\u10e1\u10e3\u10e4\u10d0\u10da\u10d8 \u10d3\u10dd\u10d9\u10e3\u10db\u10d4\u10dc\u10e2\u10d4\u10d1\u10d8\u10e1 \u10e1\u10d4\u10e0\u10d5\u10d4\u10e0\u10d8 CERN -\u10d8\u10e1\u10d0\u10d2\u10d0\u10dc. \u10d2\u10d7\u10ee\u10dd\u10d5\u10d7 \u10e1\u10e0\u10e3\u10da\u10d0\u10d3 \u10e8\u10d4\u10d8\u10e1\u10ec\u10d0\u10d5\u10da\u10dd\u10d7 \u10e1\u10d0\u10d3\u10d4\u10db\u10dd\u10dc\u10e1\u10e2\u10e0\u10d0\u10ea\u10d8\u10dd \u10e1\u10d0\u10d8\u10e2\u10d8\u10e1 \u10e8\u10d4\u10e1\u10d0\u10eb\u10da\u10d4\u10d1\u10da\u10dd\u10d1\u10d4\u10d1\u10d8.'
        id = 83
        title = u'\u10e1\u10d0\u10d8\u10e2\u10d8\u10e1 \u10e8\u10d4\u10e1\u10d0\u10ee\u10d4\u10d1'

    class Portalbox_84:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 84
        title = u'\u10d0\u10e1\u10d4\u10d5\u10d4 \u10d8\u10ee\u10d8\u10da\u10d4\u10d7'

    class Portalbox_85:
        body = u'Sveiki atvyk\u0119 \u012f Invenio bandom\u0105j\u012f tinklap\u012f. Invenio yra nemokama programin\u0117 \u012franga dokument\u0173 serveriams, sukurta CERN. Kvie\u010diame i\u0161bandyti visas tinklapio galimybes ir funkcijas.'
        id = 85
        title = u'APIE PUSLAP\u012e'

    class Portalbox_86:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 86
        title = u'TAIP PAT \u017dI\u016aR\u0116KITE'

    class Portalbox_87:
        body = u'\u0645\u0631\u062d\u0628\u0627 \u0628\u0643\u0645 \u0641\u064a \u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u062a\u062c\u0631\u064a\u0628\u064a \u0644\u0625\u0646\u0641\u064a\u0646\u064a\u0648\u060c \u0627\u0644\u0645\u062d\u0637\u0629 \u0627\u0644\u062e\u0627\u062f\u0645\u0629 (\u0627\u0644\u062d\u0631\u0629) \u0627\u0644\u0645\u0628\u0631\u0645\u062c\u0629 \u0645\u0646 \u0637\u0631\u0641 \u0627\u0644\u0645\u0646\u0638\u0645\u0629 \u0627\u0644\u0623\u0648\u0631\u0628\u064a\u0629 \u0644\u0644\u0628\u062d\u0648\u062b \u0627\u0644\u0646\u0648\u0648\u064a\u0629. \u0627\u0644\u0631\u062c\u0627\u0621 \u0639\u062f\u0645 \u0627\u0644\u062a\u0631\u062f\u062f \u0644\u0644\u0625\u0637\u0644\u0627\u0639 \u0639\u0644\u0649 \u062c\u0645\u064a\u0639 \u0635\u0641\u062d\u0627\u062a \u0647\u0630\u0627 \u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u062a\u062c\u0631\u064a\u0628\u064a'
        id = 87
        title = u'\u062d\u0648\u0644 \u0647\u0630\u0627 \u0627\u0644\u0645\u0648\u0642\u0639'

    class Portalbox_88:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 88
        title = u'\u0632\u0648\u0631\u0648\u0627 \u0623\u064a\u0636\u0627'

    class Portalbox_89:
        body = u'The Notes collection is a temporary collection that is being used for testing.'
        id = 89
        title = u'ABOUT Notes'

    class Portalbox_90:
        body = u'The ALEPH Papers collection is a temporary collection that is being used for testing.'
        id = 90
        title = u'ABOUT ALEPH Papers'

    class Portalbox_91:
        body = u'The ALEPH Internal Notes collection is a temporary restricted collection that is being used for testing.'
        id = 91
        title = u'ABOUT ALEPH Internal Notes'

    class Portalbox_92:
        body = u'The ALEPH Theses collection is a temporary restricted collection that is being used for testing.'
        id = 92
        title = u'ABOUT ALEPH Theses'

    class Portalbox_93:
        body = u'The ISOLDE Papers collection is a temporary collection that is being used for testing.'
        id = 93
        title = u'ABOUT ISOLDE Papers'

    class Portalbox_94:
        body = u'The ISOLDE Internal Notes collection is a temporary restricted and hidden collection that is being used for testing.'
        id = 94
        title = u'ABOUT ISOLDE Internal Notes'

    class Portalbox_95:
        body = u'The Drafts collection is a temporary restricted collection that is being used for testing.'
        id = 95
        title = u'ABOUT Drafts'
