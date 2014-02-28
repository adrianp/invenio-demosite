/*
 * This file is part of Invenio.
 * Copyright (C) 2014 CERN.
 *
 * Invenio is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of the
 * License, or (at your option) any later version.
 *
 * Invenio is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Invenio; if not, write to the Free Software Foundation, Inc.,
 * 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
 */

'use strict';

/* global module */
/* global require */

module.exports = function (grunt) {
    require('time-grunt')(grunt);  // show elapsed time at the end
    require('load-grunt-tasks')(grunt);  // load all grunt tasks

    var globalConfig = {
        bower_path: 'bower_components',
    };

    var buildConfig = {
        develop: 'instance/static',
        deploy: 'invenio/base/static'
    };

    // Project configuration
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        globalConfig: globalConfig,
        buildConfig: buildConfig,
        copy: {
            css: {
                expand: true,
                flatten: true,
                cwd: '<%= globalConfig.bower_path %>',
                src: ['intro.js/minified/introjs.min.css'],
                dest: '<%= grunt.option(\'target\') %>/css/'
            },

            introjs: {
                expand: true,
                flatten: true,
                cwd: '<%= globalConfig.bower_path %>/',
                src: ['intro.js/minified/intro.min.js'],
                dest: '<%= grunt.option(\'target\') %>/js/',
            },

            jquerycookie: {
                expand: true,
                flatten: true,
                cwd: '<%= globalConfig.bower_path %>/',
                src: ['jquery-cookie/jquery.cookie.js'],
                dest: '<%= grunt.option(\'target\') %>/js/',
            },
        },  // copy task

        actualclean: {
            css: {
                expand: true,
                cwd: '<%= grunt.option(\'target\') %>/css/',
                src: ['introjs.min.css']
            },

            js: {
                expand: true,
                cwd: '<%= grunt.option(\'target\') %>/js/',
                src: ['intro.min.js', 'jquery.cookie.js']
            },

            //clean the folder if it's empty
            empty: {
                src: '<%= grunt.option(\'target\') %>/**/*',
                filter: function(filepath) {
                    return (grunt.file.isDir(filepath) &&
                            require('fs').readdirSync(filepath).length === 0);
                }
            }
        }  // clean task
    });

    // build task
    grunt.registerTask('build', 'Set the output folder for the build.', function () {
        if (grunt.option('path') === undefined) {
            if (grunt.option('target') === 'develop') {
                grunt.option('target', buildConfig.develop);
            } else if (grunt.option('target') === 'deploy') {
                grunt.option('target', buildConfig.deploy);
            } else if (grunt.option('target') === undefined) {
                grunt.option('target', buildConfig.develop);
            } else {
                grunt.task.run('help');
                return;
            }
            grunt.task.run(['copy']);
        } else {
            grunt.option('target', grunt.option('path'));
            grunt.task.run(['copy']);
        }
    });

    // clean task
    grunt.renameTask('clean', 'actualclean');

    grunt.registerTask('clean', 'Clean the files.', function () {
        if (grunt.option('path') === undefined) {
            if (grunt.option('target') === 'develop') {
                grunt.option('target', buildConfig.develop);
            } else if (grunt.option('target') === 'deploy') {
                grunt.option('target', buildConfig.deploy);
            } else if (grunt.option('target') === undefined) {
                grunt.option('target', buildConfig.develop);
            } else {
                grunt.task.run('help');
                return;
            }
            grunt.task.run('actualclean');
        } else {
            grunt.option('target', grunt.option('path'));
            grunt.task.run('actualclean');
        }
    });

    // help task
    grunt.registerTask('help', 'Help menu.', function () {
        grunt.log.writeln(
            '\nAvailable options for Grunt' + '\n\n' +
            'Building:' + '\n' +
            'grunt build --target=develop # build for development mode' + '\n' +
            'grunt build --target=deploy  # build for deployment mode' + '\n' +
            'grunt build                  # build for development mode' + '\n\n' +
            'Building with custom paths:' + '\n' +
            'grunt build --path=path/to/folder  # build for custom mode' + '\n\n' +
            'Cleaning:' + '\n' +
            'grunt clean --target=develop # clean for development mode' + '\n' +
            'grunt clean --target=deploy  # clean for deployment mode' + '\n' +
            'grunt clean                  # clean for development mode' + '\n\n' +
            'Cleaning with custom paths:' + '\n' +
            'grunt clean --path=path/to/folder  # clean for custom mode' + '\n');
        });
};
