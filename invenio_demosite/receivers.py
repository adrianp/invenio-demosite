# -*- coding: utf-8 -*-
#
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
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

from datetime import datetime
from fixture import DataSet

from invenio.base.factory import with_app_context


@with_app_context(new_context=True)
def post_handler_demosite_populate(sender, default_data='', *args, **kwargs):
    """Loads data after records are created."""

    if default_data != 'demosite':
        print '>>> You can define your own post hadler for `demosite populate`'
    print '>>> Loading demosite data for Comments ...'

    class CmtRECORDCOMMENTData(DataSet):
        class C1:
            id = 1
            id_bibrec = 1
            id_user = 2
            title = 'Small comment on the abstract'
            body = 'P.1: S.Abstract: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec interdum nisi ut nibh porta, non viverra neque faucibus.'
            date_creation = datetime.now()
            star_score = 0
            nb_votes_yes = 0
            nb_votes_total = 0
            nb_abuse_reports = 0
            status = 'ok'
            round_name = ''
            restriction = ''
            in_reply_to_id_cmtRECORDCOMMENT = 0

        class C2:
            id = 2
            id_bibrec = 1
            id_user = 2
            title = 'RE: Small comment on the abstract'
            body = '>>P.1: S.Abstract: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec interdum nisi ut nibh porta, non viverra neque faucibus.\n\nYes, you are right! Moreover:\nP.1: S.Abstract: Fusce porttitor, nibh vitae vulputate rutrum, dui libero suscipit erat, eget iaculis dolor dui nec enim.'
            date_creation = datetime.now()
            star_score = 0
            nb_votes_yes = 0
            nb_votes_total = 0
            nb_abuse_reports = 0
            status = 'ok'
            round_name = ''
            restriction = ''
            in_reply_to_id_cmtRECORDCOMMENT = 1

        class C3:
            id = 3
            id_bibrec = 1
            id_user = 3
            title = ''
            body = 'P.4: F.1: Sed id consequat mauris, a tempor ligula. Duis porttitor pulvinar diam, quis ornare enim consequat nec.'
            date_creation = datetime.now()
            star_score = 0
            nb_votes_yes = 0
            nb_votes_total = 0
            nb_abuse_reports = 0
            status = 'ok'
            round_name = ''
            restriction = ''
            in_reply_to_id_cmtRECORDCOMMENT = 0

        class C4:
            id = 4
            id_bibrec = 1
            id_user = 4
            title = ''
            body = 'P.1: Aenean sed fermentum ligula, eget varius elit. Quisque pretium vestibulum nulla, at rutrum dui. Donec vitae bibendum ipsum.\nP.2: PP.3: Aenean vel gravida lacus, non posuere neque. Proin quis eros egestas, vulputate leo et, aliquam sapien.'
            date_creation = datetime.now()
            star_score = 0
            nb_votes_yes = 0
            nb_votes_total = 0
            nb_abuse_reports = 0
            status = 'ok'
            round_name = ''
            restriction = ''
            in_reply_to_id_cmtRECORDCOMMENT = 0

        class C5:
            id = 5
            id_bibrec = 1
            id_user = 5
            title = 'Minor comment on first equation'
            body = 'Vivamus laoreet, velit id congue molestie, velit tellus dignissim arcu, non placerat quam nisl id lorem.\n\nP.5: E.1: Quisque vehicula tempor tempor. Vestibulum tempor posuere felis in interdum. Donec quis lorem id felis mattis fermentum.'
            date_creation = datetime.now()
            star_score = 0
            nb_votes_yes = 0
            nb_votes_total = 0
            nb_abuse_reports = 0
            status = 'ok'
            round_name = ''
            restriction = ''
            in_reply_to_id_cmtRECORDCOMMENT = 0

        class C6:
            id = 6
            id_bibrec = 1
            id_user = 6
            title = 'Praesent nec lorem tellus.'
            body = 'P.5: Praesent velit velit, consectetur nec mattis ut, dapibus id metus.\nProin sit amet libero tellus. Donec sed rutrum diam, ut iaculis arcu.'
            date_creation = datetime.now()
            star_score = 0
            nb_votes_yes = 0
            nb_votes_total = 0
            nb_abuse_reports = 0
            status = 'ok'
            round_name = ''
            restriction = ''
            in_reply_to_id_cmtRECORDCOMMENT = 0

        class C7:
            id = 7
            id_bibrec = 1
            id_user = 7
            title = 'RE: Praesent nec lorem tellus.'
            body = '>>P.5: Praesent velit velit, consectetur nec mattis ut, dapibus id metus.\nProin sit amet libero tellus. Donec sed rutrum diam, ut iaculis arcu.\nP.5: Phasellus mattis sodales nisl, quis euismod diam consectetur sit amet.'
            date_creation = datetime.now()
            star_score = 0
            nb_votes_yes = 0
            nb_votes_total = 0
            nb_abuse_reports = 0
            status = 'ok'
            round_name = ''
            restriction = ''
            in_reply_to_id_cmtRECORDCOMMENT = 6

        class C8:
            id = 8
            id_bibrec = 1
            id_user = 8
            title = ''
            body = 'P.14: R.[1]: Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Integer purus sapien, varius egestas justo sit amet, placerat consectetur lorem.'
            date_creation = datetime.now()
            star_score = 0
            nb_votes_yes = 0
            nb_votes_total = 0
            nb_abuse_reports = 0
            status = 'ok'
            round_name = ''
            restriction = ''
            in_reply_to_id_cmtRECORDCOMMENT = 0

    fixtures = [CmtRECORDCOMMENTData]

    try:
        from invenio.ext.sqlalchemy import db
        from fixture import SQLAlchemyFixture
        from invenio.modules.comments import models as comments_model

        models = dict((m.__name__, getattr(comments_model, m.__name__[:-4]))
                      for m in fixtures)

        dbfixture = SQLAlchemyFixture(env=models, engine=db.metadata.bind,
                                      session=db.session)
        data = dbfixture.data(*fixtures)

        print ">>> There are", len(models), "tables to be loaded."
        data.setup()

        print ">>> Comments demosite data has been loaded."
    except Exception as e:
        print ">>> FAIL: data has not been loaded", e
