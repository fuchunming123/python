from qbittorrent import Client



if __name__ == "__main__":
    client = Client('120.0.0.1:8080')  #实例化qbittorrentwebAPI客户端实例
    client.login(username='admin',password='123456')
    client.increasePrio("47fae912dfd14863fd8ba1f96f0e74d21d57bf63")
    #client.("magnet:?xt=urn:btih:47fae912dfd14863fd8ba1f96f0e74d21d57bf63&dn=%e9%98%b3%e5%85%89%e7%94%b5%e5%bd%b1dy.ygdy8.com.%e6%b0%94%e5%9e%ab%e4%bc%a0%e5%a5%87.2023.HD.1080P.%e8%8b%b1%e8%af%ad%e4%b8%ad%e5%ad%97.mkv&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce")
    #client.addTrackers("47fae912dfd14863fd8ba1f96f0e74d21d57bf63","magnet:?xt=urn:btih:47fae912dfd14863fd8ba1f96f0e74d21d57bf63&dn=%e9%98%b3%e5%85%89%e7%94%b5%e5%bd%b1dy.ygdy8.com.%e6%b0%94%e5%9e%ab%e4%bc%a0%e5%a5%87.2023.HD.1080P.%e8%8b%b1%e8%af%ad%e4%b8%ad%e5%ad%97.mkv&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce")