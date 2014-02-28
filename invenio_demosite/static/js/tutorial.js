/**
This file is part of Invenio.
Copyright (C) 2014 CERN.

Invenio is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the
License, or (at your option) any later version.

Invenio is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with Invenio; if not, write to the Free Software Foundation, Inc.,
59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
**/

'use strict';

/* global introJs */

/* exported TUTORIAL */

var TUTORIAL = (function($) {

    var IJS;
    var ON_COMPLETE_CALLBACK = function() { return; };

    function indexPageComplete() {
        window.location.href = 'collection/Annotation%20Demo';
    }

    function colPageComplete() {
        window.location.href = '/record/1/notes';
    }

    function notePageComplete() {
        window.location.href = '/record/1/comments';
    }

    function tutorialFinish() {
        $.removeCookie('tutorial', { path: '/' });
    }

    $(document).ready(function() {
        IJS = introJs();
        IJS.setOptions({'skipLabel': 'Exit', 'showBullets': false, 'showStepNumbers': false});

        switch(window.location.pathname) {
            case '/':
                IJS.setOption('doneLabel', 'Next &rarr;');
                ON_COMPLETE_CALLBACK = indexPageComplete;
                return;
            case '/collection/Annotation%20Demo':
                if($.cookie('tutorial')) {
                    IJS.setOption('doneLabel', 'Next &rarr;');
                    ON_COMPLETE_CALLBACK = colPageComplete;
                    start();
                }
                return;
            case '/record/1/comments':
                IJS.setOption('doneLabel', 'OK, finish tour.');
                if($.cookie('tutorial')) {
                    ON_COMPLETE_CALLBACK = tutorialFinish;
                    start();
                }
                return;
            case '/record/1/notes':
                IJS.setOption('doneLabel', 'Next &rarr;');
                if($.cookie('tutorial')) {
                    ON_COMPLETE_CALLBACK = notePageComplete;
                    start();
                }
                return;
            default:
                return;
        }
    });

    function start(first) {
        if(first) {
            $.cookie('tutorial', true, { path: '/' });
        }
        IJS.start().oncomplete(ON_COMPLETE_CALLBACK).onexit(tutorialFinish);
    }

    return {
        start: start
    };
})(window.jQuery);
