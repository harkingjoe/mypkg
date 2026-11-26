import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.srv import Query   #変更: 作ったPerson型を使う

rclpy.init()                     #rclpyの初期化（最初に1回）
node = Node("talker")

def cb(request, response):          #変更: 依頼が来るたびに呼ばれる
    if request.name == "金城陽飛":   #変更: 依頼（request）のnameを見る
        response.age = 20           #変更: 返事（response）のageに年齢を入れる
    else:
        response.age = 255          #変更: 知らない人なら255
    return response                 #変更: 返事を返す

def main():
    srv = node.create_service(Query, "query", cb)   #変更: サービスを作成（型、名前、関数
    rclpy.spin(node)            #実行（無限ループ。タイマーや送受信を処理し続ける）
