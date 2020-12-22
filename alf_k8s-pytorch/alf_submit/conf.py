class Config(object):
    alf_version="0.0.5"               # which alf docker version to use
    #traincli_version="3.0.6"                   # which traincli version to use
    username="haonan.yu"                       # username on the devserver
    server_address="gpu-dev016.hogpu.cc"       # devserver address
    clusters={"algo-small": dict(appid="", appkey=""),
              "share-1080ti": dict(appid="", appkey="),
              "share-rtx": dict(appid="", appkey=""),
              "share-2080ti": dict(appid="", appkey="")}
    alf_dir="~/alf"                            # alf root dir on desktop
    socialbot_dir="~/SocialRobot"              # socialbot root dir on desktop
    work_home="test_gail"                      # working directory on devserver
