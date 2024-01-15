set -e

mkdir -p /home/box/project
touch /home/box/project/{util,main,helper,project,__init__}{,_helper,_init,_test}.py

chown -R box:box /home/box/project
