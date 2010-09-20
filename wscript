#! /usr/bin/env python

APPNAME='lgi'
VERSION='0.1'

top = '.'
out = 'build'

def options(opt) :
    opt.tool_options('compiler_cc')
    opt.add_option('--enable-debugging', action='store_true', dest='debug',
                   default=False, help='Enable debugging mode.')

def configure(conf) :
    import Options
    conf.check_tool('compiler_cc')
    conf.check_cfg(package='lua5.1',
                   args='--cflags --libs', uselib_store='LUA')
    conf.check_cfg(package='gobject-introspection-1.0',
                   args='--cflags --libs', uselib_store='GI')
    conf.env.append_unique('CCFLAGS', Options.options.debug and '-g' or '-O2')

def build(bld) :
    bld.recurse('src')