import os
import sys
import shutil

BASE_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

sys.path.insert(0, os.path.join(ROOT_DIR))


def build_docs(output_dir):
    import epx
    from jinja2 import Environment, FileSystemLoader

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    env = Environment(loader=FileSystemLoader(os.path.join(ROOT_DIR, 'docs')))
    context = {
        'app' : {
            'name': epx.__name__,
            'version': epx.__version__,
            'help_logo_path': "./assets/imgs/logo-md.png",
            'report_logo_path': "<%- logo_path %>"
        }
    }

    for name in ['help', 'report']:
        tmpl = env.get_template('%s.tpl' % name)
        context['title'] = name.title()
        context['app']['logo_path'] = context['app']['%s_logo_path' % name]
        
        target_file = os.path.join(output_dir, '%s.html' % name)
        with open(target_file, 'w') as f:
            f.write(tmpl.render(**context))
            f.flush()


def build_app(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    args = {
        'icon': os.path.join(BASE_DIR, 'epx.ico'),
        'spec': os.path.join(BASE_DIR, 'pyinstaller.spec')
    }
    command = "pyinstaller --icon=%(icon)s %(spec)s"
    os.system(command % args)


def build():
    app_dirname = 'ePinXtractr'

    # move out ePinXtractr folder
    output_dir = os.getcwd()
    dir_dist = os.path.join(output_dir, 'dist')
    dir_app = os.path.join(dir_dist, app_dirname)
    if os.path.exists(dir_app):
        shutil.rmtree(dir_app)

    build_app(output_dir)
    shutil.move(os.path.join(dir_dist, 'bin', app_dirname), dir_dist)
    shutil.move(os.path.join(dir_dist, 'bin'), dir_app)
    
    build_docs(dir_app)
    
    shutil.move(os.path.join(dir_app, 'report.html'),
                os.path.join(dir_app, 'assets', 'report.tpl'))
    print("\nDone!\n")


build()