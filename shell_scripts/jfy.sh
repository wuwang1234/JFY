#vim /etc/init.d/httpd
#!bin/bash
lock="manager.py"
#启动服务方法
start(){
    echo "service start...."
    su root -c "python ../manager.py runserver --host 0.0.0.0 &"
}
<pre name="code" class="plain">#停止服务方法
stop(){ echo "service stop...." pkill -f $lock}
#查看服务状态
status(){
    if [ -e $lock ];then
      echo "$0 service start"
    else
      echo "$0 service stop"
    fi
}
#重新启动
restart(){
    stop
    start
}
case "$1" in
"start")
    start
    ;;
"stop")
    stop
    ;;
"status")
    status
    ;;
"restart")
    restart
    ;;
*)
    echo "$0 start|stop|status|restart"
    ;;
esac