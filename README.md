## 轨迹接口说明
安装最新版本的包channels，在/ourcharts/setting.py配置好数据库。进入django工程后，运行python manage.py runserver即可。目前仅支持根据order_id返回相应的查询记录。连接建立后后台将查询结果缓存在服务器中，当前传送轨迹的时间间隔为实际时间的30倍。可以在/ourcharts/taxi/consumer.py 中修改相应的时间传送间隔（已添加注释）。传送完成后台自动将websocket链接关闭。可同时建立多个链接
#### 请求说明
    请求方式：websocket
	请求URL：ws://127.0.0.1/ws/track/
#### 请求文本
	{ 'message': order_id}   
#### 返回示例
	返回结果为json格式的字符串，转换可得
	{
    "status":1,
    "state":"success",
    "message":"{'time_stamp': 1477969982, 'order_id': '39a096b71376b82f35732eff6d95779b', 'driver_id': '8f20c9188561b796ef8e26196de30be4', 'longitude': 104.11570293699263, 'latitude': 30.69954721859711}"
	}





